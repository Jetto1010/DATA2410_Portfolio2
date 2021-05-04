from concurrent import futures
from data_pb2 import *
from data_pb2_grpc import *
import grpc
import time
import math
import threading
import random

width = 100
height = 100
players = []
leaderboard = []
fruits = []
running = True


class Snake(SnakeServicer):

    # Gets player information from that client
    def send_player(self, request, context):
        print("This sends player info to server")
        player = Player()
        player.name = request.name
        player.color.extend(request.color)
        player.game_over = request.game_over
        player.position.extend(request.position)
        players.append(request)
        return Confirmed(confirmation=True)

    # Gets high score from a client
    def send_high_score(self, request, context):
        global leaderboard
        # Makes the gets the high_score message
        high_score = High_score()
        high_score.name = request.name
        high_score.score = request.score
        new_score = False
        score = request.score

        # Logic behind leaderboard update
        if len(leaderboard) == 0:  # Empty leaderboard
            leaderboard.append(high_score)
            new_score = True
        else:  # Loops through leaderboard in reverse order
            for i in reversed(range(len(leaderboard))):
                if score > leaderboard[i].score:  # Checks if high score is high enough
                    if len(leaderboard) == 5:  # Will remove smallest value if leaderboard is full
                        leaderboard.pop(0)
                    # Adds high score to right spot in leaderboard
                    leaderboard = leaderboard[0:i + 1] + [high_score] + leaderboard[i + 1:]
                    new_score = True
                    break
                elif i == 0 and len(leaderboard) < 5:  # Checks if leaderboard is not full
                    leaderboard = leaderboard[0:i] + [high_score] + leaderboard[i:]
                    new_score = True
                    break

        # If new high score, updates leaderboard and writes it to file
        if new_score:
            leaderboard_string = ""
            for leader in leaderboard:
                leaderboard_string += format(leader.name) + ","
                leaderboard_string += format(leader.score) + "\n"

            file = open("leaderboard.txt", "w")
            file.write(leaderboard_string)

        return Confirmed(confirmation=True)

    # Gets information about eaten fruit from a client
    def send_fruit(self, request, context):
        print("This sends eaten fruit to server")
        fruits.remove(request)
        return Confirmed(confirmation=True)

    # Sends information about all players to a client
    def get_players(self, request, context):
        print("This sends players to clients")
        for p in players:
            yield p

    # Sends leaderboard to a client
    def get_leaderboard(self, request, context):
        print("This sends leaderboard to clients")
        return Leaderboard(high_score=leaderboard)

    # Sends size to a client
    def get_size(self, request, context):
        print("This sends size to clients")
        return Position(x=width, y=height)

    # Sends information about all fruits from clients
    def get_fruits(self, request, context):
        print("This sends fruits to player")
        for f in fruits:
            yield f


def empty_tile(pos):
    # Checks if new fruit is in list of fruits
    if pos in fruits:
        return False

    # Checks if in list of player positions
    for p in players:
        if pos in p.position:
            return False

    return True


def make_fruits():
    while True:
        # Cosine function where the return gets closer to 0 when the amount of fruits approaches 6. 0% of spawning
        # more than 6 fruits
        probability = math.cos(len(fruits) / 3.5)
        if probability > random.random():
            time.sleep(random.randint(1, 3))

            pos = Position()
            pos.x = random.randint(0, width)
            pos.y = random.randint(0, height)

            # Ensures that fruit never spawn twice on the same tile or tile with snake on it
            while not empty_tile(pos):
                pos.x = random.randint(0, width)
                pos.y = random.randint(0, height)

            fruits.append(pos)
            print("New fruit at: {}".format(pos))


def start():
    global running
    # Reads inn leaderboard file and parses it to a High_score message
    file = open("leaderboard.txt", "r")
    leaderboard_str = file.read().split("\n")
    for i in leaderboard_str:
        if i == "":
            break
        split = i.split(",")
        high_score = High_score()
        high_score.name = split[0]
        high_score.score = int(split[1])
        leaderboard.append(high_score)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    add_SnakeServicer_to_server(Snake(), server)
    server.add_insecure_port("localhost:9999")
    server.start()
    make_fruits()
    try:
        while running:
            print("server on: threads {}".format(threading.activeCount()))
            time.sleep(5)
    except KeyboardInterrupt:
        print("KeyBoardInterrupt")
        running = False
        server.stop(0)


if __name__ == "__main__":
    start()
