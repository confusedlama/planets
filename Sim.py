from mainPlanet import Dynamic, Planet
from PlanetGui import Planet_Gui
import time
import os
import platform

clear_commands = {
            "Windows": "cls",
            "Linux": "clear"
        }

dyn = Dynamic(Planet(1, 10, 10, 0, 0), Planet(1, 500, 100, 0, 0), 100, 0.1)
gui = Planet_Gui(102, 53)

gui.planets = dyn.planets
# print(gui.planets[0].x)

try:
    while True:
        gui.update_frame()
        dyn.step()
        # print(print(gui.planets[0].x))
        # print(print(gui.planets[0].y))
        time.sleep(0.25)
except KeyboardInterrupt:
    os.system(clear_commands[platform.system()])