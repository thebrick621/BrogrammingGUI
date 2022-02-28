import pygame
# Initializing Pygame Library
pygame.init()

# Sets the size of the window being drawn
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
