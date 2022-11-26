# client.py
import socket
import time
import threading

PORT = 5050
SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client


def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)


def recv(connection, username):
    while True:
        msg = connection.recv(1024).decode(FORMAT)
        if f"[{username}]" not in msg:
            print(f"\r{msg}                 ")
            print("Message (q for quit): ", end="")


def start():
    answer = input("Would you like to connect (yes/no)? ")
    if answer.lower() != "yes":
        return

    connection = connect()
    username = input("What is your name? ")
    send(connection, username)
    thread = threading.Thread(target=recv, args=(connection, username), daemon=True)
    thread.start()
    while True:
        msg = input("Message (q for quit): ")

        if msg == "q":
            break

        send(connection, msg)

    send(connection, DISCONNECT_MESSAGE)
    time.sleep(1)
    print("Disconnected")


start()
# import socket

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(("localhost", 9999))

# done = False
# while not done:
#     client.send(input("Message: ").encode("utf-8"))
#     msg = client.recv(1024).decode("utf-8")
#     if msg == "quit":
#         done = True
#     else:
#         print(msg)
