import socket  # noqa: F401

def api_versions(message):
    correlation_id_bytes = message[8:12]
    request_api_version = message[6:8]
    api_key = message[4:6]

    min_version = bytes([0x00, 0x00]) 
    max_version = bytes([0x00, 0x04]) 

    if min_version <= request_api_version <= max_version:
        error_code = 0
    else:
        error_code = 35

    error_code_bytes = error_code.to_bytes(2, byteorder="big")
    
    message_bytes = correlation_id_bytes + error_code_bytes + api_key + min_version + max_version

    message_size = len(message_bytes).to_bytes(4, byteorder="big") #byte order refers to byte endian

    return message_size+message_bytes

def create_message(message):
    request_api_key = message[4:6]
    if request_api_key == bytes([0x00, 0x12]):
        return api_versions(message)

def handleClient(client):
    message = client.recv(1024)
    client.sendall(create_message(message))

def main():
    print("Logs from your program will appear here!")

    server = socket.create_server(("localhost", 9092))
    server.listen(1)

    while True:
        client, address = server.accept()
        handleClient(client=client)
if __name__ == "__main__":
    main()
