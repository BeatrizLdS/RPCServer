import chatServerRPC
import gameServerRPC
import threading


if __name__ == '__main__':
    # Inicia o servidor de jogos em uma nova thread
    game_thread = threading.Thread(target=gameServerRPC.start_game_server)
    game_thread.start()

    # Inicia o servidor de chat em uma nova thread
    chat_thread = threading.Thread(target=chatServerRPC.start_chat_server)
    chat_thread.start()

    # Aguarda o término das threads
    game_thread.join()
    chat_thread.join()