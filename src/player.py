import pygame

class player:
    def __init__(self, x, y, animations, damage, health, scale=2, anim_speed=5):
        self.x = x
        self.y = y
        self.damage = damage
        self.health = health
        self.scale = scale
        self.HEALTH_BAR_WIDTH = 200
        self.HEALTH_BAR_HEIGHT = 20
        self.HEALTH_BAR_OFFSET_Y = 60
        self.animations = {}

        # Preload all animations
        for name, data in animations.items():
            sprite_sheet, frame_width, frame_height, num_frames = data
            frames = []
            for i in range(num_frames):
                frame = self.get_image(sprite_sheet, frame_width, frame_height, i)
                frame = pygame.transform.scale(frame, (frame_width * scale, frame_height * scale))
                frames.append(frame)
            self.animations[name] = frames

        # Start with idle animation
        self.current_animation = "idle"
        self.frames = self.animations[self.current_animation]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]

        self.anim_speed = anim_speed
        self.anim_counter = 0

    def get_image(self, sheet, width, height, frame_x=0):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), (frame_x * width, 0, width, height))
        return image

    def update(self):
        self.anim_counter += 1
        if self.anim_counter >= self.anim_speed:
            self.current_frame += 1
            if self.current_frame >= len(self.frames):
                self.current_frame = 0
            self.image = self.frames[self.current_frame]
            self.anim_counter = 0

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def set_animation(self, name):
        if self.current_animation != name:
            self.current_animation = name
            self.frames = self.animations[name]
            self.current_frame = 0
            self.anim_counter = 0
            self.image = self.frames[self.current_frame]
    def draw_health_bar(self, window):
        # Calculate health ratio
        health_ratio = self.health / 100  # if max health is 100
        bar_width = int(self.HEALTH_BAR_WIDTH * health_ratio)

        # Background (red)
        pygame.draw.rect(
            window,
            (255, 0, 0),
            (self.x, self.y + self.HEALTH_BAR_OFFSET_Y, self.HEALTH_BAR_WIDTH, self.HEALTH_BAR_HEIGHT)
        )

        # Foreground (green)
        pygame.draw.rect(
            window,
            (0, 255, 0),
            (self.x, self.y + self.HEALTH_BAR_OFFSET_Y, bar_width, self.HEALTH_BAR_HEIGHT)
        )

        # Optional: border
        pygame.draw.rect(
            window,
            (0, 0, 0),
            (self.x, self.y + self.HEALTH_BAR_OFFSET_Y, self.HEALTH_BAR_WIDTH, self.HEALTH_BAR_HEIGHT),
            2  # thickness
        )
    def attack(self,target):
        target.health -= self.damage
