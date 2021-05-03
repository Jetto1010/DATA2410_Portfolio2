from data_pb2 import *
from data_pb2_grpc import *
import time
import grpc


def run():
    channel = grpc.insecure_channel("localhost:9999")
    service = SnakeStub(channel)
    print(service.send_player(send_player()).confirmation)
    print(service.send_high_score(send_high_score()).confirmation)
    print(service.send_fruit(send_fruit()).confirmation)


def send_player():
    print("Sending player...")
    player = Player()
    player.name = "Test"
    player.color.extend([1, 2, 3])
    player.game_over = False
    position = player.position.add()
    position.x = 1
    position.y = 2
    return player


def send_high_score():
    print("Sending high score...")
    high_score = High_score()
    high_score.name = "Test_high"
    high_score.score = 34
    return high_score


def send_fruit():
    print("Sending fruit...")
    position = Position()
    position.x = 34
    position.y = 54
    return position


if __name__ == "__main__":
    run()
