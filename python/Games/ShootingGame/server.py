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

# x_pos = 0
# y_pos = 0

e_x_pos, e_y_pos = 0, 0
eb_x_pos, eb_y_pos = 0, 0

enemy_bullets = []


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} Connected")
    global e_x_pos, e_y_pos, eb_x_pos, eb_y_pos
    global enemy_bullets
    # global y_pos

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
                ob, x_pos, y_pos = msg.split(",")
                x_pos = 570 - float(x_pos)
                y_pos = 570 - float(y_pos)
                if ob == "player":
                    e_x_pos, e_y_pos = x_pos, y_pos
                elif ob == "bullet":
                    eb_x_pos, eb_y_pos = x_pos, y_pos
                    bullet = object.Bullet(e_x_pos + 15, e_y_pos + 15, 4, 4, RED, 10)

                    bullet.set_direction(eb_x_pos, eb_y_pos)
                    enemy_bullets.append(bullet)
                    # x_pos, y_pos = map(lambda pos: 570 - float(pos), msg.split(","))
                print(ob, x_pos, y_pos)
            except Exception as e:
                print(e)

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

        enemy.x_pos = e_x_pos
        enemy.y_pos = e_y_pos

        screen.fill(BLACK)

        enemy.draw(screen)

        for bullet in enemy_bullets:
            bullet.move()
            bullet.draw(screen)

        enemy_bullets = list(filter(lambda b: b.check_hit_wall(screen), enemy_bullets))

        pygame.display.update()

        # for bullet in enemy_bullets:
        #     if bullet.check_collision(enemy):
        #         playing = False

        print(enemy_bullets)

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
