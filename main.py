import pygame
import time
# Initializing Pygame Library
pygame.init()
pygame.font.init()

# Sets the size of the window being drawn
display_height = 1280
display_width = 720

# Generic Variables Establishment
clock = pygame.time.Clock()
screen = pygame.display.set_mode((display_height, display_width))
smallText = pygame.font.SysFont('Roboto.ttf', 20) # Font & size def.
mediumText = pygame.font.SysFont('Roboto.ttf', 35) # Font & size def.
largeText = pygame.font.SysFont('Roboto.ttf', 50)

# Image Loading Index
icon = pygame.image.load('icon.png')
bedroom_back = pygame.image.load('bedroom_background.png')
charsprite = pygame.image.load('char_sprite.png')
menubuttonimg = pygame.image.load('startmenu_button.png')
menubuttonimg2 = pygame.image.load('startmenu_buttonhi.png')
titleimg = pygame.image.load('title.png')

# Scales assets to fit interaction
smenu_button = pygame.transform.scale(menubuttonimg, (265,223)) ### WHEN RESIZING X AND Y ARE FLIPPED!!!!####
smenu_buttonhi = pygame.transform.scale(menubuttonimg2, (265,223))

# Color Codes
black = (0,0,0)
white = (255,255,255)
green = (0,189,0)
light_green = (0,255,0)
red = (255,0,0)
light_red = (233,85,85)
blue = (0,0,255)
light_blue = (0,102,255)
magenta = (255,0,255)
yellow = (255,255,0)

# Title & Icon Data
pygame.display.set_caption("Brogramming")
pygame.display.set_icon(icon)

# Draw rectangles
def draw_rect(x, y, w, h, color):
    pygame.draw.rect(screen, color, [x, y, w, h])


# Places a block of text on the screen in a rect.
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

# Makes a Generic block of text in middle of screen
def centered_message_display(text,font,size,color):
    font = pygame.font.SysFont(font, size)
    TextSurf, TextRect = text_objects(text, font, color)
    TextRect.center = ((display_height/2), (display_width/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

# Makes a Generic block of text in specific loc.
def message_display(text,font,size,color,x,y):
    font = pygame.font.SysFont(font, size)
    TextSurf, TextRect = text_objects(text, font, color)
    TextRect.center = (x,y)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

# Button Function   msg is a str; x&y of button origin, width&height of box, button colors, & function to run when clicked
def start_button(msg,x,y,w,h,inactive,active,action=None):

    # Finds the mouse position and tracks it as a constant
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    if x+w > mouse[0] > x and y+h > mouse[1] > y: # If xPOS plus height is greater than mouse X &
    	draw_rect(x,y,w,h, active) # If yPOS plus width is greater than mouse Y then you are hovering over rect.
    	screen.blit(smenu_buttonhi, (x-30,y-75))

    	if click[0] == 1 and action != None:
            action() # Does whatever our action parameter is so long as its a function!
    else:   	
        draw_rect(x,y,w,h, inactive)
        screen.blit(smenu_button, (x-30,y-75)) 

    textSurf, textRect = text_objects(msg, largeText, white) # What we want it to say & assigning values
    textRect.center = ((x+(w/2), (y+(h/2)))) # Find the center by adding X plus width/2 same w/ Y value but w/ height
    screen.blit(textSurf, textRect) # Draws our Text

# Load Character Img
def player(x,y):
    screen.blit(charsprite, (x,y))

def game_intro():
    intro = True


    while intro:

        # For loop is for any EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        # Dispalys Background pic
        screen.blit(bedroom_back, (0,0))

        # Mouse getpos needs to be in loop to constantly refresh
        start_button('Start Game', 100, 100, 200, 55, blue, light_blue, quit_game)
        start_button('Load Game', 100, 210, 200, 55, blue, light_blue, quit_game)
        start_button('Options', 100, 320, 200, 55, blue, light_blue, quit_game)
        start_button('Credits', 100, 430, 200, 55, blue, light_blue, quit_game)
        start_button('Quit', 100, 540, 200, 55, blue, light_blue, quit_game)
        screen.blit(titleimg, (400,50))
        
        # Updates Screen & Sets Framerate
        pygame.display.update()
        clock.tick(60)

# Quit game function
def quit_game():
    pygame.quit()
    quit()


# Main Script Stack
game_intro()