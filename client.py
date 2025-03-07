import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

# create tcp socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

print(f"[+] Connected to {SERVER_IP}:{SERVER_PORT}")

# send and receive messages
while True:
    message = input("[Client] Type a message: ")
    client_socket.send(message.encode())

    if message.lower() == "exit":
        print("[!] Disconnecting...")
        break

    response = client_socket.recv(1024).decode()
    print(f"[Server] {response}")
    
# close connection
client_socket.close()