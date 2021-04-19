import pygame
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode([800,600])

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

#closing credits or end credits are a list of the movie cast or crew
movie_credits = '''
This video showing how to scroll text
using python coding
has been made by
HAPPY CHUCK PROGRAMMING Channel.
Please support us by clicking Subscribe
Thank you all for watching
'''


centerx, centery = screen.get_rect().centerx, screen.get_rect().centery
deltaY = centery + 50  # adjust so it goes below screen start


running =True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(0)
    deltaY-= 1
    i=0
    msg_list=[]
    pos_list=[]
     
    font = pygame.font.SysFont('Courier', 30)

    #msg = font.render('Hello there, how are you?', True, red)
    for line in movie_credits.split('\n'):
        msg=font.render(line, True, red)
        msg_list.append(msg)
        pos= msg.get_rect(center=(centerx, centery+deltaY+30*i))
        pos_list.append(pos)
        i=i+1
   
    #pos = msg.get_rect(center=(centerx, centery+deltaY))
    

    #if (centery + deltaY < 0):
    #   running = False         # no repetition - once text scrolls up past screen, over 
        
    #screen.blit(msg, pos)
    for j in range(i):
        screen.blit(msg_list[j], pos_list[j])
        
    pygame.display.update()


pygame.quit()

    
    
