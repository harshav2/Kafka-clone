import socket

with socket.create_connection(("localhost", 9092)) as sock:
    sock.sendall(b"00000023001200046f7fc661")
    output=sock.recv(1024)
    print(type(output.decode()))
    print(output.decode())
    print(output)
    print(len(output))
'''
cd /d/vsc/misc/codecrafters-kafka-python    
sh your_program.sh
'''