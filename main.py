import pygame
import sys
import time

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 520
TIMER = 3000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

def update_screen():
    pygame.display.flip()
    clock.tick(60)

#Game variables 
game_state = {
    "1": None,
    "2": None,
    "3": None,
    "4": None,
    "5": None,
    "6": None,
    "7": None,
    "8": None,
    "9": None,
}

menu = False

global turn
turn = 1

global winning
winning = False
# Defining the sprites
gameboardIMG = pygame.image.load("RistinollaV2\\Pelilauta.png")
xIMG = pygame.image.load("RistinollaV2\\Risti.png")
oIMG = pygame.image.load("RistinollaV2\\Ympyrä.png")


class Photos():
    def __init__(self, image, resize=(int, int)):
        self.screen = screen
        self.new_size = pygame.transform.scale(image, (resize))
        self.image_x = (SCREEN_WIDTH - resize[0]) // 2
        self.image_y = (SCREEN_HEIGHT - resize[1] - 100) // 2
        

class Board:
# This code snippet creates a surface object using the pygame.surface library in PyGame's main scene.
    square1 = pygame.Rect(125, 16, 125, 125)
    square2 = pygame.Rect(258, 16, 125, 125)
    square3 = pygame.Rect(391, 16, 125, 125)
    square4 = pygame.Rect(125, 149, 125, 125)
    square5 = pygame.Rect(258, 149, 125, 125)
    square6 = pygame.Rect(391, 149, 125, 125)
    square7 = pygame.Rect(125, 282, 125, 125)
    square8 = pygame.Rect(258, 282, 125, 125)
    square9 = pygame.Rect(391, 282, 125, 125)
    def __init__(self) -> None:
        self.one = (145, 40)
        self.two = (275, 40)
        self.three = (405, 40)
        self.four = (145, 173)
        self.five = (275, 173)
        self.six = (405, 173)
        self.seven = (145, 306)
        self.eight = (275, 306)
        self.nine = (405, 306)



gameboard_img = Photos(gameboardIMG, (400, 400))
x = Photos(xIMG, (90, 90))
o = Photos(oIMG, (90, 90))

gameboard = Board()

