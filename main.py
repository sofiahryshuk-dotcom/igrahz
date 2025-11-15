import pygame
import sys
import os
import random
lvl='game'


pygame.init()
currentpath=os.path.dirname(__file__)
os.chdir(currentpath)
W=1200
H=800
FPS=60
sc = pygame.display.set_mode((W,H))
clock = pygame.time.Clock
from load import *
def glvl():
    sc.fill('black')


    brickg.update()
    brickg.draw(sc)
    bushg.update()
    bushg.draw(sc)
    playerg.update()
    playerg.draw(sc)
    enemyg.update()
    enemyg.draw(sc)
    irong.update()
    irong.draw(sc)
    flagg.update()
    flagg.draw(sc)
    waterg.update()
    waterg.draw(sc)
    pygame.display.update()


    class Brick(pygame.sprite.Sprite):
        def __init__(self,image,pos):
            pygame.sprite.Sprite.__init__(self)
            self.image=image
            self.rect=self.image.get_rect()
            self.rect.x=pos[0]
            self.rect.y=pos[1]

    class Water(pygame.sprite.Sprite):
        def __init__(self,image,pos):
            pygame.sprite.Sprite.__init__(self)
            self.image=image
            self.rect=self.image.get_rect()
            self.rect.x=pos[0]
            self.rect.y=pos[1]

    class Iron(pygame.sprite.Sprite):
        def __init__(self,image,pos):
            pygame.sprite.Sprite.__init__(self)
            self.image=image
            self.rect=self.image.get_rect()
            self.rect.x=pos[0]
            self.rect.y=pos[1]

    class Bush(pygame.sprite.Sprite):
        def __init__(self,image,pos):
            pygame.sprite.Sprite.__init__(self)
            self.image=image
            self.rect=self.image.get_rect()
            self.rect.x=pos[0]
            self.rect.y=pos[1]

    class Enemy(pygame.sprite.Sprite):
        def __init__(self,image,pos):
            pygame.sprite.Sprite.__init__(self)
            self.image=image
            self.rect=self.image.get_rect()
            self.rect.x=pos[0]
            self.rect.y=pos[1]

    class Flag(pygame.sprite.Sprite):
        def __init__(self,image,pos):
            pygame.sprite.Sprite.__init__(self)
            self.image=image
            self.rect=self.image.get_rect()
            self.rect.x=pos[0]
            self.rect.y=pos[1]

    class Player(pygame.sprite.Sprite):
        def __init__(self,image,pos):
            pygame.sprite.Sprite.__init__(self)
            self.image=image
            self.rect=self.image.get_rect()
            self.rect.x=pos[0]
            self.rect.y=pos[1]



























def drawmaps(nameFile):
    maps=[]
    source ='game lvl/' + str(nameFile)
    with open(source,'r') as file:
        for i in range(0,len(maps)):
            maps.append(file.readline().replace('\n','').split('','')[0:-1])
    pos = [0,0]
    for i in range (0,len(maps)):
        pos[1]=i*48
        for j in range(0,len(maps[0])):
            pos[0]=48*j

brickg=pygame.sprite.Group()
waterg=pygame.sprite.Group()
flagg=pygame.sprite.Group()
playerg=pygame.sprite.Group()
enemyg=pygame.sprite.Group()
irong=pygame.sprite.Group()
bushg=pygame.sprite.Group()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if lvl=='game':
        glvl()
        clock.tick(FPS)