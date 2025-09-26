import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot


def main():
    pygame.init()
    print("Starting Asteroids!")

    dt = 0
    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT // 2
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = (updateable,)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x, y)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Collision detected! Game Over.")
                return

            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.kill()

        screen.fill("#11111e")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000  # Amount of seconds between each loop.


if __name__ == "__main__":
    main()
