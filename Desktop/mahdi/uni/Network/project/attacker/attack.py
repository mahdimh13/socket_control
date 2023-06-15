import socket

SERVER_IP = '10.10.101.100'
SERVER_PORT = 43511

def main():
    # Create a socket
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_addr = (SERVER_IP, SERVER_PORT)
    sockfd.connect(server_addr)

    # Send commands to the server
    command = "start explorer.exe"
    sockfd.send(command.encode())

    # ...

    sockfd.close()

if __name__ == '__main__':
    main()
