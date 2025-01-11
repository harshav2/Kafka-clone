import socket

with socket.create_connection(("localhost", 9092)) as sock:
    sock.sendall(bytes.fromhex("00000023001200046f7fc661"))
    output=sock.recv(1024)
    print(len(output), output)
    for i in output:
        print(i, chr(i))
'''
cd /d/vsc/misc/codecrafters-kafka-python    
sh your_program.sh
'''