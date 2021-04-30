import pygame

WIDTH, HEIGHT = 128, 75
WIN_SCALE = 8

WIN = pygame.display.set_mode((WIDTH * WIN_SCALE, HEIGHT * WIN_SCALE))
pygame.display.set_caption("PySnake")

# Colors
PEACH_ORANGE = (255, 201, 150)
SALMON = (255, 132, 116)
VICTORIA = (88, 61, 114)
STRIKEMASTER = (159, 95, 128)

def main():

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(VICTORIA)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()