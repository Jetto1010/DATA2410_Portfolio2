from data_pb2 import *
from data_pb2_grpc import *
from bot import *
from tkinter.font import Font
from tkinter import *
import tkinter as tk
import pygame
import random
import sys

pygame.display.set_caption("PySnake")
channel = grpc.insecure_channel("localhost:9999")
service = SnakeStub(channel)
size = service.get_size(No_parameter())
WIDTH = size.x
HEIGHT = size.y
WIN_SCALE = 20
FPS = 15
run = True
WIN = pygame.display.set_mode((WIDTH * WIN_SCALE, HEIGHT * WIN_SCALE))


screen = pygame.Surface((WIDTH, HEIGHT))


# Colors

# Prevents generating a color that blends in with the background
def rand_light_color():
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    while r < 100 and g < 100 and b < 100:
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    return r, g, b


SNAKE_COLOR = rand_light_color()
TESTCOLOR_OTHERSNAKES = (255, 132, 116)
BLACK = (26, 26, 26)
GRAY = (38, 38, 38)

# Snake attributes
name = "Guest"
velX, velY = 1, 0
randX = random.randint(2, WIDTH - 10)
randY = random.randint(2, HEIGHT - 4)
snake_body = [(randX, randY + 3), (randX, randY + 2), (randX, randY + 1), (randX, randY)]
posX, posY = snake_body[-1][0] + velX, snake_body[-1][1] + velY
game_over = False

player = Player()
player.name = name
player.color.extend(rand_light_color())

# Assets
fruits = []
leaderboard = Leaderboard()
snakes = []


def draw_other_snakes():
    for snake in snakes:
        for pos in snake["position"]:
            screen.set_at(pos, TESTCOLOR_OTHERSNAKES)


# Updates information about player
def get_player_info():
    player.game_over = game_over
    positions = []
    for pos in snake_body:
        p = Position()
        p.x = pos[0]
        p.y = pos[1]
        positions.append(p)
    del player.position[:]
    player.position.extend(positions)
    return


def get_server_info():
    global fruits
    global snakes

    fruits = []
    snakes = []
    get_player_info()
    request = service.get_information(player)
    for r in request:
        if r.fruit.x != -1:
            fruits.append((r.fruit.x, r.fruit.y))
        if r.player.game_over is False:
            positions = []
            for pos in r.player.position:
                positions.append((pos.x, pos.y))
            rgb = []
            for color in r.player.color:
                rgb.append(color)

            snake = {
                "name": r.player.name,
                "position": positions,
                "color": rgb,
                "game_over": game_over
            }
            snakes.append(snake)


# Draws the fruit coordinates from the server
def draw_fruit():
    for pos in fruits:
        screen.set_at(pos, "red")


# Checks if player triggers a hit event
def hit_event():
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

    # for snake in snakes:
    # if snake_body[len(snake_body) - 1] in snake["position"] and not snake_body[len(snake_body) - 1] in snake_body[:-1]:
    #     hit_snakes = True

    # Ved å treffe seg selv, ecller andre slanger skal spillet være over, men fortsatt være i bildet. Ved å treffe
    # kanten skal spillet være over, men slangen skal fortsatt være i bildet, siden andre spillere skal ikke kunne
    # tråkke over kroppen
    if hit_self or hit_border or hit_snakes:
        game_over = True

    # Ved plukke opp frukt, push ny pos, ikke pop bakerste. Så fjern fruiten fra fruit arrayet
    elif snake_body[len(snake_body) - 1] in fruits:
        fruit = Position()
        fruit.x = posX - velX
        fruit.y = posY - velY
        if service.send_fruit(fruit).confirmation:
            fruits.remove((posX - velX, posY - velY))
            snake_body.append((posX, posY))

    else:
        # Ved bevegelse push ny pos i snake body, pop bakerste
        snake_body.pop(0)
        snake_body.append((posX, posY))


def move_snake():
    global velX
    global velY
    global posX
    global posY

    hit_event()

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


# Draws the background and assets onto the window
def draw(path=None):
    if path is None:
        path = []

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

    # Gets info from server before drawing assets

    get_server_info()
    # Drawing assets
    draw_fruit()
    if not game_over and bot:
        move_bot_snake(path)
    elif not game_over:
        move_snake()

    if bot:
        draw_path(path)
    draw_other_snakes()
    if bot:
        draw_path(path)

    WIN.blit(pygame.transform.scale(screen, WIN.get_rect().size), (0, 0))
    pygame.display.update()


