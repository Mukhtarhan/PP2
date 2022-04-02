def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
import pygame   
pygame.init()
screen = pygame.display.set_mode((800, 500))
done = False
clock = pygame.time.Clock()
image = pygame.image.load('lab7\mickey.jpeg')
image_rh=pygame.image.load('lab7\ighthand.jpeg')
image_lh=pygame.image.load('lab7\lefthand.jpeg')
image = pygame.transform.scale(image,(800,500))
image_rh = pygame.transform.scale(image_rh,(790,505))
image_lh = pygame.transform.scale(image_lh,(790,505))
image_rh.set_colorkey((0,0,0))
image_lh.set_colorkey((0,0,0))
angle=0
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill((255,255,255))
        screen.blit(image,(20,20))
        screen.blit(rot_center(image_rh,10),(20,20))
        screen.blit(rot_center(image_lh,20),(20,20))
        clock.tick(60) 
        pygame.display.flip()