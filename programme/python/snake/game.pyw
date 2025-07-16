import pygame
pygame.init()
import time
import random

running = True

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)
text = font.render("Game Over", True, (15, 10, 10))
food = (17, 0)
snake = [(10, 10), (9, 10), (8, 10)]
direction = (1, 0)
score = 0

def place_food():
    while True:
        pos = (random.randint(0, 19), random.randint(0, 19))
        if pos not in snake:
            return pos

while running:
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_z or event.key == pygame.K_w) and direction != (0, 1):
                direction = (0, -1)
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != (0, -1):
                direction = (0, 1)
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_q or event.key == pygame.K_a) and direction != (1, 0):
                direction = (-1, 0)
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != (-1, 0):
                direction = (1, 0)

    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx, head_y + dy)

    if not (0 <= new_head[0] < 20 and 0 <= new_head[1] < 20):
        screen.blit(text, (100, 180))
        pygame.display.flip()
        time.sleep(3)
        running = False

    if new_head in snake:
        screen.blit(text, (100, 180))
        pygame.display.flip()
        time.sleep(3)
        running = False

    if new_head == food:
        score += 1
        food = place_food()
    else:
        snake.pop()

    snake.insert(0, new_head)

    screen.fill((255, 255, 255))

    for xy in range(0, 400, 20):
        pygame.draw.line(screen, pygame.Color('black'), (xy, 0), (xy, 400))
        pygame.draw.line(screen, pygame.Color('black'), (0, xy), (400, xy))

    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(food[0]*20, food[1]*20, 20, 20))

    for pos in snake:
        rect = pygame.Rect(pos[0] * 20, pos[1] * 20, 20, 20)
        pygame.draw.rect(screen, pygame.Color('red'), rect)

    pygame.display.flip()
pygame.quit()