import pygame
from mainPlanet import Dynamic, Planet
import copy


# infoObject = pygame.display.Info()
ur_dyn = Dynamic(Planet(1, 200, 300, 5, 10), Planet(1, 1100, 600, 10, 5), 100, 0.001)
dyn = copy.deepcopy(ur_dyn)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1800, 900))
clock = pygame.time.Clock()
running = True

background_image = pygame.image.load("Background.jpg")
earth = pygame.image.load("earth.png")
mars = pygame.image.load("mars.png")

timer = 30

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and timer == 30:
            dyn = copy.deepcopy(ur_dyn)
            timer = 0

    if timer < 30:
        timer += 1
        
    # fill the screen with a color to wipe away anything from last frame
    screen.blit(background_image, (0, 0))

    # RENDER YOUR GAME HERE
    # pygame.draw.circle(screen, (255, 0, 0), (dyn.planets[0].x, dyn.planets[0].y), 10)
    # pygame.draw.circle(screen, (0, 0, 255), (dyn.planets[1].x, dyn.planets[1].y), 10)
    screen.blit(earth, (dyn.planets[0].x-15, dyn.planets[0].y-15))
    screen.blit(mars, (dyn.planets[1].x-15, dyn.planets[1].y-15))
    dyn.step()


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

pygame.quit()