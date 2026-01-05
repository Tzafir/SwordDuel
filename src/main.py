import pygame
import time
import random
from player import player
from enemy import enemy


WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Sword Duel")
sprite_idle = pygame.image.load("Assets/Samurai/Idle.png").convert_alpha()
BG = pygame.transform.scale(pygame.image.load("background.jpg"),(WIDTH,HEIGHT))


def draw_bg():
    WINDOW.blit(BG,(0,0))
    
def main():
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 64)
    player_animations = {
        "idle": (pygame.image.load("Assets/Samurai/Idle.png").convert_alpha(), 128, 128, 6),
        "attack": (pygame.image.load("Assets/Samurai/Attack_1.png").convert_alpha(), 128, 128, 4),
        "hurt": (pygame.image.load("Assets/Samurai/Hurt.png").convert_alpha(), 128, 128, 3)
    }
    enemy_animations = {
        "idle": [
            "Enemy/Golem_1/PNG/PNG Sequences/Idle/0_Golem_Idle_000.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Idle/0_Golem_Idle_001.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Idle/0_Golem_Idle_002.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Idle/0_Golem_Idle_003.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Idle/0_Golem_Idle_004.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Idle/0_Golem_Idle_005.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Idle/0_Golem_Idle_006.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Idle/0_Golem_Idle_007.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Idle/0_Golem_Idle_008.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Idle/0_Golem_Idle_009.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Idle/0_Golem_Idle_010.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Idle/0_Golem_Idle_011.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Idle/0_Golem_Idle_012.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Idle/0_Golem_Idle_013.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Idle/0_Golem_Idle_014.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Idle/0_Golem_Idle_015.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Idle/0_Golem_Idle_016.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Idle/0_Golem_Idle_017.png"
        ],
        "attack": [
            "Enemy/Golem_1/PNG/PNG Sequences/Slashing/0_Golem_Slashing_000.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Slashing/0_Golem_Slashing_001.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Slashing/0_Golem_Slashing_002.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Slashing/0_Golem_Slashing_003.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Slashing/0_Golem_Slashing_004.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Slashing/0_Golem_Slashing_005.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Slashing/0_Golem_Slashing_006.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Slashing/0_Golem_Slashing_007.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Slashing/0_Golem_Slashing_008.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Slashing/0_Golem_Slashing_009.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Slashing/0_Golem_Slashing_010.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Slashing/0_Golem_Slashing_011.png"
        ],
        "hurt": [
            "Enemy/Golem_1/PNG/PNG Sequences/Hurt/0_Golem_Hurt_000.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Hurt/0_Golem_Hurt_001.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Hurt/0_Golem_Hurt_002.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Hurt/0_Golem_Hurt_003.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Hurt/0_Golem_Hurt_004.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Hurt/0_Golem_Hurt_005.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Hurt/0_Golem_Hurt_006.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Hurt/0_Golem_Hurt_007.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Hurt/0_Golem_Hurt_008.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Hurt/0_Golem_Hurt_009.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Hurt/0_Golem_Hurt_010.png",
            "Enemy/Golem_1/PNG/PNG Sequences/Hurt/0_Golem_Hurt_011.png"

        ]
    }



    player1 = player(
        x=100,
        y=280,
        animations=player_animations,
        damage=20,
        health=100,
        anim_speed=5,
        scale=3
)
    enemy1 = enemy(
        x=500,
        y=280,
        animations=enemy_animations,
        damage=10,
        health=100,
        anim_speed=2,
        scale=0.5
    )
    FPS = 60
    run = True
    clock = pygame.time.Clock()
    turn = "player"
    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                break
            if turn == "player" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    player1.set_animation("attack")
                    turn = "anim_wait"
        player1.update()
        enemy1.update()

        if turn == "anim_wait" and player1.current_animation == "attack" and player1.current_frame == len(player1.frames) -1:
            player1.attack(enemy1)
            enemy1.set_animation("hurt")
            player1.set_animation("idle")
            turn = "enemy"

            # Enemy turn
        if turn == "enemy":
            enemy1.set_animation("attack")
            turn = "enemy_anim"

        if turn == "enemy_anim" and enemy1.current_animation == "attack" and enemy1.current_frame == len(enemy1.frames) - 1:
            enemy1.attack(player1)
            player1.set_animation("hurt")
            enemy1.set_animation("idle")
            turn = "player_hurt"
        
        if turn == "player_hurt" and player1.current_animation == "hurt" and player1.current_frame == len(player1.frames)-1:
            player1.set_animation("idle")
            turn = "player"


        draw_bg()
        
        player1.update()
        player1.draw(WINDOW)
        player1.draw_health_bar(WINDOW)

        enemy1.update()
        enemy1.draw(WINDOW)
        enemy1.draw_health_bar(WINDOW)

        pygame.display.update()

        if player1.health <= 0:
            victory_text = font.render("Enemy Wins!", True, (255, 0, 0))
            draw_bg()
            player1.draw(WINDOW)
            enemy1.draw(WINDOW)
            WINDOW.blit(victory_text, (WIDTH//2 - victory_text.get_width()//2,
                                        HEIGHT//2 - victory_text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(2000)
            run = False
        elif enemy1.health <= 0:
            victory_text = font.render("You Win!", True, (0, 255, 0))
            draw_bg()
            player1.draw(WINDOW)
            enemy1.draw(WINDOW)
            WINDOW.blit(victory_text, (WIDTH//2 - victory_text.get_width()//2,
                                        HEIGHT//2 - victory_text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(2000)
            run = False


        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
