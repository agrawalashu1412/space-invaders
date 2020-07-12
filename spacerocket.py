import pygame
import random
import math
from pygame import mixer
#initialize the pygame
pygame.init()



# initialize the music
pygame.mixer.init()

#create the screen
screen=pygame.display.set_mode((800,600))

#backround image
background=pygame.image.load("2352.jpg")
background = pygame.transform.scale(background, (800, 600))

# background music
# musicback= mixer.music.load("backy.mp3")
# musicback=  mixer.music.play(-1)




#Title and Icon

pygame.display.set_caption("Space Invader")
titleicon=pygame.image.load("spaceship.png")
pygame.display.set_icon(titleicon)



#player
playerImg=pygame.image.load("space-invaders.png")
playerX=350
playerY=500
playerX_change=0



#Enemy
alienImg=[]
alienX=[]
alienY=[]
alienX_change=[]
alienY_change=[]
num_of_aliens=7

for i in range(num_of_aliens):
    alienImg.append(pygame.image.load("alien.png"))
    alienX.append(random.randint(0,700))
    alienY.append(random.randint(50,200))
    alienX_change.append(5)
    alienY_change.append(50)




#bullet

# Ready= you cannot see the bullet on the screen
# fire=the bullet is currently moving


bulletImg=pygame.image.load("bulletfire.png")
bulletX=0
bulletY=500
bulletX_change=0
bulletY_change=6
bullet_state="ready"


# score

score_value=0
font=pygame.font.Font("freesansbold.ttf",32)

textX=10
textY=10



# game over text

over_font=pygame.font.Font("freesansbold.ttf",62)





def show_score(x,y):
    score=font.render("score :" + str(score_value),True,(255,0,0))
    screen.blit(score,(x,y))


def game_over():
    game_over=over_font.render("GAME OVER",True,(255,0,0))
    screen.blit(game_over, (210, 260))





def player(x,y):
    screen.blit(playerImg,(x,y))

def alien(x,y,i):
    screen.blit(alienImg[i],(x,y))


def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10 ))



def isCollision(alienX,alienY,bulletX,bulletY):
    distance= math.sqrt((math.pow(alienX - bulletX ,2)) +(math.pow(alienY - bulletY,2)))
    if distance<27:
        return True
    else:
        return False





#game loop
running =True
while running:
    # pygame.mixer.music.load("backy.mp3")
    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.set_volume(0.7)

    # pygame.mixer.music.load("backy.mp3")
    # pygame.mixer.music.play(-1)
    # RGB color=(RED,green,blue)
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RETURN:


        if event.type == pygame.QUIT:
                running=False

        # background music


        # if keystroke is pressed check whether its right or left
        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_LEFT:
                playerX_change=-4
            if event.key==pygame.K_RIGHT:
                playerX_change= 4

            if event.key == pygame.K_SPACE:
                pygame.mixer.music.load("gunsound.mp3")
                pygame.mixer.music.play()
                if bullet_state is "ready":

                    #get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)

        if event.type==pygame.KEYUP:
            if event.key== pygame.K_LEFT or event.key== pygame.K_RIGHT:

                playerX_change=0

#checking for the boundries of spaceship so it cannot move outside of the window
    playerX +=playerX_change
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736

 #checking for the boundries of alien so it can move after striking to the boundries
    for i in range(num_of_aliens):

        # game_over
        if alienY[i] >440:
            for j in range(num_of_aliens):
                alienY[j]=2000
            game_over()
            break


        alienX[i] += alienX_change[i]
        if alienX[i]<=0:
            alienX_change[i]=2.5
            alienY[i] += alienY_change[i]
        elif alienX[i] >=736:
            alienX_change[i] =-2.5
            alienY[i] += alienY_change[i]

        # collision
        collision = isCollision(alienX[i], alienY[i], bulletX, bulletY)
        if collision:
            pygame.mixer.music.load("exploid.mp3")
            pygame.mixer.music.play()
            bulletY = 500
            bullet_state = "ready"
            score_value += 10
            alienX[i] = random.randint(0, 700)
            alienY[i] = random.randint(50, 200)

        alien(alienX[i], alienY[i],i)



    # bullet Movement
    if bulletY<=0:
        bulletY = 500
        bullet_state= "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change


    player(playerX,playerY)
    show_score(textX,textY)

    pygame.display.update()






