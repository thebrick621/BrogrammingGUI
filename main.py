import pygame
import time
import json
# Initializing Pygame Library
pygame.init()
pygame.font.init()

# Sets the size of the window being drawn
display_height = 1280
display_width = 720

# Generic Variables Establishment
clock = pygame.time.Clock()
screen = pygame.display.set_mode((display_height, display_width))

# Font & Text vars
smallText = pygame.font.SysFont('Roboto.ttf', 20) # Font & size def.
mediumText = pygame.font.SysFont('Roboto.ttf', 35) # Font & size def.
largeText = pygame.font.SysFont('Roboto.ttf', 50)
largebloxText = pygame.font.Font('Blox2.ttf', 50)
mediumstitchText = pygame.font.Font('StitchWarrior.ttf', 35)
buttonstitchText = pygame.font.Font('StitchWarrior.ttf', 40)
largestitchText = pygame.font.Font('StitchWarrior.ttf', 50)
hugestitchText = pygame.font.Font('StitchWarrior.ttf', 75)

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
blue = (0,50,255)
light_blue = (0,102,255)
light_pink = (255,0,221)
magenta = (255,0,255)
yellow = (255,255,0)
light_yellow = (255,228,138)
dark_grey = (78,78,78)

# Flashy Text Stuff
flashcount = 0
flashcolors = [black,light_green]
flashcolors2 = [black,green]

# Title & Icon Data
pygame.display.set_caption("Brogramming")
pygame.display.set_icon(icon)

# Save Stuff
savedata = {
    'Firstsave' : False
}

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

        # Found a bug here; not sure why but executing the function after clicking isn't 100% working. Kinda works?
        # Switching game to not rely on buttons but will use for ez development & navi
    	if click[0] == 1 and action != None:
            action() # Does whatever our action parameter is so long as its a function!
    else:   	
        draw_rect(x,y,w,h, inactive)
        screen.blit(smenu_button, (x-30,y-75)) 

    textSurf, textRect = text_objects(msg, buttonstitchText, black) # What we want it to say & assigning values
    textRect.center = ((x+(w/2), (y+(h/2)))) # Find the center by adding X plus width/2 same w/ Y value but w/ height
    screen.blit(textSurf, textRect) # Draws our Text

def player(x,y):
# Load Character Img
    screen.blit(charsprite, (x,y))

def scene_open():
    print('null')
def loadsave():
    print('null')
def delsave_confirm():
    loop = True
    usertext_input = ''
    inputbox = pygame.Rect(350,100, 600,400) #POS of input box
    inputmargins = (inputbox.x + 5, inputbox.y + 150)
    outputmargins = (inputbox.x + 5, inputbox.y + 210)
    # Gotta do it global to keep the color shift throughout the game *Sadge*
    global flashcount
    global flashcolors
    global flashcolors2
    
    while loop:

        # For loop is for any EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Autosaves on quit
                with open('mysavedata.txt', 'w') as savefile:
                    json.dump(savedata, savefile)
                quit_game()


            if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_BACKSPACE:
                        # Converts all input txt to lowercase for easier command struc
                        usertext_input = usertext_input[:-1]
                    
                    # BIGGGGG Elif to link to commands from here incl. cheats & EEs as well as any other menu commands
                    elif event.key == pygame.K_RETURN:
                        usertext_input = usertext_input.lower()

                        # Add if statements to do something if certain str is entered
                        if 'no' in usertext_input or 'n' in usertext_input:
                            start_game()

                        elif 'yes' in usertext_input or 'y' in usertext_input:
                            savedata.clear()
                            savedata['Firstave']=False
                            with open('mysavedata.txt', 'w') as savefile:
                                json.dump(savedata, savefile)
                            screen.blit(mediumstitchText.render('Deleted',True, flashcolors[1]),(outputmargins))
                            pygame.display.update()
                            pygame.time.delay(1500)
                            start_game()

                        # If input = dummystr then clear text
                        del usertext_input
                        usertext_input = ''

                    # Sets max len of input in input box
                    elif len(usertext_input) == 19:
                        usertext_input = usertext_input[:-1]
                    # Writes on the screen
                    else:
                        usertext_input += event.unicode

            # Allows us to select & Deselect text box; maybe can make this a function?
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inputbox.collidepoint(event.pos):
                    box_selected = True
                else:
                    box_selected = False

        # Dispalys Background pic
        screen.blit(bedroom_back, (0,0))

        #screen.blit(titleimg, (250,0))
        flashcount += 1
        
        # Blits the main input box and usr text
        usertext_surface = largestitchText.render(usertext_input,True,flashcolors[(flashcount%2)])
        titletext = hugestitchText.render('Save Being Erased',True,flashcolors2[(flashcount%2)])
        default_cmdline = mediumstitchText.render('ARE YOU SURE?',True,flashcolors2[(flashcount%2)])
        pygame.draw.rect(screen,black,inputbox)
        screen.blit(titletext, (inputbox.x , inputbox.y + 5))
        screen.blit(default_cmdline, (inputbox.x + 5, inputbox.y + 105))
        screen.blit(usertext_surface, (inputmargins))


        # Updates Screen & Sets Framerate
        pygame.display.update()
        clock.tick(60)

