from data_pb2 import *
from data_pb2_grpc import *
from bot import *
from tkinter.font import Font
from tkinter import *
import tkinter as tk
import pygame
import random
import sys


# Displays an error message to the user
def show_prompt(msg, btnText="Ok"):
    prompt_win = tk.Tk()
    prompt_win.title("Prompt")
    prompt_win.configure(bg="#2d2d2d")

    # Fonts
    font = Font(family="Helvetica", size=14)

    # Message
    error_message = Label(prompt_win, text=msg, pady=30, padx=30, font=font, fg="white", bg="#2d2d2d")
    error_message.pack()

    start_game_button = Button(prompt_win, text=btnText, command=prompt_win.destroy, font=font, pady=5)
    start_game_button.pack()

    margin_label = Label(prompt_win, text="", pady=0.1, fg="white", bg="#2d2d2d")
    margin_label.pack()

    prompt_win.mainloop()


try:
    address = sys.argv[1]
except IndexError:
    print("Need to give ip and port, ip:port")
    sys.exit()

try:
    channel = grpc.insecure_channel(address)
    service = SnakeStub(channel)
    size = service.get_size(No_parameter())
except (grpc.RpcError, RuntimeError):
    show_prompt("Error:\nCould not connect to server")
    sys.exit()

# Pygame attributes
WIDTH, HEIGHT = size.x, size.y
WIN_SCALE = 20
pygame.init()
pygame.font.init()
pygame.display.set_caption("PySnake")
WIN = pygame.display.set_mode((WIDTH * WIN_SCALE + 150, HEIGHT * WIN_SCALE))
font_score_1 = pygame.font.SysFont("Helvetica", 40)
font_score_1.set_underline(True)
font_score_2 = pygame.font.SysFont("Helvetica", 30)
font_score_2.set_underline(True)
font_score_3 = pygame.font.SysFont("Helvetica", 20)
BLACK = (26, 26, 26)
GRAY = (38, 38, 38)

gameover_prompt = False

# Snake attributes
snake_name = ""
velX, velY = 1, 0
snake_body = []
posX, posY = -1, -1
game_over = False
FPS = 12
run = True
bot = 0

# Assets
player = Player()
fruits = []
snakes = []


# Prevents generating a color that blends in with the background
def rand_light_color():
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    while r < 100 and g < 100 and b < 100:
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    return r, g, b


# Draws the background in a chess like pattern
def draw_background():
    WIN.fill(GRAY, (0, 0, WIDTH * WIN_SCALE, WIN.get_height()))

    for x in range(WIDTH):
        for y in range(HEIGHT):
            offset = 0
            if y % 2 == 0:
                offset = 1

            if (x + offset) % 2 == 0:
                pygame.draw.rect(WIN, BLACK, (x * WIN_SCALE, y * WIN_SCALE, WIN_SCALE, WIN_SCALE))


# Draws all the snakes
def draw_snakes():
    for snake in snakes:
        for pos in snake["position"]:
            pygame.draw.rect(WIN, snake["color"], (pos[0] * WIN_SCALE, pos[1] * WIN_SCALE, WIN_SCALE, WIN_SCALE))


# Draws the fruit coordinates from the server
def draw_fruit():
    for pos in fruits:
        pygame.draw.rect(WIN, (255, 0, 0), (pos[0] * WIN_SCALE, pos[1] * WIN_SCALE, WIN_SCALE, WIN_SCALE))


# Draws the scores and player names
def draw_score(score):  # Has parameter for score input so right score will show on start up
    # Has to draw all the white to remove previous text
    pygame.draw.rect(WIN, (235, 235, 235), (WIDTH * WIN_SCALE, 5, 145, HEIGHT * WIN_SCALE - 10))
    text_surface = font_score_1.render("Scores:", True, BLACK)
    WIN.blit(text_surface, (WIDTH * WIN_SCALE + 10, 10))

    text_array = [  # Predetermined text
        ("", font_score_3, 55),
        ("Your score: {}".format(score), font_score_3, 30),
        ("Players:", font_score_2, 42)
    ]
    for snake in snakes:
        text_array.append(("{}: {}".format(snake["name"], len(snake["position"]) - 4), font_score_3, 20))

    pixel_from_top = 0
    # Draws all the text on the right hand side
    for i in range(1, len(text_array)):
        if text_array[i][1] == font_score_3:
            text = font_score_3.render(text_array[i][0], True, BLACK)
        else:
            text = font_score_2.render(text_array[i][0], True, BLACK)
        pixel_from_top += text_array[i - 1][2]
        WIN.blit(text, (WIDTH * WIN_SCALE + 10, pixel_from_top))


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
    global game_over

    fruits = []
    snakes = []
    stopped = True
    get_player_info()
    # Gets info from server and parses it
    request = service.get_information(player)
    for r in request:
        # Checks if fruit exist
        if r.fruit.x != -1:
            fruits.append((r.fruit.x, r.fruit.y))
        # Checks if player exist
        if r.player.game_over is False:
            if r.player.name == player.name:
                stopped = False
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

    if stopped:
        game_over = True


