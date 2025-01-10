import socket

with socket.create_connection(("localhost", 9092)) as sock:
    sock.sendall(b"00000023001200046f7fc661")
    output=sock.recv(1024)
    print(type(output.decode()))
    print(output.decode())
    print(output)
