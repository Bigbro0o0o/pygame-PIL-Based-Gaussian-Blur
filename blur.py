import pygame
from PIL import Image, ImageFilter

screen = pygame.display.set_mode((1000, 1000))

def blurSurface(surface, blurSize):    
    temporarySurf = surface
    surfaceStr = pygame.image.tostring(temporarySurf, "RGBA") #Convert the surface to a string
    PILDecode = Image.frombytes("RGBA", (temporarySurf.get_size()[0],temporarySurf.get_size()[1]), surfaceStr, 'raw') #Decode the pygame string and make it back into an image
    blurredPIL = PILDecode.filter(ImageFilter.GaussianBlur(radius = blurSize)) #Blur the Image
    blurredImage = pygame.image.fromstring(blurredPIL.tobytes(), blurredPIL.size, blurredPIL.mode) #Make the PIL blurred image back into a image
    return blurredImage

running = True
  
while running:
    pygame.time.Clock().tick(60)
    screen.fill((255,255,255))
    
    blured = blurSurface(screen, 5)
    screen.blit(blured, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
