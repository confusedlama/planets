import pygame
from mainPlanet import Dynamic, Planet
import copy


# infoObject = pygame.display.Info()
ur_dyn = Dynamic(Planet(10, 400, 400, 3, -1), Planet(1000, 500,500 ,0 , 0), 100, 0.001)
dyn = copy.deepcopy(ur_dyn)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1800, 900))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    pygame.draw.circle(screen, (255, 0, 0), (dyn.planets[0].x, dyn.planets[0].y), 10)
    pygame.draw.circle(screen, (0, 0, 255), (dyn.planets[1].x, dyn.planets[1].y), 10)
    dyn.step()


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(40)  # limits FPS to 60

pygame.quit()