import pygame
import random
import sys
# pygame setup
pygame.init()

def gameloop():
    #sets up the game window, title, & icon
    sheight = 1920/1.25
    swidth = 1080/1.25
    screen = pygame.display.set_mode((sheight, swidth))
    font = pygame.font.SysFont("arial", 30, True)
    
    #sets variables
    global score
    clock = pygame.time.Clock()
    running = True
    dt = 0
    anicount = 0
    anitime = 250
    lastani = 0
    score = 0
    starved = 0
    lastspawn = 0
    spawnlvl = 1000

    #BackgrondImage
    bgimg = pygame.transform.scale(pygame.image.load("background.png"),(sheight,swidth)).convert_alpha()
    manor = pygame.transform.scale(pygame.image.load("Manor.png"),(sheight,swidth)).convert_alpha()

    class cursorc(pygame.sprite.Sprite):
        def __init__(self, list, list2):
            super().__init__()
            self.list = list
            self.list2 = list2
            self.listlen = len(list)
            self.anicount = 0
            self.loopani = 0
            self.mode = "idle"
        def feed(self):
            self.mode = "feed"
        def animate(self):
            self.anicount += 1
            if self.anicount >= self.listlen:
                self.anicount = 0        
            if self.mode == "idle":
                self.image = self.list[0]
                self.image = self.list[self.anicount]
            if self.mode == "feed":
                self.image = self.list2[0]
                self.image = self.list2[self.anicount]
                self.loopani += 1
                if self.loopani == 1:
                    self.mode = "idle"
                    self.loopani = 0

    class friend(pygame.sprite.Sprite):
        def __init__(self, list):
            super().__init__()
            self.listlen = len(list)
            self.anicount = 0
            #self.surface = pygame.Surface((self.rect.width,self.rect.height))
            self.image = list[0]
            self.list = list
            self.hunger = 100
            self.ishungry = False
            self.hungerspd = random.randint(1,5)
            r = random.randint(1,2)
            if list == hunger_imgs:
                self.x = 0
                self.y = 0
            if list == crow_imgs:
                self.x = random.randint(10,1475)
                self.y = random.randrange(50,565)
            if list == spider_imgs:    
                if r == 1:
                    self.x = random.randint(200,720)
                    self.y = random.randint(84,600)
                if r == 2:
                    self.x = random.randint(10,1475)
                    self.y = random.randint(600, 775)
            if list == snake_imgs:
                if r == 1:
                    self.x = random.randint(10,1475)
                    self.y = random.randint(630, 775)
                if r == 2:
                    self.x = random.randint(880,1475)
                    self.y = random.randint(600, 650)
            self.rect = pygame.Rect(self.x, self.y, 80,80)        
        def drawimgSM(self):
            pygame.Surface.blit(screen, pygame.transform.scale(self.image,(80,80)), (self.x,self.y))         
        def hungerimg(self):    
            if self.hunger <= 0:
                pygame.Surface.blit(screen, pygame.transform.scale(pygame.image.load("feedhungry.png").convert_alpha(),(50,50)), (self.x+18,self.y-50))
            if self.hunger > 0:
                pygame.Surface.blit(screen, pygame.transform.scale(pygame.image.load("feed3.png").convert_alpha(),(50,50)), (self.x+18,self.y-50))
            if self.hunger > 25:
                pygame.Surface.blit(screen, pygame.transform.scale(pygame.image.load("feed2.png").convert_alpha(),(50,50)), (self.x+18,self.y-50))
            if self.hunger > 45:
                pygame.Surface.blit(screen, pygame.transform.scale(pygame.image.load("feed1.png").convert_alpha(),(50,50)), (self.x+18,self.y-50))
            if self.hunger > 85:
                pygame.Surface.blit(screen, pygame.transform.scale(pygame.image.load("feedfull.png").convert_alpha(),(50,50)), (self.x+18,self.y-50))
        def resethunger(self):
            self.hunger = 100
            self.ishungry = False
        def animate(self):
            self.anicount += 1         
            if self.anicount >= self.listlen:
                self.anicount = 0        
            self.image = self.list[self.anicount]

    #list setups
    crow_imgs = [pygame.image.load("crow1.png").convert_alpha(),
                pygame.image.load("crow2.png").convert_alpha()]
    spider_imgs = [pygame.image.load("spider1.png").convert_alpha(),
                pygame.image.load("spider2.png").convert_alpha()]
    snake_imgs = [pygame.image.load("snake1.png").convert_alpha(),
                pygame.image.load("snake2.png").convert_alpha()]
    hunger_imgs = [pygame.image.load("feedfull.png").convert_alpha(),
                pygame.image.load("feed1.png").convert_alpha(),
                pygame.image.load("feed2.png").convert_alpha(),
                pygame.image.load("feed3.png").convert_alpha(),
                pygame.image.load("feedhungry.png").convert_alpha()]

    hunger = friend(hunger_imgs)
    friends = []
    friendrects = []
    hungryfriends = []

    #cursor creation
    cursorfeed_imgs = [pygame.image.load("ghostfeed1.png").convert_alpha(),
                pygame.image.load("ghostfeed2.png").convert_alpha(),
                pygame.image.load("ghostfeed3.png").convert_alpha()]
    cursor_imgs = [pygame.image.load("ghostmove1.png").convert_alpha(),
                    pygame.image.load("ghostmove2.png").convert_alpha(),
                    pygame.image.load("ghostmove3.png").convert_alpha()]
    cursor_img = cursorc(cursor_imgs, cursorfeed_imgs)

    while running:
        # check for events and key presses    
        screen.blit(bgimg,(0,0))
        screen.blit(manor,(0,-25))
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False
                sys.exit()
            for animal in friends:
                if animal.rect.collidepoint(pygame.mouse.get_pos()):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if animal.hunger <= 85:
                            cursorc.feed(cursor_img)
                            friend.resethunger(animal)
                            score += 1
                            if animal in hungryfriends:
                                hungryfriends.remove(animal)
                            else: pass
                            
        if pygame.time.get_ticks() - lastspawn > spawnlvl:    
            lastspawn = pygame.time.get_ticks()
            newanimal = random.choice([friend(crow_imgs), friend(spider_imgs), friend(snake_imgs)])
            if pygame.Rect.collidelist(newanimal.rect, friendrects) != -1:
                pass
            else:
                friends.append(newanimal)
                friendrects.append(newanimal.rect)
            if len(friends) > 0:
                spawnlvl = 5000
            if len(friends) > 3:
                spawnlvl = 1000
            if len(friends) > 6:
                spawnlvl = 700
            if len(friends) > 30:
                spawnlvl = 100

        #create a white box behind friends
        # for item in friends:
        #     pygame.draw.rect(screen, "white", item)    
        if pygame.time.get_ticks() - lastani > anitime:
            lastani = pygame.time.get_ticks()
            cursorc.animate(cursor_img)
            cursor = pygame.cursors.Cursor((8,40), cursor_img.image)
            for animal in friends:
                friend.animate(animal)
                animal.hunger -= animal.hungerspd
                if animal.hunger < 0 and not animal.ishungry:
                    animal.ishungry = True
                    hungryfriends.append(animal)   
        pygame.mouse.set_cursor(cursor)

        #put objects on screen
        for animal in friends:
            friend.drawimgSM(animal)
            friend.hungerimg(animal)

        #displays the player's score
        scoretext = font.render("Score: " +str(score), 1, (255,255,255))
        screen.blit(scoretext, (15, 10))   

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000
        if len(hungryfriends) > 5:
            running = False
            gameover()

