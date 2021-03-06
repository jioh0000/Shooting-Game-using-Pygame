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

bulletSound = pygame.mixer.Sound("source/bullet.mp3")
hitSound = pygame.mixer.Sound("source/hit.mp3")
music = pygame.mixer.music.load("source/music.mp3")

pygame.mixer.music.play(-1) #Infinite Loop the music


class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 20, self.y, 28, 60) #top left x, top left y, width, height of the hitbox

    def move(self, win):
        if self.walkCount + 1 <= 27:
            self.walkCount = 0
        
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1

            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1

        else:
            if self.right:
                win.blit(walkRight[0], (self.x,self.y))
            else:
                win.blit(walkLeft[0], (self.x,self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2) #2 = borderness

    def hit(self):
        self.x = 60
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-10', 1, (255,0,0))
        win.blit(text, (250 - (text.get_width()/2), 200))
        pygame.display.update()

        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()


class Enenmy(object):
    walkRight = [pygame.image.load('source/R1E.png'), pygame.image.load('source/R2E.png'), pygame.image.load('source/R3E.png'), 
    pygame.image.load('source/R4E.png'), pygame.image.load('source/R5E.png'), pygame.image.load('source/R6E.png'), 
    pygame.image.load('source/R7E.png'), pygame.image.load('source/R8E.png'), pygame.image.load('source/R9E.png'),
    pygame.image.load('source/R10E.png'), pygame.image.load('source/R11E.png')]

    walkLeft = [pygame.image.load('source/L1E.png'), pygame.image.load('source/L2E.png'), pygame.image.load('source/L3E.png'), 
    pygame.image.load('source/L4E.png'), pygame.image.load('source/L5E.png'), pygame.image.load('source/L6E.png'), 
    pygame.image.load('source/L7E.png'), pygame.image.load('source/L8E.png'), pygame.image.load('source/L9E.png'),
    pygame.image.load('source/L10E.png'), pygame.image.load('source/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.velocity = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 50
        self.visible = True
    
    def move(self):
        if self.velocity > 0: #if right
            if self.x < self.path[1] + self.velocity:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.x += self.velocity
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.velocity:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.x += self.velocity
                self.walkCount = 0

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1>= 33:
                self.walkCount = 0 
            if self.velocity > 0:
                win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            #Health Bar
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            #Health Bar Background
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, (50 - self.health), 10))

            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print("hit")

def redrawGameWindow():
    win.blit(bg, (0,0))
    haejeok.move(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    text = font.render("Score: " + str(score), 1, (0,0,0))
    win.blit(text, (320,10))
    pygame.display.update()

haejeok = Player(200, 410, 64, 64)
goblin = Enenmy(100, 410, 64, 64, 300)
bullets = []
run = True
shootLoop = 0
score = 0
font = pygame.font.SysFont("comicsans", 30, True)

while run:
    clock.tick(27)

    if haejeok.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and haejeok.hitbox[1] + haejeok.hitbox[3] > goblin.hitbox[1]:
        if haejeok.hitbox[0] + haejeok[2] > goblin.hitbox[0] and haejeok.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
            haejeok.hit()
            score -= 10

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                hitSound.play()
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.velocity

        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and shootLoop == 0:
        bulletSound.play()
        if haejeok.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(Projectile(round(haejeok.x + haejeok.width // 2), round(haejeok.y + haejeok.height // 2),
            6, (0,0,0), facing))

    if keys[pygame.K_LEFT] and haejeok.x > haejeok.velocity:
        haejeok.x -= haejeok.velocity
        haejeok.left = True
        haejeok.right = False
        haejeok.standing = False

    elif keys[pygame.K_RIGHT] and haejeok.x < 500 - haejeok.velocity - haejeok.width:
        haejeok.x += haejeok.velocity
        haejeok.left = False
        haejeok.right = True
        haejeok.standing = False

    else:
        haejeok.walkCount = 0
        haejeok.standing = True
    
    if not(haejeok.isJump):
        #if keys[pygame.K_UP] and y > velocity:
        #    y -= velocity

        #if keys[pygame.K_DOWN] and y < 500 - velocity - height:
        #    y += velocity
        
        if keys[pygame.K_SPACE]:
            haejeok.isJump = True
            haejeok.right = False
            haejeok.left = False
            haejeok.walkCount = 0
    
    else:
        if haejeok.jumpCount >= -10:
            neg = 1
            if haejeok.jumpCount < 0:
                neg = -1
            haejeok.y -= (haejeok.jumpCount * abs(haejeok.jumpCount)*0.3)
            haejeok.jumpCount -= 1
        else:
            haejeok.jumpCount = 10
            haejeok.isJump = False

    redrawGameWindow()

pygame.quit()