def start_game():
    intro = True
    usertext_input = ''
    inputbox = pygame.Rect(350,100, 600,400) #POS of input box
    inputmargins = (inputbox.x + 5, inputbox.y + 150)
    outputmargins = (inputbox.x + 5, inputbox.y + 210)
    with open('mysavedata.txt') as savefile:
        savedata = json.load(savefile)

    # Gotta do it global to keep the color shift throughout the game *Sadge*
    global flashcount
    global flashcolors
    global flashcolors2
    
    while intro:

        # For loop is for any EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Autosaves on quit
                with open('mysavedata.txt', 'w') as savefile:
                    json.dump(savedata, savefile)
                quit_game()


            if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_BACKSPACE:
                        # Converts all input txt to lowercase for easier command struc
                        usertext_input = usertext_input[:-1]
                    
                    # BIGGGGG Elif to link to commands from here incl. cheats & EEs as well as any other menu commands
                    elif event.key == pygame.K_RETURN:
                        usertext_input = usertext_input.lower()

                        # Add if statements to do something if certain str is entered
                        if 'info' in usertext_input or 'nfo' in usertext_input:
                            screen.blit(mediumstitchText.render('Created by Preston Philbrick 2022',True, flashcolors[1]),(outputmargins))
                            pygame.display.update()
                            pygame.time.delay(2000)

                        elif 'quit' in usertext_input or 'back' in usertext_input or 'exit' in usertext_input:
                            screen.blit(mediumstitchText.render('Goodbye',True, flashcolors[1]),(outputmargins))
                            pygame.display.update()
                            game_intro()

                        elif 'startgame' in usertext_input or 'start' in usertext_input or 'start game' in usertext_input:
                            
                            if ('Firstsave', False) in savedata.items():
                                savedata['Firstsave'] = True
                                scene_open()

                            elif ('Firstsave', True) in savedata.items():
                                loadsave()

                        elif 'erasesave' in usertext_input or 'erase' in usertext_input or 'erase save' in usertext_input:
                            
                            if ('Firstsave', False) in savedata.items():
                                screen.blit(mediumstitchText.render('No Save Data Found',True, flashcolors[1]),(outputmargins))
                                pygame.display.update()
                                pygame.time.delay(2000)

                            if ('Firstsave', True) in savedata.items():
                                delsave_confirm()

                        elif 'help' in usertext_input:
                            screen.blit(mediumstitchText.render('StartGame     Info',True, magenta),(inputbox.x + 110, inputbox.y + 210))
                            screen.blit(mediumstitchText.render('EraseSave    Back',True, magenta),(inputbox.x + 110, inputbox.y + 260))
                            pygame.display.update()
                            pygame.time.delay(2000)

                        # If input = dummystr then clear text
                        del usertext_input
                        usertext_input = ''

                    # Sets max len of input in input box
                    elif len(usertext_input) == 19:
                        usertext_input = usertext_input[:-1]
                    # Writes on the screen
                    else:
                        usertext_input += event.unicode

            # Allows us to select & Deselect text box; maybe can make this a function?
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inputbox.collidepoint(event.pos):
                    box_selected = True
                else:
                    box_selected = False

        # Dispalys Background pic
        screen.blit(bedroom_back, (0,0))

        #screen.blit(titleimg, (250,0))
        flashcount += 1
        
        # Blits the main input box and usr text
        helptext = mediumstitchText.render('Type Help For Commands', True, flashcolors[(flashcount%2)])
        usertext_surface = largestitchText.render(usertext_input,True,flashcolors[(flashcount%2)])
        titletext = hugestitchText.render('Start Game',True,flashcolors2[(flashcount%2)])
        default_cmdline = mediumstitchText.render('What would you like to do?',True,flashcolors2[(flashcount%2)])
        pygame.draw.rect(screen,black,inputbox)
        screen.blit(helptext, (inputbox.x + 110, inputbox.y + 350))
        screen.blit(titletext, (inputbox.x + 110, inputbox.y + 5))
        screen.blit(default_cmdline, (inputbox.x + 5, inputbox.y + 105))
        screen.blit(usertext_surface, (inputmargins))


        # Updates Screen & Sets Framerate
        pygame.display.update()
        clock.tick(60)

