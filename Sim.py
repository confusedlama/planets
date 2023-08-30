from mainPlanet import Dynamic, Planet
from PlanetGui import Planet_Gui
import time
import os
import platform

clear_commands = {
            "Windows": "cls",
            "Linux": "clear"
        }

dyn = Dynamic(Planet(1, 10, 10, 5, 0), Planet(1, 100, 100, 0, 5), 100, 0.1)
gui = Planet_Gui(102, 53)

gui.planets = dyn.planets

try:
    while True:
        gui.update_frame()
        dyn.step()
        time.sleep(0.5)
except KeyboardInterrupt:
    os.system(clear_commands[platform.system()])