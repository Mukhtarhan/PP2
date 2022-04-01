
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
done = False

image = pygame.image.load('Lab7/ball.png')
x=20
y=20
clock = pygame.time.Clock()
while not done:
        screen.fill((255, 255, 255))
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_UP]: 
            y-=20
        if pressed[pygame.K_DOWN]: 
            y+=20
        if pressed[pygame.K_LEFT]:
            x-=20
        if pressed[pygame.K_RIGHT]: 
            x+=20
        screen.blit(image,(x,y))    
        pygame.display.flip()
        clock.tick(10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done = True
pygame.quit()       