class Buttons:
    left_button_surface = pygame.Surface((150, 50))
    right_button_surface = pygame.Surface((150, 50))

    menu1v1_button = pygame.Surface((300, 100))
    menubot_button = pygame.Surface((300, 100))
    menuquit_button = pygame.Surface((300, 100))
    left_button_hover = False
    right_button_hover = False

    hover_1v1 = False
    bot_hover = False
    quit_hover = False
    
    def __init__(self) -> None:
        #some variables to help
        self.button_height = 450
        self.screen_middle_width = SCREEN_WIDTH/2
        self.menu_button_height = SCREEN_HEIGHT/2 - 200

        
        #The font and setting it up
        self.font = pygame.font.Font(r"RistinollaV2\Comfortaa-Bold.ttf", 32)
        self.font_menu = pygame.font.Font(r"RistinollaV2\Comfortaa-Bold.ttf", 50)
        self.font_menu_bot = pygame.font.Font(r"RistinollaV2\Comfortaa-Bold.ttf", 45)
        self.font_menu_win = pygame.font.Font(r"RistinollaV2\Comfortaa-Bold.ttf", 80)
        self.text_restart = self.font.render("Restart", True, (0, 0, 0))
        self.text_bot = self.font.render("Menu", True, (0, 0, 0))
        self.font_1v1 = self.font_menu.render("Play 1V1", True, (0, 0, 0))
        self.font_BOT = self.font_menu_bot.render("Play With", True, (0, 0, 0))
        self.font_BOT_newline = self.font_menu_bot.render("A Bot", True, (0, 0, 0))
        self.font_quit = self.font_menu.render("QUIT", True, (0, 0, 0))
        

        self.left_button_rect = pygame.Rect(self.screen_middle_width - 200, self.button_height, 150, 50)
        self.right_button_rect = pygame.Rect(self.screen_middle_width + 50, self.button_height, 150, 50)

        self.menu1v1_button_rect = pygame.Rect(self.screen_middle_width/2 + 10, self.menu_button_height, 300, 100)
        self.menubot_button_rect = pygame.Rect(self.screen_middle_width/2 + 10, self.menu_button_height + 150, 300, 100)
        self.menuquit_button_rect = pygame.Rect(self.screen_middle_width/2 + 10, self.menu_button_height + 300, 300, 100)

        self.quit_button = pygame.Rect(SCREEN_WIDTH/2 - 150, 50, 300, 100)
        self.play_button_1v1 = pygame.Rect(SCREEN_WIDTH/2 - 150, 200, 300, 100)
        self.play_button_bot = pygame.Rect(SCREEN_WIDTH/2 - 150, 350, 300, 100)

    def create_left_button(self):
        left_button = Buttons.left_button_surface
        screen.blit(left_button, (self.screen_middle_width - left_button.get_width() - 50, self.button_height))
        #Fill the rectangle so that the black triangles dont show up
        left_button.fill((255, 255, 255))
        
        

        if button.left_button_rect.collidepoint(pygame.mouse.get_pos()):
            Buttons.left_button_hover = True
            #Draw the outer rectangle for the line
            pygame.draw.rect(left_button, (0, 0, 0),(0, 0, 150, 50), border_radius=5)
            #Draw the white box for the text
            pygame.draw.rect(left_button, (120, 120, 120), (1, 1, 148, 48), border_radius=5)
            
        else:
            Buttons.left_button_hover = False
            #Draw the outer rectangle for the line
            pygame.draw.rect(left_button, (0, 0, 0),(0, 0, 150, 50), border_radius=5)
            #Draw the white box for the text
            pygame.draw.rect(left_button, (255, 255, 255), (1, 1, 148, 48), border_radius=5)

        #Draw the text
        left_button.blit(self.text_bot, (left_button.get_width()/2 - 47, 7, 150, 50))


    def create_right_button(self):
        right_button = Buttons.right_button_surface
        screen.blit(right_button, (self.screen_middle_width - right_button.get_width() + 200, self.button_height))
        #Fill the rectangle so that the black triangles dont show up
        right_button.fill((255, 255, 255))
        

        if self.right_button_rect.collidepoint(pygame.mouse.get_pos()):
            Buttons.right_button_hover = True
            #Draw the outer rectangle for the line
            pygame.draw.rect(right_button, (0, 0, 0),(0, 0, 150, 50), border_radius=5)
            #Draw the white box for the text
            pygame.draw.rect(right_button, (120, 120, 120), (1, 1, 148, 48), border_radius=5)


        else:
            Buttons.right_button_hover = False
            #Draw the outer rectangle for the line
            pygame.draw.rect(right_button, (0, 0, 0),(0, 0, 150, 50), border_radius=5)
            #Draw the white box for the text
            pygame.draw.rect(right_button, (255, 255, 255), (1, 1, 148, 48), border_radius=5)


        #Draw the text
        right_button.blit(self.text_restart, (right_button.get_width()/2 - 60, 7, 150, 50))

    def draw_1v1_button(self):
        button_1v1 = Buttons.menu1v1_button
        screen.blit(button_1v1, (SCREEN_WIDTH/2 - 150, self.menu_button_height))
        #Fill the rectangle so that the black triangles dont show up
        button_1v1.fill((255, 255, 255))
 

        if self.menu1v1_button_rect.collidepoint(pygame.mouse.get_pos()):
            Buttons.hover_1v1 = True
            pygame.draw.rect(button_1v1, (0, 0, 0),(0, 0, 300, 100), border_radius=5)

            pygame.draw.rect(button_1v1, (120, 120, 120), (3, 3, 294, 94), border_radius=5)
            
        else:
            Buttons.hover_1v1 = False
            pygame.draw.rect(button_1v1, (0, 0, 0),(0, 0, 300, 100), border_radius=5)
            #Draw the white box for the text
            pygame.draw.rect(button_1v1, (255, 255, 255), (3, 3, 294, 94), border_radius=5)
            

        #Draw the text
        button_1v1.blit(self.font_1v1, (button_1v1.get_width()/2 -  self.font_1v1.get_width()/2, button_1v1.get_height()/2 - self.font_1v1.get_height()/2, 150, 50))



    def draw_bot_button(self):
        button_bot = Buttons.menubot_button
        screen.blit(button_bot, (SCREEN_WIDTH/2 - 150, self.menu_button_height + 150))
        #Fill the rectangle so that the black triangles dont show up
        button_bot.fill((255, 255, 255))
 

        if self.menubot_button_rect.collidepoint(pygame.mouse.get_pos()):
            Buttons.bot_hover = True
            pygame.draw.rect(button_bot, (0, 0, 0),(0, 0, 300, 100), border_radius=5)

            pygame.draw.rect(button_bot, (120, 120, 120), (3, 3, 294, 94), border_radius=5)
            
        else:
            Buttons.bot_hover = False
            pygame.draw.rect(button_bot, (0, 0, 0),(0, 0, 300, 100), border_radius=5)
            #Draw the white box for the text
            pygame.draw.rect(button_bot, (255, 255, 255), (3, 3, 294, 94), border_radius=5)
            

        #Draw the text
        button_bot.blit(self.font_BOT, (button_bot.get_width()/2 -  self.font_BOT.get_width()/2, button_bot.get_height()/2 - self.font_BOT.get_height()/2 - 20, 150, 50))
        button_bot.blit(self.font_BOT_newline, (button_bot.get_width()/2 -  self.font_BOT_newline.get_width()/2, button_bot.get_height()/2 - self.font_BOT_newline.get_height()/2 + 25, 150, 50))



    def draw_quit_button(self):
        button_quit = Buttons.menuquit_button
        screen.blit(button_quit, (SCREEN_WIDTH/2 - 150, self.menu_button_height + 300))
        #Fill the rectangle so that the black triangles dont show up
        button_quit.fill((255, 255, 255))
 

        if self.menuquit_button_rect.collidepoint(pygame.mouse.get_pos()):
            Buttons.quit_hover = True
            pygame.draw.rect(button_quit, (0, 0, 0),(0, 0, 300, 100), border_radius=5)

            pygame.draw.rect(button_quit, (120, 120, 120), (3, 3, 294, 94), border_radius=5)
            
        else:
            Buttons.quit_hover = False
            pygame.draw.rect(button_quit, (0, 0, 0),(0, 0, 300, 100), border_radius=5)
            #Draw the white box for the text
            pygame.draw.rect(button_quit, (255, 255, 255), (3, 3, 294, 94), border_radius=5)
            

        #Draw the text
        button_quit.blit(self.font_quit, (button_quit.get_width()/2 -  self.font_quit.get_width()/2, button_quit.get_height()/2 - self.font_quit.get_height()/2, 150, 50))

    def make_win_screen(self, wich):
        
        self.font_win = self.font_menu_win.render(f"{wich} Has Won The", True, (255, 255, 255))
        self.font_win_2 = self.font_menu_win.render("Game", True, (255, 255, 255))
        screen.blit(self.font_win, (7, SCREEN_HEIGHT / 3))
        screen.blit(self.font_win_2, (SCREEN_WIDTH/2 - self.font_win_2.get_width()/2, SCREEN_HEIGHT / 3 + self.font_win_2.get_height()))
        update_screen()
        time.sleep(2)
        reset_board()

