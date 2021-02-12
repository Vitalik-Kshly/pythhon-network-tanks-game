import pickle, socket, threading
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
        def __init__(self, conn, addr, client_thread) -> None:
            self.addr = addr
            self.conn = conn
            self.data = None
            self.client_thread = client_thread

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
            # con = self.Connection(conn, addr)
            client_thread = threading.Thread(target=self.get_data, args=(sock, addr))
            self.connections[addr] = Player(sock, addr, client_thread)

    def get_data(self, sock: socket, addr):
        while True:
            try:
                self.connections[addr].data = pickle.loads(sock.recv(4096))
            except:
                pass

    def send_data(self, sock, data):
        sock.send(data)


class Client(Sockets):
    def __init__(self) -> None:
        self.connect()
        threading.Thread(target=self.get_data, args=(self.s, None)).start()
        self.addr = self.s.getsockname()

    def connect(self):
        try:
            self.s.connect(self.ADDR)
        except:
            print('Something was wrong!')
    
    def get_data(self, conn: socket, addr):
        while True:
            try:
                self.data = pickle.loads(conn.recv(4096))
                
            except:
                pass
        
    def send_data(self, data):
        self.s.send(data)


if __name__ == "__main__":
    server = Server()