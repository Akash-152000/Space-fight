import pygame
import random

pygame.init()

black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
white=(255,255,255)

isJump=False
jumpCount=10
WIDTH=800
HEIGHT=400
fps=60
gameloop=True

class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(red)
        self.rect=self.image.get_rect()
        self.rect.x=50
        self.rect.y=355
        

        
            
class objects(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((20,80))
        self.image.fill(blue)
        self.rect=self.image.get_rect()
        self.rect.center=(800,360)

    def update(self):
        self.rect.x-=10
        if self.rect.right<-10:
            self.rect.x=800


class sun(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        

surface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space-Fight")
clock=pygame.time.Clock()

all_sprites=pygame.sprite.Group()
player=player()
all_sprites.add(player)

obj=objects()
all_sprites.add(obj)

while gameloop:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
    key=pygame.key.get_pressed()
    if not(isJump):
        if key[pygame.K_SPACE]:
            isJump=True
    else:
        if jumpCount>=0:
            player.rect.y-=(jumpCount*jumpCount)*0.5
            jumpCount-=1
        elif jumpCount<0 and jumpCount>=-10:
            player.rect.y+=(jumpCount*jumpCount)*0.5
            jumpCount-=1
        else:
            jumpCount=10
            player.rect.y=355
            isJump=False 

        
    all_sprites.update()
    surface.fill(black)
    all_sprites.draw(surface)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()