def game_intro():
    intro = True
    usertext_input = ''
    inputbox = pygame.Rect(350,100, 600,400) #POS of input box
    box_selected = False
    inputmargins = (inputbox.x + 5, inputbox.y + 150)
    outputmargins = (inputbox.x + 5, inputbox.y + 210)
    global flashcount
    global flashcolors
    global flashcolors2

    while intro:

        # For loop is for any EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Autosaves on quit
                with open('mysavedata.txt', 'w') as savefile:
                    json.dump(savedata, savefile)
                quit_game()

            if event.type == pygame.KEYDOWN:

                if box_selected == True:

                    if event.key == pygame.K_BACKSPACE:
                        # Converts all input txt to lowercase for easier command struc
                        usertext_input = usertext_input[:-1]
                    
                    # BIGGGGG Elif to link to commands from here incl. cheats & EEs as well as any other menu commands
                    elif event.key == pygame.K_RETURN:
                        usertext_input = usertext_input.lower()

                        # Add if statements to do something if certain str is entered
                        if 'info' in usertext_input or 'nfo' in usertext_input:
                            screen.blit(mediumstitchText.render('Created by Preston Philbrick 2022',True, flashcolors[(flashcount%2)]),(outputmargins))
                            pygame.display.update()
                            pygame.time.delay(1250)


                        elif 'quit' in usertext_input:
                            screen.blit(mediumstitchText.render('Goodbye',True, flashcolors[1]),(outputmargins))
                            pygame.display.update() 
                            pygame.time.delay(1000)
                            quit_game()

                        elif 'help' in usertext_input:
                            screen.blit(mediumstitchText.render('Quit   Info   Start',True, magenta),(outputmargins))
                            pygame.display.update()
                            pygame.time.delay(2000)

                        elif 'start' in usertext_input or 'start game' in usertext_input or 'startgame' in usertext_input:
                            del usertext_input
                            usertext_input = ''
                            pygame.time.delay(250)
                            start_game()

                        elif 'redtext' in usertext_input or 'red text' in usertext_input:
                            del usertext_input
                            usertext_input = ''
                            screen.blit(mediumstitchText.render('Updated',True, flashcolors[1]),(outputmargins))
                            pygame.display.update()
                            pygame.time.delay(2000)
                            flashcolors = [black, light_red]
                            flashcolors2 = [black, red]

                        elif 'bluetext' in usertext_input or 'blue text' in usertext_input:
                            del usertext_input
                            usertext_input = ''
                            screen.blit(mediumstitchText.render('Updated',True, flashcolors[1]),(outputmargins))
                            pygame.display.update()
                            pygame.time.delay(2000)
                            flashcolors = [black, light_blue]
                            flashcolors2 = [black, blue]

                        elif 'pinktext' in usertext_input or 'pink text' in usertext_input:
                            del usertext_input
                            usertext_input = ''
                            screen.blit(mediumstitchText.render('Updated',True, flashcolors[1]),(outputmargins))
                            pygame.display.update()
                            pygame.time.delay(2000)
                            flashcolors = [black, light_pink]
                            flashcolors2 = [black, magenta]

                        elif 'yellowtext' in usertext_input or 'yellow text' in usertext_input:
                            del usertext_input
                            usertext_input = ''
                            screen.blit(mediumstitchText.render('Updated',True, flashcolors[1]),(outputmargins))
                            pygame.display.update()
                            pygame.time.delay(2000)
                            flashcolors = [black, light_yellow]
                            flashcolors2 = [black, yellow]

                        elif 'greentext' in usertext_input or 'green text' in usertext_input:
                            del usertext_input
                            usertext_input = ''
                            screen.blit(mediumstitchText.render('Updated',True, flashcolors[1]),(outputmargins))
                            pygame.display.update()
                            pygame.time.delay(2000)
                            flashcolors = [black, light_green]
                            flashcolors2 = [black, green]

                        # If input = dummystr then clear text
                        del usertext_input
                        usertext_input = ''

                    # Sets max len of input in input box
                    elif len(usertext_input) == 19:
                        usertext_input = usertext_input[:-1]
                    # Writes on the screen
                    else:
                        usertext_input += event.unicode

            # Allows us to select & Deselect text box; maybe can make this a function?
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inputbox.collidepoint(event.pos):
                    box_selected = True
                else:
                    box_selected = False

        # Dispalys Background pic
        screen.blit(bedroom_back, (0,0))

        # Mouse getpos needs to be in loop to constantly refresh
        start_button('Start Game', 50, 575, 200, 55, blue, light_blue, start_game)
        start_button('Load Game', 300, 575, 200, 55, blue, light_blue, quit_game)
        start_button('Options', 550, 575, 200, 55, blue, light_blue, quit_game)
        start_button('Credits', 800, 575, 200, 55, blue, light_blue, quit_game)
        start_button('Quit', 1050, 575, 200, 55, blue, light_blue, quit_game)
        #screen.blit(titleimg, (250,0))
        flashcount += 1
        
        # Blits the main input box and usr text
        helptext = mediumstitchText.render('Type Help For Commands', True, flashcolors[(flashcount%2)])
        usertext_surface = largestitchText.render(usertext_input,True,flashcolors[(flashcount%2)])
        titletext = hugestitchText.render('Brogramming',True,flashcolors2[(flashcount%2)])
        default_cmdline = mediumstitchText.render('What would you like to do?',True,flashcolors2[(flashcount%2)])
        pygame.draw.rect(screen,black,inputbox)
        screen.blit(helptext, (inputbox.x + 110, inputbox.y + 350))
        screen.blit(titletext, (inputbox.x + 110, inputbox.y + 5))
        screen.blit(default_cmdline, (inputbox.x + 5, inputbox.y + 105))
        screen.blit(usertext_surface, (inputmargins))


        # Updates Screen & Sets Framerate
        pygame.display.update()
        clock.tick(60)


# Quit game function
def quit_game():
    pygame.quit()
    quit()


# Main Event Stack
game_intro()