import pygame
import random
import time

pygame.init()

##IMAGES
cactus=pygame.image.load("cactus.png")
images=[pygame.image.load("R1.png"),pygame.image.load("R2.png"),pygame.image.load("R3.png"),pygame.image.load("R4.png"),pygame.image.load("R5.png"),pygame.image.load("R6.png"),pygame.image.load("R7.png"),pygame.image.load("R8.png")]
sun_image=pygame.image.load("planet-2.png")
cloud_image=pygame.image.load("cloud-1.png")
back=pygame.image.load("back-land.png")
back2=pygame.image.load("back-land.png")
back_sky=pygame.image.load("back-sky.png")


##COLORS
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
white=(255,255,255)

add=False
image_count=0
isJump=False
jumpCount=10
WIDTH=800
HEIGHT=400
score=0
fps=60
gameloop=True




##SCORE
font_name=pygame.font.match_font("arial")
def draw_text(surf,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,black)
    text_rect=text_surface.get_rect()
    text_rect.center=(x,y)
    surf.blit(text_surface,text_rect)


##BACKGROUNDS
class backg(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(back,(WIDTH,100))
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=350

    def update(self):
        self.rect.x-=10


class backg1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(back2,(WIDTH,100))
        self.rect=self.image.get_rect()
        self.rect.x=800
        self.rect.y=350

    def update(self):
        self.rect.x-=10        



###PLAYER    
class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(images[image_count],(50, 50))
        self.rect=self.image.get_rect()
        self.rect.x=50
        self.rect.y=305
        

        
###CACTUS            
class objects(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(cactus,(20,80))
        self.rect=self.image.get_rect()
        self.rect.center=(800,320)

    def update(self):
        self.rect.x-=10
        if self.rect.right<-10:
            self.rect.x=800




###SUN
class sun(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(sun_image,(30,30))
        self.rect=self.image.get_rect()
        self.rect.center=(800,100)

    def update(self):
        self.rect.x-=1
        obj.image=pygame.transform.scale(cactus,(40,100))
        player.image = pygame.transform.scale(images[image_count],(50, 50))
        cloud.image=pygame.transform.scale(cloud_image,(50,30))
                                           
        if self.rect.right<0:
            self.rect.x=1600
        if self.rect.left>800:
            obj.image=pygame.transform.scale(cactus,(40,100))
            player.image = pygame.transform.scale(images[image_count],(50, 50))
            cloud.image=pygame.transform.scale(cloud_image,(50,30))



###CLOUD
class clouds(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(cloud_image,(50,30))
        self.rect=self.image.get_rect()
        self.rect.center=(800,130)

    def update(self):
        self.rect.x-=2
        if self.rect.right<0:
            self.rect.x=800



            
###GAME WINDOW 
surface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space-Fight")
clock=pygame.time.Clock()


###OBJECTS
all_sprites=pygame.sprite.Group()
backg=backg()
all_sprites.add(backg)

backg1=backg1()
all_sprites.add(backg1)

sun=sun()
all_sprites.add(sun)

obj=objects()
all_sprites.add(obj)

cloud=clouds()
all_sprites.add(cloud)

player=player()
all_sprites.add(player)



###GAME LOOP
while gameloop:
    
    score+=1
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
            player.rect.y=305
            isJump=False

    if key[pygame.K_UP]:
        time.sleep(5)
        

    surface.fill(black)  
    all_sprites.update()
    if image_count<7:
        image_count+=1
    else:
        image_count=0

        
    if backg.rect.right<=0:
        backg.rect.x=800
    if backg1.rect.right<=0:
        backg1.rect.x=800
    
    if sun.rect.left>800:
        surface.fill((169,169,169))
    else:
        surface.blit(back_sky,(0,0))


    #######COLLISIONS
    if player.rect.right>obj.rect.left and player.rect.left<obj.rect.left and player.rect.bottom>obj.rect.top and player.rect.top<obj.rect.bottom:
        gameloop=False
    
    
        
    all_sprites.draw(surface)
    #final_score="Score"+str(score)
    draw_text(surface, "Score"+":"+str(score), 28, 70, 20)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()


