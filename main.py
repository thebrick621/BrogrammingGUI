import pygame
# Initializing Pygame Library
pygame.init()

# Sets the size of the window being drawn
screen = pygame.display.set_mode((1280, 720))

# Title & Icon Data
pygame.display.set_caption("Brogramming")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False