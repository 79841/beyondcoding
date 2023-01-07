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

e_x_pos, e_y_pos = 0, 0
eb_x_pos, eb_y_pos = 0, 0

enemy_bullets = []


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client


def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)


####
def recv(connection):
    global e_x_pos, e_y_pos, eb_x_pos, eb_y_pos
    global enemy_bullets
    while True:
        msg = connection.recv(1024).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False

        print(f"{msg}")

        try:
            ob, x_pos, y_pos = msg.split(",")
            x_pos = 570 - float(x_pos)
            y_pos = 570 - float(y_pos)
            if ob == "player":
                e_x_pos, e_y_pos = x_pos, y_pos
            elif ob == "bullet":
                eb_x_pos, eb_y_pos = x_pos + 30, y_pos + 30
                bullet = object.Bullet(e_x_pos + 15, e_y_pos + 15, 4, 4, RED, 10)

                bullet.set_direction(eb_x_pos, eb_y_pos)
                enemy_bullets.append(bullet)
                # x_pos, y_pos = map(lambda pos: 570 - float(pos), msg.split(","))
            print(ob, x_pos, y_pos)
        except Exception as e:
            print(e)


####

connection = connect()

####
thread = threading.Thread(target=recv, args=(connection,), daemon=True)
thread.start()
####


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
        send(connection, f"bullet,{pos[0]},{pos[1]}")

    player.move(pygame.key.get_pressed(), screen.get_size())
    send(connection, f"player,{player.x_pos},{player.y_pos}")

    screen.fill(WHITE)
    player.draw(screen)

    for bullet in bullets:
        bullet.move()
        bullet.draw(screen)

    bullets = list(filter(lambda b: b.check_hit_wall(screen), bullets))

    ####
    enemy.x_pos = e_x_pos
    enemy.y_pos = e_y_pos

    enemy.draw(screen)

    for bullet in enemy_bullets:
        bullet.move()
        bullet.draw(screen)

    enemy_bullets = list(filter(lambda b: b.check_hit_wall(screen), enemy_bullets))

    ####

    pygame.display.update()

    for bullet in bullets:
        if bullet.check_collision(enemy):
            playing = False

    ####
    for bullet in enemy_bullets:
        if bullet.check_collision(player):
            playing = False
    ####

pygame.quit()
