import pygame
import time
import json


# Python Dict used for Save Data that will later turn into JSON
# Dictionary isnt ONLY data set that can be written to. But is one of the more expansive
# For my purposes a Tuple may be the best option
# savedata = {
#     'Event1' : 'Action1',
#     'Event2' : 'Action2',
#     'Event3' : 'Action3'
# }

# With open allows interfacing w/ JSON code in python syntax
# with open('testsave.txt', 'w') as testfile: # open txt file; if it doesn't exit make it ('w') testfile used to interact w/ JSON
#     json.dump(savedata,testfile) # Dumps out savedata variable into the testfile var which is just our txt shorthand

# Converts JSON data back into python dict; is essentially your save load function
# with open('testsave.txt') as testfile:
#     data = json.load(testfile)



# Initializing Pygame Library
pygame.init()
pygame.font.init()

# Sets the size of the window being drawn
display_height = 1280
display_width = 720

x,y = 0,0

# Generic Variables Establishment
clock = pygame.time.Clock()
screen = pygame.display.set_mode((display_height, display_width))
smallText = pygame.font.SysFont('Roboto.ttf', 20) # Font & size def.
mediumText = pygame.font.SysFont('Roboto.ttf', 35) # Font & size def.
largeText = pygame.font.SysFont('Roboto.ttf', 55)


# Image Loading Index
icon = pygame.image.load('icon.png')
bedroom_back = pygame.image.load('bedroom_background.png')
charsprite = pygame.image.load('char_sprite.png')

# Color Codes
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
light_green = (0,255,0)
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

# YOU CAN ALSO ADD BORDERWIDTH! add ,2 to your rect to ONLY render border!
def draw_border(x, y, w, h, color, border):
    pygame.draw.rect(screen, color, [x, y, w, h], border)

# Places a block of text on the screen in a rect.
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

# Makes a Generic block of text; func. should be edited to include more params though
def message_display(text):
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_height/2), (display_width/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

# Load Character Img
def player(x,y):
    screen.blit(charsprite, (x,y))


# Quit game function
def quit_game():
    pygame.quit()
    quit()

# Button Function   msg is a str; x&y of button origin, width&height of box, button colors, & function to run when clicked
def button(msg,x,y,w,h,inactive,active,action=None):

    # Finds the mouse position and tracks it as a constant
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y: # If xPOS plus height is greater than mouse X &
                                            # If yPOS plus width is greater than mouse Y then you are hovering over rect.
        draw_rect(x,y,w,h, active)
        if click[0] == 1 and action != None: # If mouse is clicked and 'action' parameter not blank then do action on mouse click
            action() # Does whatever our action parameter is so long as its a function!
    else:
        draw_rect(x,y,w,h, inactive)

    textSurf, textRect = text_objects(msg, smallText) # What we want it to say & assigning values
    textRect.center = ((x+(w/2), (y+(h/2)))) # Find the center of the button by adding X plus width/2 same w/ Y value but w/ height
    screen.blit(textSurf, textRect) # Draws our Text

# Dictionary Containing Events & Bools to create accurate save file
# Since we're using a Dictionary its automatically defined globally, meaning we can use it outside
# any loops that may be created. We will probably have to load it as its own class or possibly file
# to ensure true global access of saving

data = {
    'Event1' : False,
    'Event2' : False,
    'Event3' : False
}
# Tries to open our save file and override any values that we previously had;
try:
    with open('refsave.txt') as refsavefile:
        data = json.load(refsavefile)
except:
    print('No file yet')


def reversefade(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for x in range(0,300):
        fade.set_alpha(x)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

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
        button('GOMEGGIES', 350, 450, 100, 50, red, blue, game_loop)
        button('Whomegalul?', 850, 450, 100, 50, red, blue, quit_game)

        # Updates Screen & Sets Framerate
        pygame.display.update()
        clock.tick(60)       




# Main Game loop
def game_loop():
    player_xloc = (35)
    player_yloc = (100)
    running = True
    usertext_input = '' # Used to allow usr input as str
    textborder = pygame.Rect(600,370,500,100) # Used for positioning of input txt box; not sure why, but only works this way
    box_selected = False # Bool to tell if usr input box is active
    flashcount = 0
    flashcolors = [black,light_green]
    
    while running:
       
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                # Saves our game on quitting of game automatically; pogchamp
                with open('refsave.txt', 'w') as refsavefile:
                    json.dump(data, refsavefile)

                quit_game()

            # If Key gets pressed, do thing
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:

                    # Checks to see if our Bool is true in order to do event; testing our save
                    if ('Event1', True) in data.items():
                        draw_rect(600, 370, 100, 100, black)
                        message_display("TEST")
                        time.sleep(3)

                # If 'P' is pressed, exec pause screen func
                if event.key == pygame.K_p:
                    pause_screen()

                if event.key == pygame.K_s:
                    # Changes the value of our dictionary to signify a save
                    data['Event1'] = True

                # Input text box
                if box_selected == True: # Checks if selection bool is active or inactive
                    if event.key == pygame.K_BACKSPACE: # Delete last char in str
                        usertext_input = usertext_input[0:-1] # Use indexing to delete only 1 char
                    
                    elif event.key == pygame.K_RETURN: # Does action when enter is pressed
                        print('Yo Pier you gon come out here?')

                    else:
                        usertext_input += event.unicode # Captures User text and puts it in temp str var

            # If mos pos collides w/ input txt box pos then do thing
            if event.type == pygame.MOUSEBUTTONDOWN:
                if textborder.collidepoint(event.pos): #If collide, then change bool & make box active 
                    box_selected = True
                else:
                    box_selected = False # Returns to inactive state

                

        # Fills the Screen W/ color
        screen.fill(white)
        screen.blit(bedroom_back, (0,0))
        flashcount += 1

        # Places Player Sprite on screen
        player(player_xloc,player_yloc)

        # Renders our text from users input
        usertext_surface = mediumText.render(usertext_input,True,flashcolors[(flashcount%2)]) # Options for rending actual Text str
        screen.blit(usertext_surface, (0,0)) # Blits our text; can edit coords to be text box w/ draw_rec

        # References an established rectangle var; '2' Shows only the border & Draws our Shape;
        pygame.draw.rect(screen,white,textborder,2)
        # Blits our text into our TextBorder, +5 makes it look pretty
        screen.blit(usertext_surface, (textborder.x + 5, textborder.y + 5))

        testscrolltext = largeText.render('HEYO PIER YOU GON COME OUT HERE?', True, white)
        


        # Updates Screen & Sets Framerate
        pygame.display.update()
        clock.tick(60)

# Pause Screen
def pause_screen():
    pause = True
    
    while pause:
        for event in pygame.event.get():

            # Generic Quit func.
            if event.type == pygame.QUIT:
                quit_game()

        screen.fill(red)
        button('GOMEGGIES', 350, 450, 100, 50, red, blue, game_loop)
        button('Whomegalul?', 850, 450, 100, 50, red, blue, quit_game)

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
