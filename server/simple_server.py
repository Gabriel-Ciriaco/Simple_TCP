import socket

class Server:

    def __init__(self, IPV4: tuple[HOST: str, PORT: int], MAX_CONNECTIONS: int = 1) -> Server:
        self.HOST, self.PORT = IPV4
        self.MAX_CONNECTIONS = MAX_CONNECTIONS

    def __enter__(self):
        
        # Initalizing server as TCP IPV4
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Reuse socket PORT in case of the PORT being in TIME_WAIT
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # It binds an address to the server.
        self.socket.bind((self.HOST, self.PORT))

        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"\nClosing {self.socket.getsockname()}")
        self.socket.close()
    

    '''
        Listening to new connections.
    '''
    def listen_connections(self):

        print(f"Waiting for connection at {(self.HOST, self.PORT)}...\n")

        self.socket.listen(self.MAX_CONNECTIONS)

        connection, address = self.socket.accept()

        with connection:
            print(f"\t{address} established a connection.\n")

            while True:
                data = connection.recv(1024)

                if not data:
                    break

                print(f"\t{address} said: {data.decode("utf-8")}")
                connection.sendall("Bye bye!".encode("utf-8"))



if __name__ == "__main__":
    with Server(("localhost",5000)) as s:
        s.listen_connections()
