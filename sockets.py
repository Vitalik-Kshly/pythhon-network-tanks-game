import pickle, socket, threading, os
# from .client import GameData
from abc import abstractmethod, ABC

class Sockets(ABC):
    '''
    Accept & handle clients

    '''
    ADDR = ('192.168.0.116', 3000)
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
class PlayerObj:
    def __init__(self, addr, data) -> None:
        self.addr = None
        self.data = data
        

class GameData:
    def __init__(self) -> None:
        self.pos_x = self.pos_y = 0
        self.angle = 0
        self.keys = {'W':0, "A":0, "S":0, "D":0}

class Server(Sockets):
    
    connections = {}
    
    def __init__(self) -> None:
        self.data = None
        self.s.bind(self.ADDR)
        self.s.listen(1)
        self.speed = 0.09
        threading.Thread(target= self.connect).start()
        threading.Thread(target= self.send_data).start()
        
        

    
    def connect(self):
        while True:
            sock, addr = self.s.accept()
            client_thread = threading.Thread(target=self.get_data, args=(sock, addr)).start()
            self.connections.update({sock : PlayerObj(sock.getpeername(), GameData())})
            print(f'{sock.getpeername()} new connection!\n{len(self.connections)} user(s) already connected!')

    def get_data(self, sock: socket, addr):
        while True:
            
            try:
                data = pickle.loads(sock.recv(4096))
                if data == 'CLOSE':
                    print(f'{sock.getpeername()} disconnected!')
                    del self.connections[sock]
                    del sock
                    break
                else:
                    self.connections[sock].data.keys = data
                    # os.system('cls')
                    # print(f'{sock.getpeername()}: {data}')
                    self.calculate(data, sock)
                    pass    
            except:
                pass
    
    def calculate(self, data, sock):
        if data['W'] and self.connections[sock].data.pos_y > 0:
            self.connections[sock].data.pos_y -= self.speed
        if data['A'] and self.connections[sock].data.pos_x > 0:
            self.connections[sock].data.pos_x -= self.speed
        if data['S'] and self.connections[sock].data.pos_y < 750:
            self.connections[sock].data.pos_y += self.speed
        if data['D'] and self.connections[sock].data.pos_x < 750:
            self.connections[sock].data.pos_x += self.speed
        return

    def send_data(self):
        while True:
            
            try:
                if len(self.connections):
                    data = []
                    for key in self.connections:
                        data.append(self.connections[key])
                    for key in self.connections:
                        key.send(pickle.dumps(data))    
            except Exception as e:
                # print(e)
                pass


class Client(Sockets):
    def __init__(self, addr) -> None:
        self.ADDR = (addr, 3000)
        self.connect()
        threading.Thread(target=self.get_data).start()
    
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