#EXTERNAL IMPORTS
import pygame
pygame.init()

#INTERNAL FILE IMPORTS
import config as cg
cg.screen = pygame.display.set_mode((cg.SCREEN_WIDTH, cg.SCREEN_HEIGHT))

from backgroundManager import BackgroundManager
from characterManager import CharacterManager

#MANAGERS
backgroundManager = BackgroundManager()
characterManager = CharacterManager()

backgroundManager.generateNewCactus()

#COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#FONTS
gameOverFont = pygame.font.Font(None, 60)

def writeGameOverText():
    text = gameOverFont.render("GAME OVER", True, WHITE)
    cg.screen.blit(text, (cg.SCREEN_WIDTH/2-text.get_width()/2, cg.SCREEN_HEIGHT/2-text.get_height()/2))

gameOverBlurringCount = 0
def gameOver():
    global gameOverBlurringCount
    gameOverBlurringCount += 1

    screen_surface = pygame.display.get_surface()

    scaled_surface = pygame.transform.smoothscale(screen_surface, (100, 75))
    blurred_surface = pygame.transform.smoothscale(scaled_surface, (cg.SCREEN_WIDTH, cg.SCREEN_HEIGHT))
    cg.screen.blit(blurred_surface, (0, 0))

clock = pygame.time.Clock()
running = True
while running:
    if not cg.gameOver:
        cg.screen.fill(WHITE)
        
        cg.distance += int(cg.cactiSpeed//8)
        
        backgroundManager.updateCactiPos()
        backgroundManager.updateBirdsPos()
        characterManager.updateDinoPos()
        characterManager.updateDinoImage()
        collision = characterManager.checkCollision()

        backgroundManager.drawAll()
        characterManager.drawDino()

        if collision:
            cg.gameOver = True

    else:
        if gameOverBlurringCount < 225:
            gameOver()
        else:
            writeGameOverText()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if not cg.gameOver:
                if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE:
                    if cg.jumping == cg.ducking == False:
                        cg.jumping = True

                        cg.dinoVel = (cg.dinoVel[0], -cg.jumpStrength)
                elif event.key == pygame.K_DOWN:
                    if cg.jumping == cg.ducking == False:
                        cg.ducking = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if cg.ducking:
                    cg.ducking = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()