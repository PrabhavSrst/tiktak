import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP

pygame.init()   
screen_width=300
screen_height=300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('tictactoe')
#needed variables
line_width=4
markers=[]
clicked= False
player=1
pos=[]
winner=0
run= True
game=False
#defining colors
green=(0,255,0)
red=(255,0,0 )
blue=(0,0,255)
#define font
font = pygame.font.SysFont(None, 40)
def draw_grid():#function for drawing the grid
    bg = (225, 225, 225)
    grid = (0, 0, 0)
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), line_width)
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, screen_height), line_width)
for x in range(3):
    row=[0]*3
    markers.append(row)
print(markers)
def draw_markers():#function for drawing the markers
    x_pos=0
    for x in markers:
        y_pos=0
        for y in x:
            if y==1:
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
            if y==-1:
                pygame.draw.circle(screen, red, (x_pos * 100 + 50, y_pos * 100 + 50), 40, line_width)
            y_pos+=1
        x_pos+=1

def check_winner():#checking for a winner 
    y_pos=0
    global winner
    global game
    for x in markers:
        #columns
        if sum(x)==3:
            winner=1
            game=True
        if sum(x)==-3:
            winner=2
            game=True
        #rows
        if markers[0][y_pos]+markers[1][y_pos]+markers[2][y_pos]==-3:
            winner = 2
            game=True
        y_pos+=1
#check cross
    if markers[0][0]+markers[1][1]+markers[2][2]==3 or markers[2][0]+markers[1][1]+markers[0][2]==3:
            winner=1
            game=True
    if markers[0][0]+markers[1][1]+markers[2][2]==-3 or markers[2][0]+markers[1][1]+markers[0][2]==-3:
            winner=2
            game=True
def draw_winner(winner):#display winner
    winned='Player ' + str(winner) + " wins" 
    winned= font.render(winned, True, blue)
    pygame.draw.rect(screen, green, (screen_width //2 -100 , screen_height // 2-60, 200, 50))
    screen.blit(winned, (screen_width // 2-100, screen_height // 2 - 50))
while run:#window and game state display
    draw_grid()
    draw_markers()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game==0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked== False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked= False
                pos=pygame.mouse.get_pos()
                cell_x=pos[0]
                cell_y=pos[1]
                if markers[cell_x//100][cell_y//100]==0:
                    markers[cell_x//100][cell_y//100]=player
                    player*=-1 
                    check_winner()
    if game== True:
        draw_winner(winner)

    pygame.display.update()
pygame.quit()