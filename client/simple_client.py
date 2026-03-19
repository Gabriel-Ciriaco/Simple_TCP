import warnings
import socket

class Client:

    def __init__(self, IPV4: tuple) -> None:
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
        
            print(f"\nSuccessly connected to : {(self.SERVER_HOST, self.SERVER_PORT)}", end="\n\n")
            
            print(f"Client started on {self.socket.getsockname()}!\n")
        
            self.enviar_input()
        

        except ConnectionRefusedError:
            warn_msg = f"Connection to {(self.SERVER_HOST, self.SERVER_PORT)} was refused. The server might be down or not listening."
            warnings.warn(warn_msg)

    def enviar_input(self):
        if self.socket:
            while True:
                message = input("Escreva uma mensagem: ")
                        
                self._send(message)

                self._recv()
                        
                if message == "FIM":
                    break
    
    def _send(self, message):
        if message:
            self.socket.send(message.encode("utf-8"))

    def _recv(self):
        if self.socket:
            data = self.socket.recv(1024)

            if not data:
                return

            message = data.decode("utf-8")

            print(f"Server responded: {message}")


if __name__ == "__main__":
    with Client(("localhost", 5000)) as c:
        c.connect()