button = Buttons()
#Game functions

    


def regX(pos):
    global turn
    game_state[pos] = 1
    turn = 0
    

def regO(pos):
    global turn
    game_state[pos] = 0
    turn = 1
    

def draw_icons():
    positions = {
        "1": gameboard.one,
        "2": gameboard.two,
        "3": gameboard.three,
        "4": gameboard.four,
        "5": gameboard.five,
        "6": gameboard.six,
        "7": gameboard.seven,
        "8": gameboard.eight,
        "9": gameboard.nine,
    }

    for key, pos in positions.items():
        if game_state[key] == 0:
            screen.blit(o.new_size, pos)
        elif game_state[key] == 1:
            screen.blit(x.new_size, pos)

def check_win():
    # Define all possible winning combinations
    win_conditions = [
        ["1", "2", "3"],  # Top row
        ["4", "5", "6"],  # Middle row
        ["7", "8", "9"],  # Bottom row
        ["1", "4", "7"],  # Left column
        ["2", "5", "8"],  # Middle column
        ["3", "6", "9"],  # Right column
        ["1", "5", "9"],  # Diagonal from top-left to bottom-right
        ["3", "5", "7"]   # Diagonal from top-right to bottom-left
    ]

    # Iterate through each winning combination
    for condition in win_conditions:
        # Check if all three squares in the current winning combination belong to the same player
        if game_state[condition[0]] == game_state[condition[1]] == game_state[condition[2]] is not None:
            return True  # Return True if a winning combination is found

    return False  # Return False if no winning combination is found

