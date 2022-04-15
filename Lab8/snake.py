import pygame
from random import randrange

RES=800
SIZE=50

x, y= randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs={'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': True}
length=1  
snake=[(x,y)]
dx, dy = 0, 0
fps=5

pygame.init()
sc=pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

while True:
    sc.fill(pygame.Color('black'))
    [(pygame.draw.rect(sc,pygame.Color('green'),(i, j, SIZE, SIZE))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))
    
    x+=dx*SIZE
    y+=dy*SIZE
    snake.append((x, y))
    snake=snake[-length:]

    if snake[-1]==apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length+=1
        fps+=1 
    
    if x<0 or x>RES-SIZE or y<0 or y>RES-SIZE:
        break
    if len(snake) != len(set(snake)):
        break

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and dirs['UP']:
        dx, dy = 0, -1   
        dirs = {'UP': True, 'DOWN': False, 'LEFT': True, 'RIGHT': True}   
    if key[pygame.K_DOWN] and dirs['DOWN']:
        dx, dy = 0, 1
        dirs = {'UP': False, 'DOWN': True, 'LEFT': True, 'RIGHT': True}
    if key[pygame.K_LEFT] and dirs['LEFT']:
        dx, dy = -1, 0
        dirs = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': False}
    if key[pygame.K_RIGHT] and dirs['RIGHT']:
        dx, dy = 1, 0
        dirs = {'UP': True, 'DOWN': True, 'LEFT': False, 'RIGHT': True}
