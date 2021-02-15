import pickle, threading, os, time
from sockets import Client

class PlayerObj:
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
    alive = True
    def __init__(self, addr) -> None:
        self.client = Client(addr)
        self.game_data = GameData()
        self.player_pos = []
        self.thread_send = threading.Thread(target=self.send_data).start()
        self.thread_get = threading.Thread(target=self.get_data).start()
        


    def send_data(self):
        while self.alive:
            # print(self.alive)
            self.client.send_data(pickle.dumps(self.game_data.keys))
            # os.system('cls')
            # print(self.game_data.keys)

    def close_connection(self):
        self.client.send_data(pickle.dumps("CLOSE"))

    def get_data(self):
        while self.alive:
            # game_data = self.client.s.recv(4096) #pickle.loads()
            
            try:
                self.player_pos = pickle.loads(self.client.s.recv(4096))
                pass
            except:
                pass
        
    

if __name__ == '__main__':
    player = Player()

