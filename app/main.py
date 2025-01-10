import socket  # noqa: F401

def create_message(message):
    correlation_id_bytes = message[8:12]

    message_bytes = correlation_id_bytes

    message_size = len(message_bytes).to_bytes(4, byteorder="big") #byte order refers to byte endian

    return message_size+message_bytes


def handleClient(client):
    output=client.recv(1024)
    client.sendall(create_message(message=output))

def main():
    print("Logs from your program will appear here!")

    server = socket.create_server(("localhost", 9092))
    server.listen(1)

    while True:
        client, address = server.accept()
        handleClient(client=client)
if __name__ == "__main__":
    main()
