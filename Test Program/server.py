import socket

HOST = ""
PORT = 5000
data = ""

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))

print(f"Socket Successfully Created at PORT = {PORT}\n")

sock.listen(1)
print(f"socket is listening...\n")

while True:
    conn, addr = sock.accept()
    print(f"Connection from : {addr}")

    data = conn.recv(10240).decode()
    if not data:
        break

    print(f"message from client : {data}")

    conn.send(data.encode())

sock.close()
