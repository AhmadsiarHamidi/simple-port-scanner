import socket

HOST = "127.0.0.1"
PORT = 80

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"[*] Listening on {HOST}:{PORT} ...")

conn, addr = server.accept()
print(f"[+] Connection from {addr}")

conn.close()
server.close()
