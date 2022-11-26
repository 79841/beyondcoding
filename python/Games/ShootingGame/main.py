# main.py
import pygame
import object
import math
import time


import threading
import socket

PORT = 5050
SERVER = "localhost"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SIZE = [600, 600]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Shooting Game")


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


connection = connect()
# thread = threading.Thread(target=recv, args=(connection, username), daemon=True)
# thread.start()

playing = True
clock = pygame.time.Clock()

player = object.Player(300, 500, 30, 30, GREEN, 5)

bullets = []

enemy = object.Box(200, 200, 30, 30, RED, 5)

while playing:

    clock.tick(120)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        playing = False

    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()

        bullet = object.Bullet(player.center_x, player.center_y, 4, 4, BLACK, 10)

        bullet.set_direction(pos[0], pos[1])
        bullets.append(bullet)

    player.move(pygame.key.get_pressed(), screen.get_size())
    send(connection, f"{player.x_pos},{player.y_pos}")

    screen.fill(WHITE)
    player.draw(screen)

    for bullet in bullets:
        bullet.move()
        bullet.draw(screen)

    bullets = list(filter(lambda b: b.check_hit_wall(screen), bullets))

    enemy.draw(screen)

    pygame.display.update()

    for bullet in bullets:
        if bullet.check_collision(enemy):
            playing = False

pygame.quit()


# while True:
#     msg = input("Message (q for quit): ")

#     if msg == "q":
#         break

#     send(connection, msg)

# send(connection, DISCONNECT_MESSAGE)
# time.sleep(1)
# print("Disconnected")
