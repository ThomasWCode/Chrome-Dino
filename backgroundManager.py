import pygame
import random
pygame.init()

import config as cg
from imageHandler import ImageHandler

#HANDLERS
imageHandler = ImageHandler()

#COLOURS
BLACK = (0, 0, 0)
SAND_COLOUR = (255 ,226, 156)

#FONTS
normalDistanceLabelFont = pygame.font.Font(None, 30)
bigDistanceLabelFont = pygame.font.Font(None, 60)

#IMAGES
skyImage = imageHandler.load_scale("Images/sky.jpg", (cg.SCREEN_WIDTH, cg.SCREEN_HEIGHT))

cg.cactusImage = imageHandler.load_scaleKeepRatio_transparency("Images/catci.png", height=cg.dinoHeight+20)
cg.cactusWidth, cg.cactusHeight = cg.cactusImage.get_width(), cg.cactusImage.get_height()

cg.birdImage = imageHandler.load_scaleKeepRatio_transparency("Images/bird.png", height=cg.dinoHeight//3)
cg.birdWidth, cg.birdHeight = cg.birdImage.get_width(), cg.birdImage.get_height()

#RECTS
groundRect = pygame.rect.Rect(0, cg.SCREEN_HEIGHT-cg.groundHeight, cg.SCREEN_WIDTH, cg.groundHeight)

class Cacti:
    def __init__(self, type, pos):
        self.type = type
        self.pos = pos

class Bird:
    def __init__(self, pos):
        self.pos = pos

class BackgroundManager:
    def __init__(self):
        self.bigDistantLabel = False
        self.timeSinceBigLabel = 0
        self.frozeDistance = 0

    def drawAll(self):
        self.drawSky()
        self.drawGround()
        self.drawCacti()
        self.drawBirds()
        self.drawDistanceLabel()

    def drawSky(self):
        cg.screen.blit(skyImage, (0, 0))

    def drawGround(self):
        pygame.draw.rect(cg.screen, SAND_COLOUR, groundRect)

    def drawCacti(self):
        for cactus in cg.cacti:
            cg.screen.blit(cg.cactusImage, cactus.pos)

    def drawBirds(self):
        for bird in cg.birds:
            cg.screen.blit(cg.birdImage, bird.pos)

    def drawDistanceLabel(self):
        if cg.distance % 1000 == 0:
            self.bigDistantLabel = True
            self.frozeDistance = cg.distance

        if self.bigDistantLabel:
            self.timeSinceBigLabel += 1

            if self.timeSinceBigLabel <= 20 or 40 <= self.timeSinceBigLabel <= 60 or 80 <= self.timeSinceBigLabel <= 100 or 120 <= self.timeSinceBigLabel <= 140 or 160 <= self.timeSinceBigLabel <= 180:
                label = bigDistanceLabelFont.render(str(self.frozeDistance), True, BLACK)

                cg.screen.blit(label, (0, 0))
        else:
            label = normalDistanceLabelFont.render(str(cg.distance), True, BLACK)

            cg.screen.blit(label, (0, 0))

        if self.timeSinceBigLabel >= 200:
            self.bigDistantLabel = False
            self.timeSinceBigLabel = 0

    def generateNewObstacle(self):
        if random.randint(1, 3) == 3:
            self.generateNewBird()
        else:
            self.generateNewCactus()

    def generateNewCactus(self):
        cactusPos = (cg.SCREEN_WIDTH+cg.cactusWidth, cg.SCREEN_HEIGHT-(cg.groundHeight+cg.cactusHeight))
        cactus = Cacti("small", cactusPos)

        cg.cacti.append(cactus)

    def generateNewBird(self):
        birdPos = (cg.SCREEN_WIDTH+cg.birdWidth, cg.SCREEN_HEIGHT-(cg.groundHeight+cg.runningDinoHeight))
        bird = Bird(birdPos)

        cg.birds.append(bird)

    def updateCactiPos(self):
        for cactus in cg.cacti:
            cactus.pos = (cactus.pos[0]-cg.cactiSpeed, cactus.pos[1])

            if cactus.pos[0]+cg.cactusWidth <= 0:
                cg.cacti.remove(cactus)
                
                self.generateNewObstacle()

                if cg.cactiSpeed >= cg.maxCactiSpeed:
                    cg.cactiSpeed = cg.maxCactiSpeed
                else:
                    cg.cactiSpeed += 0.5

    def updateBirdsPos(self):
        for bird in cg.birds:
            bird.pos = (bird.pos[0]-cg.cactiSpeed, bird.pos[1])

            if bird.pos[0]+cg.cactusWidth <= 0:
                cg.birds.remove(bird)

                self.generateNewObstacle()

                if cg.cactiSpeed >= cg.maxCactiSpeed:
                    cg.cactiSpeed = cg.maxCactiSpeed
                else:
                    cg.cactiSpeed += 0.5