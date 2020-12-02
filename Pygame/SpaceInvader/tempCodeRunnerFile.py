import pygame as pygame 
import random 
import math 
import time

pygame.init()
pygame.font.init() 
pygame.mixer.init()
screen=pygame.display.set_mode((700,700))  
#loading icons,image of ship,enemy
pygame.display.set_caption("Space Invaders") 
icon=pygame.image.load("Pygame/icon.png")
pygame.display.set_icon(icon)
back_ground=pygame.image.load("Pygame/background.jpg")  
#score
Score=0
level=1
Level=pygame.font.Font("freesansbold.ttf",32)
score=pygame.font.Font('freesansbold.ttf',32) 
g_over=pygame.font.Font("freesansbold.ttf",64)
over=g_over.render("Game Over",1,(255,255,255))
#creating ship
ship=pygame.image.load("Pygame/rocket.png") 
shipX=340 
shipY=620
shipX_change=0
shipY_change=0
#creating enemy
enemy=pygame.image.load("Pygame/enemy.png")
enemyX=random.randint(10,500) 
enemyY=random.randint(10,300) 
enemyX_change=0.9
#Loading bullet ,setting position of bullet
bullet=pygame.image.load("Pygame/bullet.png") 
bulletX=shipX+15 
bulletY=shipY+7
bullet_state="ready"
#enemy_bullet 
e_bullet=pygame.image.load("Pygame/bullet (1).png") 
e_bulletX=enemyX+15
e_bulletY=enemyY+15 
#Loading in sounds 
Warning_=pygame.mixer.Sound("Pygame/mixkit-classic-alarm-995.wav") 
fire=pygame.mixer.Sound('Pygame/shoot.wav')

enemykilled=pygame.mixer.Sound("Pygame/invaderkilled.wav") 
lll=pygame.mixer.Sound("Pygame/level.wav") 
#Functions
def get_score(): 
    scr=score.render("Score:"+str(Score),1,(255,255,255)) 
    lvl=Level.render("Level:"+str(level),1,(255,255,255))
    screen.blit(scr,(5,5))
    screen.blit(lvl,(570,5)) 

def draw(): 
    screen.blit(bullet,(bulletX,bulletY))
    screen.blit(ship,(shipX,shipY)) 
    screen.blit(enemy,(enemyX,enemyY)) 
    screen.blit(e_bullet,(e_bulletX,e_bulletY))
    pygame.display.update()  
#variables 
min_score=7
run=True 
b_y=0  
bullet_change=0.5
level_chnge=1 
l=2
#main loop
while run:
    b_dist=math.sqrt(math.pow((e_bulletX-shipX),2)+math.pow((e_bulletY-shipY-20),2))
    dist=math.sqrt(math.pow((enemyX-shipX),2)+math.pow((enemyY-shipY),2))
    bulletdist=math.sqrt(math.pow((enemyX-bulletX),2)+math.pow(((enemyY-enemy.get_height())-bulletY),2))
    screen.fill((0,0,0))
    screen.blit(back_ground,(0,0))
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            run=False
        if event.type==pygame.KEYDOWN: 
            if event.key==pygame.K_LEFT: 
                shipX_change=-1
            if event.key==pygame.K_RIGHT: 
                shipX_change=1
            if event.key==pygame.K_SPACE: 
                fire.play()
                b_y=2
                bullet_state="fire"
        if event.type==pygame.KEYUP: 
            if event.key==pygame.K_RIGHT: 
                shipX_change=0
            if event.key==pygame.K_LEFT: 
                shipX_change=0
            if event.key==pygame.K_SPACE: 
                b_y=2
                bullet_stae="fire"  

    if e_bulletY>700 or e_bulletY<0: 
        e_bulletX=enemyX+15 
        e_bulletY=enemyY+6 

    if enemyX>620: 
        enemyX=620 
        enemyX_change=-0.9
        enemyY+=40
    
    elif enemyX<10: 
        enemyX=10 
        enemyX_change=0.9
        enemyY+=40 

    if level>level_chnge: 
        bullet_change+=0.4
        level_chnge+=2 
    
    if level==l: 
        l+=1
        lll.play()

    if bulletY<3: 
        b_y=0 
        bulletY=shipY+7
        bullet_state="ready" 

    if bullet_state=="ready": 
        bulletX=shipX+15

    if shipX>635: 
        shipX=635 

    elif shipX<5: 
        shipX=5
        
    if dist<150: 
        Warning_.play()

    if dist<50 or b_dist<35: 
        screen.blit(over,((50+over.get_width())//2,300))  
        run=False 

    if bulletdist<60 or (bulletdist+math.sqrt(enemy.get_width()))<60:
       enemykilled.play() 
       Score+=1 
       enemyX=random.randint(10,500) 
       enemyY=random.randint(10,300) 

    if Score>min_score:  
        level+=1 
        min_score+=4 

    e_bulletY+=bullet_change
    shipX+=shipX_change
    enemyX+=enemyX_change 

    get_score() 
    draw()

    bulletY-=b_y 
pygame.quit()
    

