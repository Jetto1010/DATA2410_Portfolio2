import pygame

WIDTH, HEIGHT = 64, 36
WIN_SCALE = 20
FPS = 1
WIN = pygame.display.set_mode((WIDTH * WIN_SCALE, HEIGHT * WIN_SCALE))
pygame.display.set_caption("PySnake")

screen = pygame.Surface((WIDTH, HEIGHT))

# Colors
PEACH_ORANGE = (255, 201, 150)
SALMON = (255, 132, 116)
VICTORIA = (88, 61, 114)
TRENDY_PINK = (114, 87, 140)

# Snake attributes
velX, velY = 1, 0
posX, posY = 1, 1
snake_body = [(1,4), (1,3), (1,2), (1,1)]

# Obstacles
fruits = []

def drawSnake():
    print(snake_body)
    global fruits
    global velX
    global velY
    global posX
    global posY

    
    
    key = pygame.key.get_pressed()
    if (key[pygame.K_w] or key[pygame.K_UP]) and velY != 1: # Up
        velY = -1
        velX = 0
    elif (key[pygame.K_a] or key[pygame.K_LEFT]) and velX != 1: # Left
        velY = 0
        velX = -1
    elif (key[pygame.K_s] or key[pygame.K_DOWN]) and velY != -1: # Down
        velY = 1
        velX = 0
    elif (key[pygame.K_d] or key[pygame.K_RIGHT]) and velX != -1: # Right
        velY = 0
        velX = 1

    
    # Ved plukke opp frukt, push ny pos, ikke pop bakerste. Så fjern fruiten fra fruit arrayet
    if snake_body[len(snake_body) - 1] in fruits:
        return
    else:
        snake_body.pop(0)
        snake_body.append((posX, posY))
    # Ved bevegelse push ny pos i snake body, pop bakerste

    
    posX += velX
    posY += velY

    for pos in snake_body:
        screen.set_at(pos, PEACH_ORANGE)
    

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