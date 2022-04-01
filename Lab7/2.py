import pygame
pygame.init()
list_songs=['Lab7/sample1.ogg','Lab7/sample2.ogg','Lab7/sample3.ogg']
screen = pygame.display.set_mode((400, 400))
done = False
cnt=0
curr=int()
flPause=False


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT :
                     done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    
                         flPause = not flPause
                         if flPause and cnt==0:
                            pygame.mixer.music.load('Lab7/sample1.ogg')
                            curr=0
                            cnt=1
                            pygame.mixer.music.play()
                         elif flPause and cnt==1:
                            pygame.mixer.music.pause()
                            cnt=1
                         else:
                            pygame.mixer.music.unpause()
                            cnt=1
                if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT and curr<=1:
                    curr+=1
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.stop(sound_effect)
                    sound_effect=pygame.mixer.Sound(list_songs[curr])
                    pygame.mixer.Sound.play(sound_effect)
                    
                if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT and curr==2:
                    curr=0
                    pygame.mixer.music.load('Lab7/sample1.ogg')
                    pygame.mixer.music.play()
                    
                if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT and curr>=1:
                    curr-=1
                    pygame.mixer.music.load(list_songs[curr])
                    pygame.mixer.music.play()
                    
                if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT and curr==0: 
                    curr=2 
                    pygame.mixer.music.load('Lab7/sample3.ogg')
                    pygame.mixer.music.play()   
        pygame.display.flip()