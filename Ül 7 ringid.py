import pygame
import random

WIDTH, HEIGHT = 800, 600
RADIUS = 10

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ringide joonistamine - Metsjärv")

clock = pygame.time.Clock()

circles = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            circles.append((x, y, color))

    screen.fill((153, 232, 158))

    for circle in circles:
        pygame.draw.circle(screen, circle[2], (circle[0], circle[1]), RADIUS, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()