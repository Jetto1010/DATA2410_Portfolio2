import pygame

WIDTH, HEIGHT = 64, 36
WIN_SCALE = 20
FPS = 20
WIN = pygame.display.set_mode((WIDTH * WIN_SCALE, HEIGHT * WIN_SCALE))
pygame.display.set_caption("PySnake")

screen = pygame.Surface((WIDTH, HEIGHT))

# Colors
PEACH_ORANGE = (255, 201, 150)
SALMON = (255, 132, 116)
VICTORIA = (88, 61, 114)
TRENDY_PINK = (114, 87, 140)

# Snake attributes
velocity = 1
posX = 1
posY = 1

def drawSnake():
    global posX
    global posY

    key = pygame.key.get_pressed()
    if key[pygame.K_w] or key[pygame.K_UP]:
        posY = posY + velocity

    screen.set_at((posX, posY), PEACH_ORANGE)

def draw():
    # Background
        screen.fill(VICTORIA)
        
        for x in range(WIDTH):
            for y in range(HEIGHT):
                offset = 0
                if y%2 == 0:
                    offset = 1

                if (x + offset)%2 == 0:
                    screen.set_at((x, y), TRENDY_PINK)

        drawSnake()

        WIN.blit(pygame.transform.scale(screen, WIN.get_rect().size), (0, 0))
        pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()

    pygame.quit()

if __name__ == "__main__":
    main()