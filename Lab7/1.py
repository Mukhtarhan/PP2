import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
done = False

clock = pygame.time.Clock()

image = pygame.image.load('lab7\mickeyclock.jpeg')
image = pygame.transform.scale(image,(400,400))
angle=0
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                
    

        

        image = pygame.transform.rotate(image, angle)
        angle += 1

        screen.blit(image, 20)    
        pygame.display.flip()