import pygame
import random
pygame.init()
gameExit=True
surface=pygame.display.set_mode((800,600))
pygame.display.set_caption("Game1")
x=0
y=500
height=50
width=50
white=(255,255,255)

ball=pygame.image.load("ball.png")
ax=random.randrange(10,790)
ay=900
height_a=20
width_a=60
speed=7


while gameExit:
    ax=random.randrange(10,790)
    ay=900
    height_a=20
    width_a=60
    speed=7
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameExit=False
        key=pygame.key.get_pressed()
    if key[pygame.K_RIGHT] and x<=790-width:
        x+=1
    if key[pygame.K_LEFT] and x>=10:
        x-=1
    
    surface.fill((255,255,255))

    pygame.draw.rect(surface,(0,0,255),(ax,ay,width_a,height_a))
    ay-=1
    
    if ay<10:
        ax=random.randrange(10,790)
        ay=height_a
    surface.blit(ball,(x,y))
    
    
    pygame.display.flip()
pygame.quit()
