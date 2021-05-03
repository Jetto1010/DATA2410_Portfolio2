from concurrent import futures
from data_pb2 import *
from data_pb2_grpc import *
import grpc
import time
import threading

players = []
leaderboard = []
fruits = []


class Snake(SnakeServicer):

    def send_player(self, request, context):
        print("This sends player to server")
        player = Player()
        player.name = request.name
        player.color.extend(request.color)
        player.game_over = request.game_over
        player.position.extend(request.position)
        players.append(player)
        return Confirmed(confirmation=True)

    def send_high_score(self, request, context):
        print("This sends high score to server")
        high_score = High_score()
        high_score.name = request.name
        high_score.score = request.score
        leaderboard.append(high_score)
        return Confirmed(confirmation=True)

    def send_fruit(self, request, context):
        print("This sends eaten fruit to server")
        position = Position()
        position.x = request.x
        position.y = request.y
        fruits.append(position)
        return Confirmed(confirmation=True)

    def get_players(self, request, context):
        print("This sends players to clients")
        for p in players:
            yield p

    def get_leaderboard(self, request, context):
        print("This sends leaderboard to clients")
        return Leaderboard(high_score=leaderboard)

    def get_fruits(self, request, context):
        print("This sends fruits to player")
        for f in fruits:
            yield f


def start():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    add_SnakeServicer_to_server(Snake(), server)
    server.add_insecure_port("localhost:9999")
    server.start()
    try:
        while True:
            print("server on: threads {}".format(threading.activeCount()))
            time.sleep(5)
    except KeyboardInterrupt:
        print("KeyBoardInterrupt")
        server.stop(0)


if __name__ == "__main__":
    start()
