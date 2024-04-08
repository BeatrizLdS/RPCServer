import grpc
from concurrent import futures
import game_pb2
import game_pb2_grpc

class GameService(game_pb2_grpc.GameServiceServicer):
    def __init__(self):
        self.users = []
        self.moves = []
        
    def Connect(self, request, context):
        self.users.append(request.name)
        print(len(self.users))
        if len(self.users) == 1:
            return game_pb2.GameState(state="FIRST_TO_CONNECT")
        return game_pb2.GameState(state="START_GAME")
    
    def SendMove(self, request, context):
        print("Received move: ", request)
        self.moves.append(request)
        return game_pb2.Empty()

    def GameStream(self, request, context):
        lastIndex = 0
        while True:
            while len(self.moves) > lastIndex:
                current_move = self.moves[lastIndex]
                lastIndex += 1
                yield current_move    
                
def start_game_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    game_pb2_grpc.add_GameServiceServicer_to_server(GameService(), server)
    server.add_insecure_port('[::]:1200')
    server.start()
    print("Server started listening on port 1200")
    server.wait_for_termination()