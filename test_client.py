from data_pb2 import *
from data_pb2_grpc import *
import grpc

channel = grpc.insecure_channel("localhost:9999")
service = SnakeStub(channel)


def run():
    # print(service.send_high_score(send_high_score()).confirmation)
    # print(service.send_fruit(send_fruit()).confirmation)
    # print(get_leaderboard())
    # print(get_size())
    # print(get_information())
    print(service.send_player(make_player()).confirmation)
    channel.close()


def make_player():
    print("Making player...")
    player = Player()
    player.name = "Test2"
    player.color.extend([1, 2, 3])
    player.game_over = False
    positions = []
    for i in range(5):
        pos = Position()
        pos.x = 3*4 + i
        pos.y = 24
        positions.append(pos)
    player.position.extend(positions)
    return player


def send_high_score():
    print("Sending high score...")
    high_score = High_score()
    high_score.name = "Test_high"
    high_score.score = 6
    return high_score


def send_fruit():
    print("Sending fruit...")
    position = Position()
    position.x = 18
    position.y = 10
    return position


def get_leaderboard():
    print("Getting fruits...")
    return service.get_leaderboard(No_parameter())


def get_size():
    print("Getting size...")
    return format(service.get_size(No_parameter()))


def get_information():
    print("Getting information...")
    request = service.get_information(make_player())
    return_str = ""
    for r in request:
        return_str += format(r.player) + " "
        return_str += format(r.fruit) + " "
    return return_str


if __name__ == "__main__":
    run()
