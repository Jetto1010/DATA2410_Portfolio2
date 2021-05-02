import pygame
import time
import random
import threading
from math import *
import tkinter as tk
from tkinter.font import Font
from tkinter import *
import sys

WIDTH, HEIGHT = 64, 36
WIN_SCALE = 20
FPS = 20
run = True
WIN = pygame.display.set_mode((WIDTH * WIN_SCALE, HEIGHT * WIN_SCALE))
pygame.display.set_caption("PySnake")

screen = pygame.Surface((WIDTH, HEIGHT))

# Colors
SNAKE_COLOR = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
TESTCOLOR_OTHERSNAKES = (255, 132, 116)
BLACK = (26, 26, 26)
GRAY = (38, 38, 38)

# Snake attributes
name = "Guest"
velX, velY = 1, 0
randX = random.randint(2, WIDTH - 10)
randY = random.randint(2, HEIGHT - 4)
snake_body = [(randX, randY + 3), (randX, randY + 2), (randX, randY + 1), (randX, randY)]
posX, posY = snake_body[len(snake_body) - 1][0] + velX, snake_body[len(snake_body) - 1][1] + velY
game_over = False

snake = {
    "name": name,
    "position": snake_body,
    "color": SNAKE_COLOR,
    "game_over": game_over
}

print(snake)

# Test data of fruit. This function is supposed to run on the server
def create_fruit():
    global fruits

    while run:
        # Cosine function where the return gets closer to 0 when the amount of fruits approaches 6. 0% of spawning more than 6 fruits
        probability = cos(len(fruits) / 3.5)
        if probability > random.random():
            time.sleep(random.randint(1, 3))

            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)

            while (x,y) in fruits:
                x = random.randint(0, WIDTH)
                y = random.randint(0, HEIGHT)

            fruits.append((x,y))

# Assets
fruits = []
snakes = [
    {
        "name": "jetto",
        "position": [(30, 4), (30, 3), (30, 2), (30, 1)],
        "color": "random color",
        "game_over": False
    },

    {
        "name": "nikko",
        "position": [(40, 4), (40, 3), (40, 2), (40, 1)],
        "color": "random color",
        "game_over": False
    }
]

# Displays 5 highest scores ever gotten in the game
highscores = [
    {
        "name": "nikko",
        "score": 43
    },
    {
        "name": "jetto",
        "score": -3
    }
]

def draw_other_snakes():
    global snakes
    
    for snake in snakes:
        for pos in snake["position"]:
            screen.set_at(pos, TESTCOLOR_OTHERSNAKES)

# Draws the fruit coordinats from the server
def draw_fruit():
    for pos in fruits:
        screen.set_at(pos, "red")
        
def move_snake():
    global fruits
    global snakes
    global game_over
    global velX
    global velY
    global posX
    global posY

    # Boolean statements for game_over if test below
    hit_self = snake_body[len(snake_body) - 1] in snake_body[:-1]
    hit_border = posX > WIDTH - 1 or posX < 0 or posY > HEIGHT - 1 or posY < 0
    
    hit_snakes = False

    for snake in snakes:
        if snake_body[len(snake_body) - 1] in snake["position"]:
            hit_snakes = True

    # Ved å treffe seg selv, eller andre slanger skal spillet være over, men fortsatt være i bildet.
    # Ved å treffe kanten skal spillet være over, men slangen skal fortsatt være i bildet, siden andre spillere skal ikke kunne tråkke over kroppen
    if hit_self or hit_border or hit_snakes:
        game_over = True

    # Ved plukke opp frukt, push ny pos, ikke pop bakerste. Så fjern fruiten fra fruit arrayet
    elif snake_body[len(snake_body) - 1] in fruits:
        print(fruits)
        print(posX - velX, posY - velY)
        print(fruits)
    
        fruits.remove((posX - velX, posY - velY))
        snake_body.append((posX, posY))

    else:
        # Ved bevegelse push ny pos i snake body, pop bakerste
        snake_body.pop(0)
        snake_body.append((posX, posY))

    # Movement
    key = pygame.key.get_pressed()
    if (key[pygame.K_w] or key[pygame.K_UP]) and velY != 1:  # Up
        velY = -1
        velX = 0
    elif (key[pygame.K_a] or key[pygame.K_LEFT]) and velX != 1:  # Left
        velY = 0
        velX = -1
    elif (key[pygame.K_s] or key[pygame.K_DOWN]) and velY != -1:  # Down
        velY = 1
        velX = 0
    elif (key[pygame.K_d] or key[pygame.K_RIGHT]) and velX != -1:  # Right
        velY = 0
        velX = 1    

    posX += velX
    posY += velY

