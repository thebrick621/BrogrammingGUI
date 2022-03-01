import pygame
# Initializing Pygame Library
pygame.init()

# Sets the size of the window being drawn
display_height = 1280
display_width = 720
screen = pygame.display.set_mode((display_height, display_width))

# Generic Variables Establishment
clock = pygame.time.Clock()

# Image Loading Index
icon = pygame.image.load('icon.png')
bedroom_back = pygame.image.load('bedroom_background.png')
charsprite = pygame.image.load('char_sprite.png')

# Color Codes
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
magenta = (255,0,255)
yellow = (255,255,0)

# Title & Icon Data
pygame.display.set_caption("Brogramming")
pygame.display.set_icon(icon)

# Load Character Img
def player(x,y):
    screen.blit(charsprite, (x,y))

player_xloc = (35)
player_yloc = (100)

# Main Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fills the Screen W/ color
    screen.fill(white)
    screen.blit(bedroom_back, (0,0))

    # Places Player Sprite on screen
    player(player_xloc,player_yloc)


    # Updates Screen & Sets Framerate
    pygame.display.update()
    clock.tick(60)