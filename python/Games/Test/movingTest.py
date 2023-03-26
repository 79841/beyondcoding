import pygame

pygame.init()

screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption("test moving")

clock = pygame.time.Clock()


class Box:
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.color = c

    def draw(self, screen):
        pygame.draw.rect(
            screen, self.color, [self.x, self.y, self.width, self.height], 0
        )


playing = True
screen.fill((0, 0, 100))
box = Box(100, 100, 50, 50, (255, 255, 255))

while playing:
    clock.tick(60)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        playing = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        box.y -= 5
    if pressed[pygame.K_a]:
        box.x -= 5
    if pressed[pygame.K_s]:
        box.y += 5
    if pressed[pygame.K_d]:
        box.x += 5

    box.draw(screen)

    pygame.display.update()


pygame.quit()
