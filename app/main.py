import socket  # noqa: F401

def create_message(id):
    id_bytes = id.to_bytes(4, byteorder="big")  #byte order refers to byte endian 
    message_size = len(id_bytes).to_bytes(4, byteorder="big") 

    return message_size+id_bytes


def handleClient(client):
    client.recv(1024)
    client.sendall(create_message(id=7))

def main():
    print("Logs from your program will appear here!")

    server = socket.create_server(("localhost", 9092), reuse_port=True)
    server.listen(1)

    while True:
        client, address = server.accept()
        handleClient(client=client)
if __name__ == "__main__":
    main()
