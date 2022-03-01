import pygame
import time
# Initializing Pygame Library
pygame.init()
pygame.font.init()

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

# Draw rectangles
def draw_rect(x, y, w, h, color):
    pygame.draw.rect(screen, color, [x, y, w, h])


# Places a block of text on the screen in a rect.
def text_objects(text, font):
    textSurface = font.render(text, True, yellow)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont('Roboto.ttf', 55)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_height/2), (display_width/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

# Load Character Img
def player(x,y):
    screen.blit(charsprite, (x,y))

# Intro For Game
def game_intro():
    intro = True


    while intro:

        # For loop is for any EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Dispalys Text
        message_display("When your pizza rolls are done.")

        # Mouse getpos needs to be in loop to constantly refresh
        mouse = pygame.mouse.get_pos()

        # If xPOS plus height is greater than mouse X &
        # If yPOS plus width is greater than mouse Y then you are hovering over rect.

        if 350+100 > mouse[0] > 350 and 450+50 > mouse[1] > 450: # If xPOS plus height is greater than mouse X &
                                            # If yPOS plus width is greater than mouse Y then you are hovering over rect.
            draw_rect(350,450,100,50, blue)
        else:
            draw_rect(350,450,100,50, red)
        
        if 850+100 > mouse[0] > 850 and 450+50 > mouse[1] > 450:
            draw_rect(850,450,100,50, blue)
        else:
            draw_rect(850,450,100,50, green)

        # Updates Screen & Sets Framerate
        pygame.display.update()
        clock.tick(60)       


# Main Game loop
def game_loop():
    player_xloc = (35)
    player_yloc = (100)
    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # If Key gets pressed, do thing
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    draw_rect(600, 370, 100, 100, black)
                    message_display("TEST")

        # Fills the Screen W/ color
        screen.fill(white)
        screen.blit(bedroom_back, (0,0))

        # Places Player Sprite on screen
        player(player_xloc,player_yloc)

        

        # Updates Screen & Sets Framerate
        pygame.display.update()
        clock.tick(60)


# Main Operation Stack
game_intro()
game_loop()
pygame.quit()
quit()




# How to make an ALPHA button. 

# s = pygame.Surface((1000,750), pygame.SRCALPHA)   # per-pixel alpha
# s.fill((255,255,255,128))                         # notice the alpha value in the color
# windowSurface.blit(s, (0,0))