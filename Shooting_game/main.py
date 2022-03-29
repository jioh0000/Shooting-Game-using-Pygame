import pygame

pygame.init() #Game Start

win = pygame.display.set_mode((500,480))
pygame.display.set_caption("Wind's World Game")

walkRight = [pygame.image.load('source/R1.png'), pygame.image.load('source/R2.png'), pygame.image.load('source/R3.png'), 
pygame.image.load('source/R4.png'), pygame.image.load('source/R5.png'), pygame.image.load('source/R6.png'), 
pygame.image.load('source/R7.png'), pygame.image.load('source/R8.png'), pygame.image.load('source/R9.png')]

walkLeft = [pygame.image.load('source/L1.png'), pygame.image.load('source/L2.png'), pygame.image.load('source/L3.png'), 
pygame.image.load('source/L4.png'), pygame.image.load('source/L5.png'), pygame.image.load('source/L6.png'), 
pygame.image.load('source/L7.png'), pygame.image.load('source/L8.png'), pygame.image.load('source/L9.png')]

bg = pygame.image.load('source/bg.jpg')
char = pygame.image.load('source/standing.png')

clock = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
velocity = 10

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1

    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1

    else:
        win.blit(char, (x,y))

    pygame.display.update()


run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - velocity - width:
        x += velocity
        left = False
        right = True

    else:
        right = False
        left = False
        walkCount = 0
    
    if not(isJump):
        #if keys[pygame.K_UP] and y > velocity:
        #    y -= velocity

        #if keys[pygame.K_DOWN] and y < 500 - velocity - height:
        #    y += velocity
        
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount * abs(jumpCount)*0.3)
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    redrawGameWindow()

pygame.quit()
