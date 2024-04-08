import grpc
from concurrent import futures
import game_pb2
import game_pb2_grpc

class GameService(game_pb2_grpc.GameServiceServicer):
    def __init__(self):
        self.users = []
            
def start_game_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    game_pb2_grpc.add_GameServiceServicer_to_server(GameService(), server)
    server.add_insecure_port('[::]:1200')
    server.start()
    print("Server started listening on port 1200")
    server.wait_for_termination()