#IMPORTS
import pygame
import os
import random

#INITIALIZE
pygame.init()

#VARIABLES
screen_h = 600
screen_w = 1100
screen = pygame.display.set_mode((screen_w, screen_h))

hehe = [pygame.image.load(os.path.join("Assets/MindBlowon", 'hehe.png')),
        pygame.image.load(os.path.join("Assets/MindBlowon", 'cry.png'))]
sliding = [pygame.image.load(os.path.join("Assets/MindBlowon", 'slide1.png')),
           pygame.image.load(os.path.join("Assets/MindBlowon", 'slide2.png'))]
jumping = [pygame.image.load(os.path.join("Assets/MindBlowon", 'jump.png'))]
small_cactus = [pygame.image.load(os.path.join("Assets/Cactus", 'SmallCactus11.png')),
                pygame.image.load(os.path.join("Assets/Cactus", 'SmallCactus22.png')),
                pygame.image.load(os.path.join("Assets/Cactus", 'SmallCactus33.png'))]
large_cactus = [pygame.image.load(os.path.join("Assets/Cactus", 'LargeCactus11.png')),
                pygame.image.load(os.path.join("Assets/Cactus", 'LargeCactus22.png')),
                pygame.image.load(os.path.join("Assets/Cactus", 'LargeCactus33.png'))]
face = [pygame.image.load(os.path.join("Assets/Face", 'Face1.png')),
        pygame.image.load(os.path.join("Assets/Face", 'Face2.png'))]
thumbs = [pygame.image.load(os.path.join("Assets/Cactus", 'smallThumb.png')),
          pygame.image.load(os.path.join("Assets/Cactus", 'BigThumb.png'))]
cloud = [pygame.image.load(os.path.join("Assets/Other", 'Cloud.png'))]
twohundo = [pygame.image.load(os.path.join("Assets/Other", "200KK.png"))]
BG = [pygame.image.load(os.path.join("Assets/Other", 'Ground.png'))]

class MindBlown:
    x_pos = 80
    y_pos = 315
    y_pos_duck = 340
    jump_VEL = 9.5

    def __init__(self):
        self.run_img = sliding
        self.jump_img = jumping

        self.mb_Run = True
        self.mb_Jump = False

        self.step_index = 0
        self.jump_vel = self.jump_VEL
        self.image = self.run_img[0]
        self.mb_rect = self.image.get_rect()
        self.mb_rect.x = self.x_pos
        self.mb_rect.y = self.y_pos

    def update(self, userInput):
        if self.mb_Run:
            self.run()
        if self.mb_Jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_SPACE] or userInput[pygame.K_w] and not self.mb_Jump:
            self.mb_Jump = True
            self.mb_Run = False
            self.mb_Duck = False
        elif not (self.mb_Jump or userInput[pygame.K_DOWN]):
            self.mb_Run = True
            self.mb_Jump = False
            self.mb_Duck = False

    def run(self):
        self.image = self.run_img[self.step_index//5]
        self.mb_rect = self.image.get_rect()
        self.mb_rect.x = self.x_pos
        self.mb_rect.y = self.y_pos
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img[0]
        if self.mb_Jump:
            self.mb_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.jump_VEL:
            self.mb_Jump = False
            self.jump_vel = self.jump_VEL

    def draw(self, screen):
        screen.blit(self.image, (self.mb_rect.x, self.mb_rect.y))

class Cloud:
    def __init__(self):
        self.x = screen_w + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = cloud[0]
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < - self.width:
            self.x = screen_w + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class TwoHund:
    def __init__(self):
        self.x = screen_w + random.randint(800, 1000)
        self.y = 60
        self.image = twohundo[0]
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class CactiNFrenz:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = screen_w

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < - self.rect.width:
            cactinfren.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)

class SmallCacti(CactiNFrenz):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 325

class BigCacti(CactiNFrenz):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 300

class Thumbs(CactiNFrenz):
    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(image, self.type)
        self.rect.y = 300

class Face(CactiNFrenz):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 240
        self.index = 0

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index//5], self.rect)
        self.index += 1

def main():
    global game_speed, x_pos_bg, y_pos_bg, points, cactinfren
    run = True
    clock = pygame.time.Clock()
    player = MindBlown()
    CLOUD = Cloud()
    TWOHUND = TwoHund()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.SysFont("comicsansms", 20)
    cactinfren = []
    deathCount = 0

    def score():
        global points, game_speed
        points += 0.5
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(int(points)), True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        screen.blit(text, text_rect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG[0].get_width()
        screen.blit(BG[0], (x_pos_bg, y_pos_bg))
        screen.blit(BG[0], (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            screen.blit(BG[0], (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill((240,233,227))
        userInput = pygame.key.get_pressed()

        player.draw(screen)
        player.update(userInput)

        if len(cactinfren) == 0:
            if random.randint(0,3) == 0:
                cactinfren.append(SmallCacti(small_cactus))
            elif random.randint(0,3) == 1:
                cactinfren.append(BigCacti(large_cactus))
            elif random.randint(0,3) == 2:
                cactinfren.append(Face(face))
            elif random.randint(0,3) == 3:
                cactinfren.append(Thumbs(thumbs))

        for element in cactinfren:
            element.draw(screen)
            element.update()
            if player.mb_rect.colliderect(element.rect):
                pygame.time.delay(2000)
                deathCount += 1
                menu(deathCount)

        background()

        CLOUD.draw(screen)
        CLOUD.update()

        TWOHUND.draw(screen)
        TWOHUND.update()

        score()

        clock.tick(40)
        pygame.display.update()

def menu(deathCount):
    global points
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()
        screen.fill((240,233,227))
        font = pygame.font.SysFont("comicsansms", 30)

        if deathCount == 0:
            text = font.render("Press any KEY to start!", True, (0,0,0))
            screen.blit(hehe[0], (screen_w // 2 - 100, screen_h // 2 - 200))
        elif deathCount > 0:
            text = font.render("Press any KEY to restart! ", True, (0, 0, 0))
            score = font.render("Points: " + str(int(points)), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (screen_w // 2, screen_h // 2 + 50)
            screen.blit(score, scoreRect)
            screen.blit(hehe[1], (screen_w // 2 - 100, screen_h // 2 - 200))
        textRect = text.get_rect()
        textRect.center = (screen_w // 2, screen_h // 2 + 20)
        screen.blit(text, textRect)
        pygame.display.update()


menu(deathCount=0)

