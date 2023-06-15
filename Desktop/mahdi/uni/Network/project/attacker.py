import socket
from PIL import Image

HOST = '127.0.0.1' # Computer A's IP address
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

img_byte_arr = b''
data = s.recv(1024)

while data:
    img_byte_arr += data
    data = s.recv(1024)

# Save screenshot
img = Image.frombytes('RGB', (1280, 1024), img_byte_arr)
img.save('screenshot.png')

with open('received_file.txt', 'wb') as f:
    while True:
        data = s.recv(1024)
        if not data:
            break
        f.write(data)

while True:
    s.send(b"MOVE_UP")
    s.send(b"MOVE_DOWN")
    s.send(b"MOVE_LEFT")
    s.send(b"MOVE_RIGHT")
    s.send(b"CLICK")
s.close()