def main():
    playsound()
    font = pygame.font.SysFont("arial", 80, True)
    startrunning = True

    bgimg = pygame.transform.scale(pygame.image.load("background.png"),(sheight,swidth)).convert_alpha()
    while startrunning:
        screen.blit(bgimg,(0,0))
        titletext = font.render("SPECTRAL MANOR 1.0", 1, (255,255,255))
        screen.blit(titletext, (400, 330))        
        starttext = font.render("Press spacebar to begin.", 1, (255,255,255))
        screen.blit(starttext, (390, 400))
        pygame.display.flip()
        
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                startrunning = False
                break
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                startrunning = False
                gameloop()  

def gameover():
    global score
    gameoverfont = pygame.font.SysFont("arial", 70, True)
    gameoverfontbig = pygame.font.SysFont("arial", 120, True)
    overrunning = True
    bgimg = pygame.transform.scale(pygame.image.load("background.png"),(sheight,swidth)).convert_alpha()
    while overrunning:
        screen.blit(bgimg,(0,0))
        finalscore = score
        gameovertextL1 = gameoverfontbig.render("YOU LOSE!", 1, (255,255,255))
        screen.blit(gameovertextL1, (475, 200))
        gameovertextL1 = gameoverfont.render("5 friends starved!", 1, (255,255,255))
        screen.blit(gameovertextL1, (520, 330))
        gameovertextL2 = gameoverfont.render("Score: " +str(finalscore), 1, (255,255,255))
        screen.blit(gameovertextL2, (635, 400))
        gameovertextL3 = gameoverfont.render("Press spacebar to play again!", 1, (255,255,255))
        screen.blit(gameovertextL3, (380, 630))
        pygame.display.flip()

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                overrunning = False
                break
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                overrunning = False
                gameloop()  

def playsound():
    try:
        pygame.mixer.music.load("BGSound.mp3")
        pygame.mixer.music.play(loops = -1)
    except:
        sys.exit()

#sets up the game window, title, & icon
pygame.display.set_icon(pygame.transform.scale(pygame.image.load("snake1.png"),(75,75)))
pygame.display.set_caption("Spectral Manor 1.0")
sheight = 1920/1.25
swidth = 1080/1.25
screen = pygame.display.set_mode((sheight, swidth))

if __name__ == "__main__":
     main()

pygame.quit()