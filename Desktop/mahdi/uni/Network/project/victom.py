import socket
from pyautogui import *
from PIL import ImageGrab

HOST = '127.0.0.1'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print('Connected by', addr)

# Take screenshot
img = ImageGrab.grab()
img_byte_arr = img.tobytes()

# Send screenshot data
conn.send(img_byte_arr)


with open('file.txt', 'rb') as f:
    data = f.read(1024)
    while data:
        conn.send(data)
        data = f.read(1024)



while True:
    data = conn.recv(1024).decode()
    if data == "MOVE_UP":
        move(0, -50)
    elif data == "MOVE_DOWN":
        move(0, 50)
    elif data == "MOVE_LEFT":
        move(-50, 0)
    elif data == "MOVE_RIGHT":
        move(50, 0)
    elif data == "CLICK":
        click()
conn.close()