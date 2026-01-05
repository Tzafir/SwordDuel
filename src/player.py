import pygame

class player:
    def __init__(self, x, y, animations, damage, health, scale=2, anim_speed=5):
        self.x = x
        self.y = y
        self.damage = damage
        self.health = health
        self.scale = scale
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
