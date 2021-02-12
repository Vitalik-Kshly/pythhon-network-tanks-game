import pickle, threading, os, time
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
    alive = True
    def __init__(self) -> None:
        self.client = Client()
        self.game_data = GameData()
        self.thread_send = threading.Thread(target=self.send_data)
        self.thread_send.start()
        self.thread_get = threading.Thread(target=self.get_data)
        self.thread_get.start()
        


    def send_data(self):
        while self.alive:
            print(self.alive)
            self.client.send_data(pickle.dumps(self.game_data.keys))
            # os.system('cls')
            print(self.game_data.keys)

    
    def get_data(self):
        while self.alive:
            
            try:
                self.game_data = pickle.loads(self.client.s.recv(4096))
                print(self.game_data.__dict__)
                pass
            except:
                pass
        
    

if __name__ == '__main__':
    player = Player()

