import sys
import os

# Suppress the "hello from the pygame community" message
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame
import random
import numpy as np
from helpers import *
from pygame.locals import *


# Function to parse color input from user (HEX)
def parse_color_input(color_input):
    while True:
        try:
            color_input = color_input.strip().lstrip("#")
            if len(color_input) != 6:
                raise ValueError
            return tuple(int(color_input[i : i + 2], 16) for i in (0, 2, 4))
        except ValueError:
            print(
                "\n\033[1;31;40m❌ Invalid color format. Please enter colors as HEX (#RRGGBB).\033[1;37;40m"
            )
            color_input = input(
                "\n\033[1;36;40m❌ Please enter a valid HEX color (format: #RRGGBB): \033[1;37;40m"
            ).strip()


# Function to get random color
def get_random_color():
    return tuple(random.randint(0, 255) for _ in range(3))


# Ask the user if they want to insert custom colors
while True:
    custom_colors = (
        input(
            "\n\033[1;36;40m🎨 Do you want to insert custom colors? (yes/no): \033[1;37;40m"
        )
        .strip()
        .lower()
    )
    if custom_colors in ["yes", "no"]:
        break
    else:
        print(
            "\n\033[1;31;40m❌ Invalid input. Please enter 'yes' or 'no'.\033[1;37;40m"
        )

if custom_colors == "yes":
    # Get user input for colors
    alive_color_input = input(
        "\n\033[1;32;40m🌹 Enter the HEX value for 'alive' color (format: #HEX): \033[1;37;40m"
    )
    dead_color_input = input(
        "\033[1;33;40m🥀 Enter the HEX value for 'dead' color (format: #HEX): \033[1;37;40m"
    )

    COLOR_ALIVE = parse_color_input(alive_color_input)
    COLOR_DEAD = parse_color_input(dead_color_input)
else:
    COLOR_ALIVE = get_random_color()
    COLOR_DEAD = get_random_color()

pygame.init()

INT = 100
INT_SQ = INT * INT

SIZE = 5

screen = pygame.display.set_mode((80 + INT * SIZE, 160 + INT * SIZE))
pygame.display.set_caption("")  # Remove the window title
running = True
clock = pygame.time.Clock()

# Initialize Status Array - Making an array with half dead and half alive
zero = np.zeros((INT, INT // 2), dtype=int)
one = np.ones((INT, INT // 2), dtype=int)
current_status_array = np.concatenate((zero, one), axis=1)

# Defining font style and size
font = pygame.font.Font("freesansbold.ttf", 32)

text_title = font.render("Pixels Fighting", True, (255, 255, 255), (0, 0, 0))
textRectTitle = text_title.get_rect()
textRectTitle.center = (40 + INT * SIZE / 2, 40)


# Defining Box Class
class Box:
    def __init__(self, x, y, alive):
        self.x = x
        self.y = y
        self.alive = alive
        self.surf = pygame.Surface((SIZE, SIZE))
        self.rect = (40 + SIZE * self.y, 100 + SIZE * self.x)

    def assign_color(self):
        if self.alive == 0:
            self.surf.fill(COLOR_DEAD)
        else:
            self.surf.fill(COLOR_ALIVE)
        screen.blit(self.surf, self.rect)

    def update(self):
        self.alive = current_status_array[self.x][self.y]
        self.assign_color()


boxes = []

for i in range(INT_SQ):
    x = i // INT
    y = i % INT
    boxes.append(Box(x, y, current_status_array[x][y]))

# Main python loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_status_array = UpdateArray(current_status_array, INT)
    for box in boxes:
        box.update()

    screen.blit(text_title, textRectTitle)

    pygame.display.update()

    # Using clock.tick() to control frame rate instead of time.sleep
    clock.tick(240)  # Run the loop at 240 frames per second for faster updates
