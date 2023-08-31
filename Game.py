import pygame
from mainPlanet import Dynamic, Planet


# infoObject = pygame.display.Info()
dyn = Dynamic(Planet(1, 200, 300, 5, 10), Planet(1, 1100, 600, 10, 5), 100, 0.001)

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

    clock.tick(30)  # limits FPS to 60

pygame.quit()