def draw_snake():
    # Draws every "pixel" body of the snake
    for pos in snake_body:
        screen.set_at(pos, SNAKE_COLOR)

# Draws the background and assets onto the window
def draw():
    global game_over

    # Drawing background
    screen.fill(BLACK)

    for x in range(WIDTH):
        for y in range(HEIGHT):
            offset = 0
            if y % 2 == 0:
                offset = 1

            if (x + offset) % 2 == 0:
                screen.set_at((x, y), GRAY)

    # Drawing assets
    draw_fruit()
    if not game_over:
        move_snake()
    draw_snake()
    draw_other_snakes()

    WIN.blit(pygame.transform.scale(screen, WIN.get_rect().size), (0, 0))
    pygame.display.update()

# Displays a menu with highscores and a start game button 
def show_menu():
    global highscores

    window = tk.Tk()
    window.title("PySnake")
    window.resizable(0, 0)

    # Exits program if X is pressed
    window.protocol("WM_DELETE_WINDOW", sys.exit)

    # Fonts
    font = Font(family="Helvetica", size=12)
    titleFont = Font(family="Helvetica", size=24)

    # Title:
    title_label = tk.Label(text="PySnake", font=titleFont, padx=30, pady=20)
    title_label.pack()

    # Name field:
    name_label = Label(text="Name: ", font=font)
    name_input = Entry(font=font)
    name_label.pack()
    name_input.pack()

    # Start game button:
    def start():
        global name
        name = name_input.get()
        window.destroy()

    startGame_button = Button(text="Start game", command=start ,font=font , pady=5)
    startGame_button.pack()

    # Highscores: 
    score_text = "Highscores: \n"
    for score in highscores:
        score_text += "{}: {}\n".format(score["name"], score["score"])

    score_label = tk.Label(text=score_text, font=font, padx=60, pady=15)
    score_label.pack()

    # Made by text:
    made_text = "Made by:\n Nikola Dordevic, s348139\n Jørund Topp Løvlien, s341822"
    made_label = tk.Label(text=made_text, padx=60, pady=10)
    made_label.pack()

    window.mainloop()

# Displays session score, and highscores when the match is over
def show_score():
    global snakes
    global highscores

    window = tk.Tk()
    window.title("PySnake")
    window.resizable(0, 0)

    font = Font(family="Helvetica", size=12)

    # Session score:
    session_text = "Session scores: \n"
    for snake in snakes:
       session_text += "{}: {}\n".format(snake["name"], len(snake["position"]) - 4)
    session_label = tk.Label(text=session_text, font=font, padx=30, pady=10)
    session_label.pack()

    # Highscores:
    score_text = "Highscores: \n"
    for score in highscores:
        score_text += "{}: {}\n".format(score["name"], score["score"])

    score_label = tk.Label(text=score_text, font=font, padx=60, pady=5)
    score_label.pack()
    
    window.mainloop()

def main():
    global run

    show_menu()
    

    clock = pygame.time.Clock()
    threading.Thread(target=create_fruit).start()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()

    pygame.quit()
    show_score()



if __name__ == "__main__":
    main()
