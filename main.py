import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    pygame.init()
    print("Starting Asteroids!")

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        dt = clock.tick(60) / 1000  # Amount of seconds between each loop.
        # print(f"dt: {dt}")
        pygame.display.flip()


if __name__ == "__main__":
    main()
