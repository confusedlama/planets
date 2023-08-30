from mainPlanet import Planet
import time
import os
import platform

clear_commands = {
            "Windows": "cls",
            "Linux": "clear"
        }


class Planet_Gui:
    def __init__(self, x, y, scale = 2):
        self.x = x
        self.y = y
        self.planets = []
        self.i = 0
        self.scale = scale

        self.empty_frame = ""
        for i in range(y):
            for j in range(x):
                self.empty_frame += "░░"
            self.empty_frame += "\n"

    
    def generate_frame(self):
        frame = self.empty_frame

        for planet in self.planets:
            if planet.x >= 0 and planet.x < self.x and planet.y >= 0 and planet.y < self.y:
                frame = frame[:self.planet_to_string_coords(planet.x, planet.y)] + "▓▓" + frame[self.planet_to_string_coords(planet.x, planet.y)+2:]

        return frame
    
    
    def update_frame(self):
        os.system(clear_commands[platform.system()])
        print(self.generate_frame())


    def planet_to_string_coords(self, x, y):
        return (y // self.scale) * self.x * 2 + (y // self.scale) + (x // self.scale) * 2



move_pattern = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

def make_planet(x, y):
    return Planet(0, x, y, 0, 0)

def move_planet(planet, x, y):
    planet.x = planet.x + x
    planet.y = planet.y + y

try:
    gui = Planet_Gui(102, 53)
    planets = [make_planet(10, 10), make_planet(90, 40)]
    while True:
        for i in range(len(move_pattern)):
            move_planet(planets[0], move_pattern[i][0], move_pattern[i][1])
            move_planet(planets[1], move_pattern[i][0], move_pattern[i][1])
            gui.planets = planets
            gui.generate_frame()
            gui.update_frame()
            time.sleep(0.5)
        
except KeyboardInterrupt:
    os.system(clear_commands[platform.system()])