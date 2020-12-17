import pygame   
import math 
import random  
import os 
pygame.init()  

pygame.font.init()
screen=pygame.display.set_mode((700,700))

back=pygame.transform.scale(pygame.image.load(os.path.join("E:\\Python AI\\Pygame\\space\\","1.png")),(700,700)) 
ship=pygame.image.load(os.path.join("E:\\Python AI\\Pygame\\space\\","pixel_ship_yellow.png"))  
lzr=pygame.image.load(os.path.join("E:\\Python AI\\Pygame\\space\\","pixel_laser_yellow.png"))

time=pygame.time.Clock()

enemy=[pygame.image.load(os.path.join("E:\\Python AI\\Pygame\\space\\","pixel_ship_blue_small.png")),
pygame.image.load(os.path.join("E:\\Python AI\\Pygame\\space\\","pixel_ship_green_small.png")),pygame.image.load(os.path.join("E:\\Python AI\\Pygame\\space\\","pixel_ship_red_small.png")),
pygame.image.load(os.path.join("E:\\Python AI\\Pygame\\space\\","pixel_ship_green_small.png")),pygame.image.load(os.path.join("E:\\Python AI\\Pygame\\space\\","pixel_ship_blue_small.png"))]  

laser=[pygame.image.load(os.path.join("E:\\Python AI\\Pygame\\space\\","pixel_laser_blue.png")),
pygame.image.load(os.path.join("E:\\Python AI\\Pygame\\space\\","pixel_laser_green.png")),pygame.image.load(os.path.join("E:\\Python AI\\Pygame\\space\\","pixel_laser_green.png")),
pygame.image.load(os.path.join("E:\\Python AI\\Pygame\\space\\","pixel_laser_red.png")),pygame.image.load(os.path.join("E:\\Python AI\\Pygame\\space\\","pixel_laser_blue.png"))] 

pos=[[random.randint(10,300),random.randint(-90,-30)],[random.randint(350,450),random.randint(-50,-30)],[random.randint(500,625),random.randint(-120,-60)],
     [random.randint(10,300),random.randint(-45,-10)],[random.randint(470,625),random.randint(-80,-40)]] 

enemylzr=[[pos[0][0],pos[0][1]],[pos[1][0],pos[1][1]],[pos[2][0],pos[2][1]],[pos[3][0],pos[3][1]],[pos[4][0],pos[4][1]]] 
laseersnd=pygame.mixer.Sound(os.path.join("E:\\Python AI\\Pygame\\space\\","laser.mp3"))
score_sound=pygame.mixer.Sound(os.path.join("E:\\Python AI\\Pygame\\space\\","level.wav")) 
shipX=300 
shipY=550 
run=True  
lzrX,lzrY,state,change=shipX,shipY+6,"ready",0
width=ship.get_width() 

over=pygame.font.Font("freesansbold.ttf",64) 
g_over=over.render('GAME OVER',1,(255,255,255))  
Score=0
dis=pygame.font.Font("freesansbold.ttf",25) 
def reset(): 
    global lzrX,lzrY,state,Score,change
    lzrX=shipX
    lzrY=shipY+6 
    state="ready" 
    Score+=1
    score_sound.play()
    change=0

while run:  
    s_r=dis.render("Score:"+str(Score),1,(255,255,255)) 
    for j in range(len(pos)): 
        if math.sqrt(math.pow((pos[j][0]-shipX),2)+math.pow((pos[j][1]-shipY),2))<50: 
            width=0

    health=[shipX,(shipY+ship.get_height()+12),(width-5),10] 
    time.tick(70) 

    screen.fill((0,0,0))
    screen.blit(back,(0,0)) 
    screen.blit(ship,(shipX,shipY))
    screen.blit(lzr,(lzrX,lzrY)) 
    screen.blit(s_r,(5,5)) 
    for i in range(len(pos)): 
        screen.blit(enemy[i],pos[i])
    
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            run=False   

    press=pygame.key.get_pressed() 
    if (press[pygame.K_LEFT] or press[pygame.K_a]) and shipX>4: 
        shipX+=-6
    if (press[pygame.K_RIGHT] or press[pygame.K_d])and shipX<600: 
        shipX+=6
    if (press[pygame.K_UP] or press[pygame.K_w]) and shipY>400: 
        shipY+=-6
    if (press[pygame.K_DOWN] or press[pygame.K_s]) and shipY<560: 
        shipY+=6  

    if press[pygame.K_SPACE]: 
        change=7.6
        laseersnd.play()
        state="fire"
    if lzrY<5: 
        lzrX=shipX
        lzrY=shipY+6 
        state="ready"
        change=0  
    if state=="ready": 
        lzrX=shipX 
        lzrY=shipY  

    if math.sqrt(math.pow((pos[0][0]-lzrX),2)+math.pow((pos[0][1]-lzrY),2))<30: 
            reset() 
            pos[0][0],pos[0][1]=random.randint(350,450),random.randint(-30,-10)

    elif math.sqrt(math.pow((pos[1][0]-lzrX),2)+math.pow((pos[1][1]-lzrY),2))<30: 
            reset() 
            pos[1][0],pos[1][1]=random.randint(20,90),random.randint(-30,-5)

    elif math.sqrt(math.pow((pos[2][0]-lzrX),2)+math.pow((pos[2][1]-lzrY),2))<30:
            reset()
            pos[2][0],pos[2][1]=random.randint(500,625),random.randint(-121,-60)

    elif math.sqrt(math.pow((pos[3][0]-lzrX),2)+math.pow((pos[3][1]-lzrY),2))<30: 
            reset()
            pos[3][0],pos[3][1]=random.randint(50,100),random.randint(-10,0)

    elif math.sqrt(math.pow((pos[4][0]-lzrX),2)+math.pow((pos[4][1]-lzrY),2))<30: 
            reset()
            pos[4][0],pos[4][1]=random.randint(10,300),random.randint(-90,-30)

    if width<=5: 
        screen.blit(g_over,(150,350)) 
        run=False 

    for h in range(len(enemylzr)): 
        screen.blit(laser[h],enemylzr[h])

    for i in range(len(pos)): 
        if pos[i][1]>710: 
            pos[i][1]=random.randint(-100,-20) 
            pos[i][0]=random.randint(10,650) 
        else: 
            pos[i][1]+=3  

    for u in range(len(enemylzr)): 
        if math.sqrt(math.pow((enemylzr[u][0]-shipX),2)+math.pow((enemylzr[u][1]-shipY),2))<35: 
            enemylzr[u][0],enemylzr[u][1]=pos[u] 
            width-=12 
        elif enemylzr[u][1]>705: 
            enemylzr[u][0],enemylzr[u][1]=pos[u] 
        else:
            enemylzr[u][1]+=random.uniform(4,6)   
       
    lzrY-=change
    pygame.draw.rect(screen,[0,255,0],health)
    pygame.display.flip()  
    pygame.display.update()