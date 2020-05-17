import pygame
import random
pygame.init()
gameExit=True
surface=pygame.display.set_mode((800,600))
pygame.display.set_caption("Game1")
x=0
y=555
height=50
width=50
white=(255,255,255)
clock=pygame.time.Clock()
ball=pygame.image.load("ball.png")
ax=800
ay=580
height_a=2100
width_a=60
speed=7
jumpCount=10
isJump=False
num=2

while gameExit:
    if num<30:
        num+=0.01
#    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameExit=False
        key=pygame.key.get_pressed()
    if key[pygame.K_RIGHT] and x<=790-width:
        x+=5
    if key[pygame.K_LEFT] and x>=10:
        x-=5

    if not(isJump):
        if key[pygame.K_SPACE]:
            isJump=True
    else:
        if jumpCount>=-10:
            y-=(jumpCount*abs(jumpCount))*0.5
            jumpCount-=1
        else:
            jumpCount=10
            isJump=False 

    
    surface.fill((255,255,255))

    pygame.draw.rect(surface,(0,0,255),(ax,ay,width_a,height_a))
    ax-=num
    
    if ax<-100:
        ax=800
        ay=random.randrange(450,580)



    surface.blit(ball,(x,y))
    
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

