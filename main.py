import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Groups
    update_group = pygame.sprite.Group()
    draw_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (update_group, draw_group)
    Asteroid.containers = (update_group, draw_group, asteroid_group)
    AsteroidField.containers = (update_group)
    Shot.containers = (update_group, draw_group, shot_group)

    # Objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        update_group.update(dt)

        for asteroid in asteroid_group:
            if player.collide(asteroid):
                print("Game over!")
                exit()

        for drawable in draw_group:
            drawable.draw(screen)

        # Flip must happen last
        dt = clock.tick(60) / 1000.0
        pygame.display.flip()

if __name__ == "__main__":
    main()