# Displays a menu with high scores and a start game button
def show_menu():
    global leaderboard

    window = tk.Tk()
    window.title("PySnake")
    window.resizable(0, 0)
    window.configure(bg="#2d2d2d")

    # Exits program if X is pressed
    window.protocol("WM_DELETE_WINDOW", sys.exit)

    # Fonts
    font = Font(family="Helvetica", size=12)
    title_font = Font(family="Helvetica", size=24)

    # Title:
    title_label = tk.Label(text="PySnake 🐍", font=title_font, fg="white", bg="#2d2d2d", padx=30, pady=20)
    title_label.pack()

    # Name field:
    name_label = Label(text="Name: ", font=font, fg="white", bg="#2d2d2d", )
    name_label.pack()
    name_input = Entry(font=font)
    name_input.pack()
    margin_label = Label(text="", pady=0.1, fg="white", bg="#2d2d2d", )
    margin_label.pack()

    # Start game button:
    def start():
        global name
        name = name_input.get()
        window.destroy()

    start_game_button = Button(text="Start game", command=start, font=font, pady=5)
    start_game_button.pack()

    # High scores:
    score_text = "High scores: \n"
    leaderboard = service.get_leaderboard(No_parameter())
    for score in leaderboard.high_score:
        score_text += "{}: {}\n".format(score.name, score.score)

    score_label = tk.Label(text=score_text, font=font, fg="white", bg="#2d2d2d", padx=60, pady=15)
    score_label.pack()

    # Made by text:
    made_text = "Made by:\n Nikola Dordevic, s341839\n Jørund Topp Løvlien, s341822"
    made_label = tk.Label(text=made_text, padx=60, pady=10, fg="white", bg="#2d2d2d", )
    made_label.pack()

    window.mainloop()


# Displays session score, and high scores when the match is over
def show_score():
    global snakes
    global leaderboard

    window = tk.Tk()
    window.title("PySnake")
    window.resizable(0, 0)
    window.configure(bg="#2d2d2d")

    font = Font(family="Helvetica", size=12)
    title_font = Font(family="Helvetica", size=24)

    # Title:
    title_label = tk.Label(text="PySnake 🐍", font=title_font, fg="white", bg="#2d2d2d", padx=30, pady=20)
    title_label.pack()

    # Session score:
    session_text = "Session scores: \n"
    for snake in snakes:
        session_text += "{}: {}\n".format(snake["name"], len(snake["position"]) - 4)
    session_label = tk.Label(text=session_text, font=font, padx=30, pady=10, fg="white", bg="#2d2d2d")
    session_label.pack()

    # High scores:
    score_text = "High scores: \n"
    for score in leaderboard.high_score:
        score_text += "{}: {}\n".format(score.name, score.score)

    score_label = tk.Label(text=score_text, font=font, padx=60, pady=5, fg="white", bg="#2d2d2d")
    score_label.pack()

    window.mainloop()


def main():
    global run

    show_menu()

    clock = pygame.time.Clock()
    get_player_info()
    player_request = service.send_player(player)  # Sends server info about a new player
    player.name = player_request.name  # If name is not unique, player will get new one
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()

    pygame.quit()
    show_score()


def move_bot_snake(path):
    global velX, velY, posX, posY

    hit_event()

    try:
        velX = path[1][0] - posX
        velY = path[1][1] - posY

        path.pop(0)
    except IndexError:
        pass

    posX += velX
    posY += velY


def draw_path(path):
    for p in path:
        screen.set_at(p, (255, 215, 0))


def bot_main():
    global run
    global fruits

    show_menu()
    clock = pygame.time.Clock()

    # Starting conditions
    client_info = {
        "run": run,
        "snake_body": snake_body,
        "velocity": (velX, velY),
        "fruits": fruits,
        "snakes": snakes,
        "dimensions": (WIDTH, HEIGHT)
    }

    get_player_info()
    player_request = service.send_player(player)  # Sends server info about a new player
    player.name = player_request.name  # If name is not unique, player will get new one
    get_server_info()
    fruit = fruits[0]
    path = find_path(fruit, client_info)

    while run:
        clock.tick(FPS)
        client_info = {
            "run": run,
            "snake_body": snake_body,
            "velocity": (velX, velY),
            "fruits": fruits,
            "snakes": snakes,
            "dimensions": (WIDTH, HEIGHT)
        }

        fruit = closest_fruit(fruit, client_info)
        if path[2:4] in snakes or len(path) == 1:  # LEN PATH JUST IMPLEMENTED UNTIL PATHING WITH NO RESULT FIXED
            path = find_path(fruit, client_info)

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw(path)

    pygame.quit()
    show_score()


bot = False

if __name__ == "__main__":
    if bot:
        bot_main()
    else:
        main()