# Checks if player triggers a hit event
def hit_event():
    global fruits
    global snakes
    global game_over
    global velX, velY
    global posX, posY

    # Boolean statements for game_over if test below
    hit_self = snake_body[len(snake_body) - 1] in snake_body[:-1]
    hit_border = posX > WIDTH - 1 or posX < 0 or posY > HEIGHT - 1 or posY < 0

    hit_snakes = False

    # Checks if snake is in another snake but not in its own snake
    for snake in snakes:
        if snake_body[len(snake_body) - 1] in snake["position"] and snake_name != snake["name"]:
            hit_snakes = True

    # By hitting itself, other snakes or the wall the game will be over.
    if hit_self or hit_border or hit_snakes:
        game_over = True

    # At fruit pick up, push new pos, don't remove last. Then removes the fruit from array and sends info to server
    elif snake_body[len(snake_body) - 1] in fruits:
        fruit = Position()
        fruit.x = posX - velX
        fruit.y = posY - velY
        if service.send_fruit(fruit).confirmation:
            fruits.remove((posX - velX, posY - velY))
            snake_body.append((posX, posY))

    else:
        # On movement push new pos into snake body, remove last
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
    # Drawing background
    draw_background()
    # Gets info from server before drawing assets
    get_server_info()
    # Drawing assets
    draw_fruit()
    if not game_over and bot:
        move_bot_snake(path)
    elif not game_over:
        move_snake()

    draw_snakes()
    draw_score(len(snake_body) - 4)

    pygame.display.update()


# Displays a menu with high scores and a start game button
def show_menu():
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
    title_label = tk.Label(window, text="PySnake 🐍", font=title_font, fg="white", bg="#2d2d2d", padx=30, pady=20)
    title_label.pack()

    # Name field:
    name_label = Label(window, text="Name: ", font=font, fg="white", bg="#2d2d2d", )
    name_label.pack()

    name_input = Entry(window, font=font)
    name_input.pack()

    margin_label = Label(window, text="", pady=0.1, fg="white", bg="#2d2d2d")
    margin_label.pack()

    ib = IntVar()
    bot_checkbox = Checkbutton(window, text="Run as bot", variable=ib, font=font, indicatoron=True)
    bot_checkbox.pack()

    margin_label = Label(window, text="", pady=0.1, fg="white", bg="#2d2d2d")
    margin_label.pack()

    # Start game button:
    def start():
        global snake_name
        global bot

        bot = ib.get()
        snake_name = name_input.get()
        window.destroy()

    start_game_button = Button(window, text="Start game", command=start, font=font, pady=5)
    start_game_button.pack()

    margin_label = Label(window, text="", pady=0.1, fg="white", bg="#2d2d2d")
    margin_label.pack()

    # How to play:
    def howto():
        msg = """
            Collect "fruit" or red pixels to achieve a greater score.
            Avoid dying by evading other players, yourself and the border.
            The snake can not move backwards
            The game is over once everybody has gotten a game over or the player decides to exit.

            Controls:
            There are two sets of controls that do the same thing

            W or Arrow Up: Move the snake upwards

            A or Arrow Left: Move the snake to the left

            S or Arrow Down: Move the snake downwards

            D or Arrow Right: Move the snake to the right
        """

        show_prompt(msg)

    howto_button = Button(window, text="How to play", command=howto, font=font, pady=3)
    howto_button.pack()

    # High scores:
    score_text = "High scores: \n"
    leaderboard = service.get_leaderboard(No_parameter())
    for i in reversed(range(len(leaderboard.high_score))):
        score_text += "{}: {}\n".format(leaderboard.high_score[i].name, leaderboard.high_score[i].score)

    score_label = tk.Label(window, text=score_text, font=font, fg="white", bg="#2d2d2d", padx=60, pady=15)
    score_label.pack()

    # Made by text:
    made_text = "Made by:\n Nikola Dordevic, s341839\n Jørund Topp Løvlien, s341822"
    made_label = tk.Label(window, text=made_text, padx=60, pady=10, fg="white", bg="#2d2d2d", )
    made_label.pack()

    window.mainloop()


