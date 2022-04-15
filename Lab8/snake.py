import pygame, sys
from pygame.locals import *
import random
 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen_width = 600
screen_height = 400
 
DISPLAYSURF = pygame.display.set_mode((600,400))
DISPLAYSURF.fill(WHITE)
class Food():
     def __init__(self):         
        self.food_size_x = 10
        self.food_size_y = 10
        self.food_pos = [random.randint(1, screen_width/10)*10,random.randint(1, screen_height/10)*10]

     def draw_food(self):
        pygame.draw.rect(DISPLAYSURF, BLUE, pygame.Rect(self.food_pos[0], self.food_pos[1],self.food_size_x, self.food_size_y))

F1=Food()

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    F1.draw_food()
    pygame.display.update()
    
   