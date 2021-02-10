from sockets import Client


class GameObject:
    def __init__(self) -> None:
        self.pos_x = self.pos_y = None


class Player:
    def __init__(self) -> None:
        self.client = Client()




player = Player()

