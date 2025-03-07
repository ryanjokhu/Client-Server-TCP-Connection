import socket

HOST = '0.0.0.0' #listen on all available interfaces
PORT = 12345 #choose any available port

# create tcp socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(2) #allow 1 client at a time

print(f"[*] Listening on {HOST}:{PORT}")

# accept client connection
client_socket, client_address = server_socket.accept()
print(f"[*] Connection established with {client_address}")

# receive and send messages
while True:
    data = client_socket.recv(1024).decode()
    if not data or data.lower() == "exit":
        print("[!] Client disconnected")
        break
    print(f"[Client] {data}")

    # send response
    response = input("[Server] Type a response: ")
    client_socket.send(response.encode())

# close connection
client_socket.close()
server_socket.close()