# Displays session score, and high scores when the match is over
def show_score():
    global snakes

    score_win = tk.Tk()
    score_win.title("PySnake")
    score_win.resizable(0, 0)
    score_win.configure(bg="#2d2d2d")

    font = Font(family="Helvetica", size=12)
    title_font = Font(family="Helvetica", size=24)

    # Title:
    title_label = tk.Label(score_win, text="PySnake 🐍", font=title_font, fg="white", bg="#2d2d2d", padx=30, pady=20)
    title_label.pack()

    # Session score:
    session_text = "Session score: {}".format(len(snake_body) - 4)
    session_label = tk.Label(score_win, text=session_text, font=font, padx=30, pady=10, fg="white", bg="#2d2d2d")
    session_label.pack()

    # High scores:
    score_text = "High scores: \n"
    leaderboard = service.get_leaderboard(No_parameter())
    for i in reversed(range(len(leaderboard.high_score))):
        score_text += "{}: {}\n".format(leaderboard.high_score[i].name, leaderboard.high_score[i].score)

    score_label = tk.Label(score_win, text=score_text, font=font, padx=60, pady=5, fg="white", bg="#2d2d2d")
    score_label.pack()

    margin_label = Label(score_win, text="", pady=0.1, fg="white", bg="#2d2d2d")
    margin_label.pack()

    score_win.mainloop()


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


def main():
    global run
    global posX, posY
    global gameover_prompt

    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if game_over and not gameover_prompt:
            gameover_prompt = True
            show_prompt("GAME OVER", "Spectate")

        draw()


def bot_main():
    global run
    global fruits
    global posX, posY
    global velX, velY
    global snakes
    global WIDTH, HEIGHT

    clock = pygame.time.Clock()
    get_server_info()

    # Starting conditions
    client_info = {
        "run": run,
        "snake_body": snake_body,
        "velocity": (velX, velY),
        "fruits": fruits,
        "snakes": snakes,
        "dimensions": (WIDTH, HEIGHT)
    }

    path = find_path(closest_fruit(client_info), client_info)

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

        fruit = closest_fruit(client_info)
        if path[2:4] in snakes or len(path) == 1:  # LEN PATH JUST IMPLEMENTED UNTIL PATHING WITH NO RESULT FIXED
            path = find_path(fruit, client_info)

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw(path)


def start_snake():
    global posX, posY
    global velX
    global game_over
    global snake_name
    global FPS
    # Draws all the text
    draw_score(-1)
    # If game_over is false, it is the first time the player started this session
    # If game_over is true, it is not the first time
    if not game_over:
        if snake_name != "":
            player.name = snake_name  # Set player name to input name
        else:
            player.name = snake_name = "Guest"
        player.color.extend(rand_light_color())
        player.game_over = False
        player_request = service.send_player(player)  # Sends server info about a new player
        player.name = player_request.name  # If name is not unique, player will get new one
    else:
        # This way player keeps same name and color
        player_request = service.send_player(player)  # Sends server info that player wants to play again
        player.game_over = game_over = False  # Sets game_over to false for player
    # Gets empty tiles from server
    for pos in player_request.position:
        snake_body.append((pos.x, pos.y))
    # If closer to the right side it will start going towards the left instead
    if snake_body[0][0] > WIDTH / 2:
        velX = -1
    # Sets start position
    posX, posY = snake_body[-1][0] + velX, snake_body[-1][1] + velY

    if bot == 1:
        FPS = 20
        bot_main()
    else:
        main()

    pygame.quit()
    high_score = High_score()
    high_score.name = snake_name
    high_score.score = len(snake_body) - 4
    service.send_high_score(high_score)
    show_score()


if __name__ == "__main__":
    show_menu()
    start_snake()
