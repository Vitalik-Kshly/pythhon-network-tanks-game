import pickle, socket, threading, os
# from .client import GameData
from abc import abstractmethod, ABC

class Sockets(ABC):
    '''
    Accept & handle clients

    '''
    ADDR = ('localhost', 3000)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    @abstractmethod
    def get_data(self, conn: socket, addr):
        pass

    @abstractmethod
    def send_data(self):
        pass
    
    @abstractmethod
    def connect():
        pass
class Player:
    def __init__(self, conn, addr, client_thread, data) -> None:
        self.addr = addr
        self.conn = conn
        self.data = data
        self.client_thread = client_thread

class GameData:
    def __init__(self) -> None:
        self.pos_x = self.pos_y = None
        self.angle = 0
        self.keys = {'W':0, "A":0, "S":0, "D":0}

class Server(Sockets):
    
    connections = {}
    
    def __init__(self) -> None:
        self.data = None
        self.s.bind(self.ADDR)
        self.s.listen(1)
        threading.Thread(target= self.connect).start()
        threading.Thread(target= self.send_data).start()
        
        

    
    def connect(self):
        while True:
            sock, addr = self.s.accept()
            client_thread = threading.Thread(target=self.get_data, args=(sock, addr)).start()
            self.connections.update({addr : Player(sock, sock.getpeername(), client_thread, GameData())})
            print(f'{sock.getpeername()} new connection!\n{len(self.connections)} user(s) already connected!')

    def get_data(self, sock: socket, addr):
        while True:
            
            try:
                self.connections[addr].data.keys = pickle.loads(sock.recv(4096))
                pass    
            except:
                pass


    def send_data(self):
        while True:
            try:
                if len(self.connections):
                    for key in self.connections:
                        for i in self.connections:
                            self.connections[i].conn.send(pickle.dumps(self.connections[key].data))
            except Exception as e:
                pass


class Client(Sockets):
    def __init__(self) -> None:
        self.connect()
        threading.Thread(target=self.get_data).start()
        self.addr = self.s.getsockname()
    
    def connect(self):
        try:
            self.s.connect(self.ADDR)
            print(f'{self.s.getpeername()} connected!')
        except:
            print('Something was wrong!')
    
    def get_data(self):
        while True:
            try:
                self.data = pickle.loads(self.s.recv(4096))
            except:
                pass
        
    def send_data(self, data):
        self.s.send(data)


if __name__ == "__main__":
    server = Server()