import pygame
pygame.init()

import config as cg
from imageHandler import ImageHandler

#HANDLERS
imageHandler = ImageHandler()

#IMAGES
dinoRunningImage = imageHandler.load_scaleKeepRatio_transparency("Images/dino.png", height=cg.dinoHeight)
cg.runningDinoHeight = dinoRunningImage.get_height()

dinoDuckingImage = imageHandler.load_scaleKeepRatio_transparency("Images/duckingDino.png", height=cg.dinoHeight//2)
cg.duckingDinoHeight = dinoDuckingImage.get_height()

dinoImage = dinoRunningImage
cg.dinoWidth, cg.dinoHeight = dinoImage.get_width(), dinoImage.get_height()

lastTime = 0
currentTime = pygame.time.get_ticks()
class CharacterManager:
    def drawDino(self):
        cg.screen.blit(dinoImage, cg.dinoPos)

    def updateDinoPos(self):
        global lastTime
        global currentTime

        if not cg.dinoPos:
            cg.dinoPos = (20, cg.SCREEN_HEIGHT-cg.groundHeight-cg.dinoHeight)

        currentTime = pygame.time.get_ticks()
        if cg.jumping and currentTime-lastTime>=50:
            cg.dinoPos = (cg.dinoPos[0], cg.dinoPos[1] + cg.dinoVel[1])
            
            cg.dinoVel = (cg.dinoVel[0], cg.dinoVel[1] + cg.gravity)
            
            if cg.dinoPos[1] >= cg.SCREEN_HEIGHT - cg.groundHeight - cg.dinoHeight:
                cg.dinoPos = (cg.dinoPos[0], cg.SCREEN_HEIGHT - cg.groundHeight - cg.dinoHeight)
                cg.jumping = False
                cg.dinoVel = (cg.dinoVel[0], 0)

            lastTime = currentTime

        elif cg.ducking:
            cg.dinoPos = (20, cg.SCREEN_HEIGHT-cg.groundHeight-cg.dinoHeight)

        elif cg.ducking == cg.jumping == False:
            cg.dinoPos = (20, cg.SCREEN_HEIGHT-cg.groundHeight-cg.dinoHeight)

    def updateDinoImage(self):
        global dinoImage

        if cg.ducking:
            dinoImage = dinoDuckingImage

            cg.dinoWidth, cg.dinoHeight = dinoImage.get_width(), dinoImage.get_height()
        else:
            dinoImage = dinoRunningImage

            cg.dinoWidth, cg.dinoHeight = dinoImage.get_width(), dinoImage.get_height()

    def checkCollision(self):
        for cactus in cg.cacti:
            dinoMask = pygame.mask.from_surface(dinoImage)
            cactusMask = pygame.mask.from_surface(cg.cactusImage)

            offset = (cactus.pos[0] - cg.dinoPos[0], cactus.pos[1] - cg.dinoPos[1])
            collision = dinoMask.overlap(cactusMask, offset)

            if collision:
                return True
            
        for bird in cg.birds:
            dinoMask = pygame.mask.from_surface(dinoImage)
            birdMask = pygame.mask.from_surface(cg.birdImage)

            offset = (bird.pos[0] - cg.dinoPos[0], bird.pos[1] - cg.dinoPos[1])
            collision = dinoMask.overlap(birdMask, offset)

            if collision:
                return True

        return False