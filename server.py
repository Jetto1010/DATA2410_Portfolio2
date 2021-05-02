from concurrent import futures
import grpc
import data_pb2
import data_pb2_grpc
import time
import threading

def create_fruit():
    return

class Listener(data_pb2_grpc.DataServicer):
    def sendPlayer