import grpc
from concurrent import futures
import chat_pb2_grpc
import chat_pb2

class ChatService(chat_pb2_grpc.ChatServiceServicer):
    def __init__(self):
        self.chats = []
    
    def SendMessage(self, request, context):
        print("Received message:", request)
        self.chats.append(request)
        print(self.chats)
        return request
    
    def ChatStream(self, request_iterator, context):
        lastIndex = 0
        while True:
            while len(self.chats) > lastIndex:
                current_chat = self.chats[lastIndex]
                lastIndex += 1
                yield current_chat


def start_chat_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(), server)
    server.add_insecure_port('[::]:1100')
    server.start()
    print("Server started listening on port 1100")
    server.wait_for_termination()
