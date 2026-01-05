import pygame
import time
import random
from player import player

WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Sword Duel")
sprite_idle = pygame.image.load("Assets/Samurai/Idle.png").convert_alpha()
BG = pygame.transform.scale(pygame.image.load("background.jpg"),(WIDTH,HEIGHT))


def draw_bg():
    WINDOW.blit(BG,(0,0))
    
def main():
    player_animations = {
        "idle": (pygame.image.load("Assets/Samurai/Idle.png").convert_alpha(), 128, 128, 6),
        "attack": (pygame.image.load("Assets/Samurai/Attack_1.png").convert_alpha(), 128, 128, 4),
        "hurt": (pygame.image.load("Assets/Samurai/Hurt.png").convert_alpha(), 128, 128, 3)
    }

    player1 = player(
        x=100,
        y=280,
        animations=player_animations,
        damage=10,
        health=100,
        anim_speed=15,
        scale=3
)
    FPS = 60
    run = True
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player1.set_animation("attack")
        if player1.current_animation == "attack" and player1.current_frame == len(player1.frames)-1:
            player1.set_animation("idle")

        draw_bg()
        
        player1.update()
        player1.draw(WINDOW)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()
