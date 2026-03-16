import warnings
import socket

class Client:

    def __init__(self, IPV4: tuple[SERVER_HOST: str, SERVER_PORT: int]) -> None:
        self.SERVER_HOST, self.SERVER_PORT = IPV4
        self.data = None

    def __enter__(self) -> Client:

        # Initalizing server as TCP IPV4
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        

        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing client at {self.socket.getsockname()}")
        self.socket.close()
    

    '''
        Connecting:
    '''
    def connect(self):
        try:        
            self.socket.connect((self.SERVER_HOST, self.SERVER_PORT))
            print(f"Client started on {self.socket.getsockname()}!\n")

            print(f"\nSuccessly connected to : {(self.SERVER_HOST, self.SERVER_PORT)}")

            self.socket.sendall("Hi cool server!".encode("utf-8"))
            self.data = self.socket.recv(1024).decode("utf-8")
        except ConnectionRefusedError:
            warn_msg = f"Connection to {(self.SERVER_HOST, self.SERVER_PORT)} was refused. The server might be down or not listening."
            warnings.warn(warn_msg)

if __name__ == "__main__":
    with Client(("localhost", 5000)) as c:
        c.connect()
        if c.data:
            print(f"\n\tServer responded: {c.data}\n")