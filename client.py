import threading, os
from sockets import Client

class Player:
        def __init__(self, conn, addr) -> None:
            self.addr = None
            self.conn = conn
            self.data = None

class GameData:
    def __init__(self) -> None:
        self.pos_x = self.pos_y = None
        self.angle = 0
        self.keys = {'W':0, "A":0, "S":0, "D":0}


class Player():
    def __init__(self) -> None:
        self.client = Client()
        self.game_data = GameData(self.client.s, self.client.addr)
        threading.Thread(target=self.send_data)

    def send_data(self):
        while True:
            self.client.send_data(self.game_data)

    def get_data(self):
        while True:
            pass


if __name__ == '__main__':
    player = Player()

