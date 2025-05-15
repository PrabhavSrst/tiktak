import pygame
from pygame.locals import *

pygame.init()   
screen_width=300
screen_height=300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('tictactoe')
line_width=4
run= True
def draw_grid():
    bg = (225, 225, 225)
    grid = (0, 0, 0)
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), line_width)
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, screen_height), line_width)
while run:
    draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()