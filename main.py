import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()
    print("Starting Asteroids!")

    dt = 0
    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT // 2
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroid, updateable, drawable)
    AsteroidField.containers = (updateable,)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x, y)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)

        for obj in asteroid:
            if obj.check_collision(player):
                print("Collision detected! Game Over.")
                return

        screen.fill("#11111e")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000  # Amount of seconds between each loop.


if __name__ == "__main__":
    main()
