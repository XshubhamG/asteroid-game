import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()
    print("Starting Asteroids!")

    dt = 0
    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT // 2
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000  # Amount of seconds between each loop.
        screen.fill("#11111e")

        player.update(dt)
        player.draw(screen)

        # print(f"dt: {dt}")
        pygame.display.flip()


if __name__ == "__main__":
    main()