def place_items():
    if Board.square1.collidepoint(pygame.mouse.get_pos()):
        if game_state["1"] == None:
            if turn == 0:
                regO("1")
            else:
                regX("1")
        else:
            print("this place is used")
        
    if Board.square2.collidepoint(pygame.mouse.get_pos()):
        if game_state["2"] == None:
            if turn == 0:
                regO("2")
            else:
                regX("2")
        else:
            print("this place is used")
    if Board.square3.collidepoint(pygame.mouse.get_pos()):
        if game_state["3"] == None:
            if turn == 0:
                regO("3")
            else:
                regX("3")
        else:
            print("this place is used")
    if Board.square4.collidepoint(pygame.mouse.get_pos()):
        if game_state["4"] == None:
            if turn == 0:
                regO("4")
            else:
                regX("4")
        else:
            print("this place is used")
    if Board.square5.collidepoint(pygame.mouse.get_pos()):
        if game_state["5"] == None:
            if turn == 0:
                regO("5")
            else:
                regX("5")
        else:
            print("this place is used")
    if Board.square6.collidepoint(pygame.mouse.get_pos()):
        if game_state["6"] == None:
            if turn == 0:
                regO("6")
            else:
                regX("6")
        else:
            print("this place is used")
    if Board.square7.collidepoint(pygame.mouse.get_pos()):
        if game_state["7"] == None:    
            if turn == 0:
                regO("7")
            else:
                regX("7")
        else:
            print("this place is used")
    if Board.square8.collidepoint(pygame.mouse.get_pos()):
        if game_state["8"] == None:
            if turn == 0:
                regO("8")
            else:
                regX("8")
        else:
            print("this place is used")
    if Board.square9.collidepoint(pygame.mouse.get_pos()):
        if game_state["9"] == None:
            if turn == 0:
                regO("9")
            else:
                regX("9")
        else:
            print("this place is used")


def reset_board():
    global turn
    turn = 1
    global winning
    winning = False
    game_state.update({
    "1": None,
    "2": None,
    "3": None,
    "4": None,
    "5": None,
    "6": None,
    "7": None,
    "8": None,
    "9": None,
})

color = pygame.color.Color(144, 144, 144, a=144)
overlay = pygame.rect.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)


def win_screen():
    runner = True
    while runner:
        


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        update_screen()



def main_menu():

    run = True
    while run:

        screen.fill((255, 255, 255))

        button.draw_1v1_button()
        button.draw_bot_button()
        button.draw_quit_button()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Buttons.hover_1v1:
                    game()
                if Buttons.bot_hover:
                    print("Not invented")
                if Buttons.quit_hover:
                    pygame.quit()
                    sys.exit()

        update_screen()






def game():

    global winning
    running = True
    while running:
        

        

        screen.fill((255, 255, 255))
        screen.blit(gameboard_img.new_size, (gameboard_img.image_x, gameboard_img.image_y))
        button.create_left_button()
        button.create_right_button()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if winning == False:
                    place_items()
                if Buttons.left_button_hover:
                    main_menu()
                if Buttons.right_button_hover:
                    reset_board()
                


        

        draw_icons()
        if check_win():
            

                
            game_over_screen_fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            game_over_screen_fade.fill((100, 100, 100))
            game_over_screen_fade.set_alpha(160)
            

            screen.blit(game_over_screen_fade, (0, 0))
            winning = True
            if turn == 0:
                button.make_win_screen("X")
                
            elif turn == 1:
                button.make_win_screen("0")
                
            

        update_screen()
        



main_menu()



pygame.quit()
sys.exit()
