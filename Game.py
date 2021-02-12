 
from sockets import Server
import os


class Game:
    def __init__(self) -> None:
        self.server = Server()
        self.players = {}
    
    def update(self):
        while True:
            temp_data = self.server.get_data()
            self.players[temp_data.addr] = temp_data


if __name__ == "__main__":
    game = Game()