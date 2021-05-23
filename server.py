from concurrent import futures
from data_pb2 import *
from data_pb2_grpc import *
import grpc
import time
import threading
import random
import re
import json

width = 64
height = 36
players = []
leaderboard = []
fruits = []
running = True


class Snake(SnakeServicer):

    # Gets high score from a client
    def send_high_score(self, request, context):
        global leaderboard
        # Makes the gets the high_score message
        high_score = High_score()
        high_score.name = request.name
        high_score.score = request.score
        new_score = False
        score = request.score

        if len(leaderboard) == 0:  # Empty leaderboard
            leaderboard.append(high_score)
            new_score = True
        else:  # Loops through leaderboard in reverse order
            for i in reversed(range(len(leaderboard))):
                if score > leaderboard[i].score:  # Checks if high score is high enough
                    if len(leaderboard) == 5:  # Will remove smallest value if leaderboard is full
                        leaderboard.pop(0)
                    # Adds high score to right spot in leaderboard
                    leaderboard.insert(i, high_score)
                    new_score = True
                    break
                elif i == 0 and len(leaderboard) < 5:  # Checks if leaderboard is not full
                    leaderboard.insert(i, high_score)
                    new_score = True

        # If new high score, updates leaderboard and writes it to file
        if new_score:
            leaderboard_array = []
            for leader in leaderboard:
                leaderboard_player = {
                    "name": leader.name,
                    "score": leader.score
                }

                leaderboard_array.append(leaderboard_player)

            with open('leaderboard.json', 'w') as f:
                json.dump(leaderboard_array, f)

        return Confirmed(confirmation=True)

    # Gets information about eaten fruit from a client
    def send_fruit(self, request, context):
        global fruits
        fruits.remove(request)
        threading.Thread(target=make_fruits).start()
        return Confirmed(confirmation=True)

    # Gets information about new player
    def send_player(self, request, context):
        global players
        # If new player, not player that wants to play again
        player = Player()
        player.color.extend(request.color)
        if not request.game_over:
            game_over = request.game_over
            name = request.name
            same_name = 1
            for i in range(len(players)):  # Checks if name is same as other players
                if name == players[i].name:
                    temp_name = re.sub("[(][0-9]+[)]", "", name)
                    temp_name += "({})".format(same_name)  # Will add number to the end of name to make it unique
                    name = temp_name
                    same_name += 1
        else:
            name = request.name
            game_over = False

        player.name = name
        player.game_over = game_over
        # Creates empty array for snake position
        positions = [None] * 4
        all_tiles_empty = False
        # Checks if tiles are empty and will select new tiles if not empty
        while not all_tiles_empty:
            pos = Position()
            pos.x = random.randint(4, width - 4)
            pos.y = random.randint(4, height - 3)
            # Checks if head tile is empty
            while not empty_tile(pos):
                pos.x = random.randint(4, width - 4)
                pos.y = random.randint(4, height - 4)

            for i in range(len(positions)):
                temp_pos = Position()
                temp_pos.x = pos.x
                temp_pos.y = pos.y + (3 - i)
                # Places all tiles in array if they are empty
                if empty_tile(temp_pos):
                    positions[i] = temp_pos
                    if i == len(positions) - 1:
                        all_tiles_empty = True
                else:
                    break

        player.position.extend(positions)
        players.append(player)
        return player

    # Sends leaderboard to a client
    def get_leaderboard(self, request, context):
        return Leaderboard(high_score=leaderboard)

    # Sends size to a client
    def get_size(self, request, context):
        return Position(x=width, y=height)

    # Sends information about all fruits from clients
    def get_information(self, request, context):
        global players
        # Gets player information and replaces old info with new
        player = request
        for i in range(len(players)):  # Loops through all players to check if player is already in list
            if player.name == players[i].name:
                players[i] = player
                break

        length_fruits = len(fruits)
        length_players = len(players)

        if length_fruits >= length_players:
            for i in range(length_fruits):
                info = Information()
                if i < length_players:  # Sends info about player and fruit
                    info.player.name = players[i].name
                    info.player.color.extend(players[i].color)
                    info.player.game_over = players[i].game_over
                    info.player.position.extend(players[i].position)
                    info.fruit.x = fruits[i].x
                    info.fruit.y = fruits[i].y
                else:  # Sends info about a fruit if there are more fruits than players
                    info.fruit.x = fruits[i].x
                    info.fruit.y = fruits[i].y
                    info.player.game_over = True
                yield info
        else:
            for i in range(length_players):
                info = Information()
                if i < length_fruits:  # Sends info about player and fruit
                    info.player.name = players[i].name
                    info.player.color.extend(players[i].color)
                    info.player.game_over = players[i].game_over
                    info.player.position.extend(players[i].position)
                    info.fruit.x = fruits[i].x
                    info.fruit.y = fruits[i].y
                else:  # Sends info about player if more players than fruits
                    info.player.name = players[i].name
                    info.player.color.extend(players[i].color)
                    info.player.game_over = players[i].game_over
                    info.player.position.extend(players[i].position)
                    info.fruit.x = -1
                yield info


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
    global fruits
    # Generates fruits over time
    time.sleep(random.random() + random.randint(0, 2))
    pos = Position()
    pos.x = random.randint(1, width - 1)
    pos.y = random.randint(1, height - 1)

    # Ensures that fruit never spawn twice on the same tile or tile with snake on it
    while not empty_tile(pos):
        pos.x = random.randint(1, width - 1)
        pos.y = random.randint(1, height - 1)

    fruits.append(pos)


def make_fruits_startup(number_of_fruits):
    global fruits
    for i in range(number_of_fruits):
        make_fruits()


def remove_dead():
    global players

    while running:
        # Will remove dead players from array
        for player in players:
            if player.game_over:
                players.remove(player)
        # Saves a temporary player array to see if player has disconnected without dying
        # (If game freezes this will also count as dying)
        temp_players = players.copy()
        time.sleep(0.5)
        # Checks player positioning after half a second
        if len(temp_players) != 0:
            for p in players:
                for t_p in temp_players:
                    if p.name == t_p.name:  # Makes is so it dose not loop unnecessary
                        if p.position == t_p.position:
                            p.game_over = True
                        temp_players.remove(t_p)
                        continue


def start():
    global running
    # Reads inn leaderboard file and parses it to a High_score message
    with open('leaderboard.json') as f:
        try:
            leaderboard_array = json.load(f)
        except json.JSONDecodeError:
            leaderboard_array = []

    for player in leaderboard_array:
        high_score = High_score()
        high_score.name = player["name"]
        high_score.score = player["score"]
        leaderboard.append(high_score)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_SnakeServicer_to_server(Snake(), server)
    server.add_insecure_port("localhost:9999")
    server.start()
    print("Server has started")
    threading.Thread(target=make_fruits_startup, args=(6,)).start()
    threading.Thread(target=remove_dead).start()
    try:
        while running:
            time.sleep(5)
    except KeyboardInterrupt:
        print("KeyBoardInterrupt")
        running = False
        server.stop(0)


if __name__ == "__main__":
    start()
