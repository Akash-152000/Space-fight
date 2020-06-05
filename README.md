# Space-fight
pygame is a python framework developed for making games in python.

Best way to install pygame is pip tool
>pip install pygame

Pygame makes it easy for the begineers to learn and implement the basics of 2d game development.
Along with pygame python provides various different frameworks for developing games.

After the installation pf pygame, we can get started to devlope our game.In pygame mostly all games have same start,below is the template which 
ca be edited as per rquirement.

```
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
gameLoop = False

while not gameLoop:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gameLoop = True
        
        pygame.display.flip()
pygame.quit()

```

- **import pygame** - this is of course needed to access the PyGame framework.

- **pygame.init()** - This kicks things off. It initializes all the modules required for PyGame.

- **pygame.display.set_mode((width, height))** - This will launch a window of the desired size. The return value is a Surface object which is the object you will perform graphical operations on. This will be discussed later.

- **pygame.event.get()** - this empties the event queue. If you do not call this, the windows messages will start to pile up and your game will become unresponsive in the opinion of the operating system.

- **pygame.QUIT** - This is the event type that is fired when you click on the close button in the corner of the window.

- **pygame.display.flip()** - PyGame is double-buffered. This swaps the buffers. All you need to know is that this call is required in order for any updates that you make to the game screen to become visible.


# Getting started
If you want to implement this project follow the below steps.

* **Clone this repository**

For cloning the repository open ur terminal and move to the local repository where you want to download the project and then run the below snippet

```
git clone 
```


