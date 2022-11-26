# server.py
import threading
import socket
import object
import pygame

PORT = 5050
SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = set()
clients_lock = threading.Lock()

x_pos = 0
y_pos = 0


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} Connected")
    global x_pos
    global y_pos

    try:
        connected = True
        while connected:
            msg = conn.recv(1024).decode(FORMAT)
            # if not msg:
            #     break

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")

            try:
                x_pos, y_pos = map(lambda pos: 570 - float(pos), msg.split(","))
                print(x_pos, y_pos)
            except:
                pass

    finally:
        with clients_lock:
            clients.remove(conn)

        conn.close()


# def start():
print("[SERVER STARTED]!")
server.listen()
while True:
    conn, addr = server.accept()
    # with clients_lock:
    # username = conn.recv(1024).decode(FORMAT)
    # clients.add(conn)
    thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
    thread.start()

    pygame.init()

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    SIZE = [600, 600]

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Shooting Game")

    playing = True
    clock = pygame.time.Clock()

    enemy = object.Box(200, 200, 30, 30, RED, 5)

    while playing:

        clock.tick(120)

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            playing = False

        enemy.x_pos = x_pos
        enemy.y_pos = y_pos

        screen.fill(BLACK)

        enemy.draw(screen)

        pygame.display.update()

    pygame.quit()

# start()

# import socket

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server.bind(("localhost", 9999))

# server.listen()

# client, addr = server.accept()

# done = False

# while not done:
#     msg = client.recv(1024).decode("utf-8")
#     if msg == "quit":
#         done = True
#     else:
#         print(msg)
#     client.send(input("Message: ").encode("utf-8"))
