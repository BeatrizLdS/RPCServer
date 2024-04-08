import chatServerRPC
import gameServerRPC
import threading


if __name__ == '__main__':
    threading.Thread(target=gameServerRPC.start_game_server, daemon=True).start()
    # threading.Thread(target=chatServerRPC.start_chat_server, daemon=True).start()