import pygame
pygame.init()

class ImageHandler:
    def load(self, imagePath):
        return pygame.image.load(imagePath)
    
    def load_scale(self, imagePath, size):
        image = pygame.image.load(imagePath)
        image = pygame.transform.scale(image, size)

        return image
    
    def load_scaleKeepRatio(self, imagePath, height=None, width=None):
        image = pygame.image.load(imagePath)

        originalWidth, originalHeight = image.get_size()
        aspectRatio = originalWidth / originalHeight

        if height:
            newWidth = int(height * aspectRatio)

            image = pygame.transform.scale(image, (newWidth, height))
        else:
            newHeight = int(width * aspectRatio)

            image = pygame.transform.scale(image, (width, newHeight))

        return image
    
    def load_transparency(self, imagePath):
        return pygame.image.load(imagePath).convert_alpha()
    
    def load_scale_transparency(self, imagePath, size):
        image = pygame.image.load(imagePath).convert_alpha()
        image = pygame.transform.scale(image, size)

        return image
    
    def load_scaleKeepRatio_transparency(self, imagePath, height=None, width=None):
        image = pygame.image.load(imagePath).convert_alpha()

        originalWidth, originalHeight = image.get_size()
        aspectRatio = originalWidth / originalHeight

        if height:
            newWidth = int(height * aspectRatio)

            image = pygame.transform.scale(image, (newWidth, height))
        else:
            newHeight = int(width * aspectRatio)

            image = pygame.transform.scale(image, (width, newHeight))

        return image