import pickle, socket, threading
from abc import abstractmethod, ABC


class Sockets(ABC):
    '''
    Accept & handle clients

    '''
    ADDR = ('localhost', 3000)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    
    def get_data(self, conn: socket):
        while True:
            data = conn.recv(4096)
            try:
                tank = pickle.loads(data)
                print(f'We\'v got a message:\n {tank.name} ')
            except:
                pass

    def send_data(self):
        for (addr, conn) in self.connections:
            conn.send()
    
    @abstractmethod
    def connect():
        pass

class Server(Sockets):
    
    def __init__(self) -> None:
        self.s.bind(self.ADDR)
        self.s.listen(1)
        threading.Thread(target= self.connect).start()
        self.connections = {}
        

    
    def connect(self):
        while True:
            conn, addr = self.s.accept()
            print(f'{conn} had just connected!')
            self.connections[addr] = conn
            threading.Thread(target= self.get_data, args= (conn,)).start()


class Client(Sockets):
    def __init__(self) -> None:   
        self.connect()
        threading.Thread(target=self.get_data, args=(self.s,)).start()

    def connect(self):
        try:
            self.s.connect(self.ADDR)
        except:
            print('Something was wrong!')



if __name__ == "__main__":
    server = Server()