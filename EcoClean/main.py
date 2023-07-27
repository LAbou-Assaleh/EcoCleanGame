# importing modules
import pygame, sys
from pygame import *
import random
import math
pygame.init()
# creating fonts
font = pygame.font.SysFont("Times New Roman",20)
minifont = pygame.font.SysFont("Times New Roman",25)
font2 = pygame.font.SysFont('Times New Roman', 50)
fontv2 = pygame.font.SysFont("Times New Roman", 30)
# creating screen
SIZE = (width,height) = (900,600)
screen = pygame.display.set_mode(SIZE)
# creating colors
green = (0,255,0)
blue = (0, 0, 255)
black = (0,0,0)
red = (255, 0, 0)
pale = (238,232,170)
numred = (172, 27, 27)
grey = (100, 100, 100)
white = (255, 255, 255)
# creating variables
restart = False
total = 0
multi = 0.5

# returns which key is pressed
def key():
  while True:
    for event in pygame.event.get():
      if event.type == KEYUP:
        if event.key == K_0:
          return "0"
        elif event.key == K_1:
          return "1"
        elif event.key == K_2:
          return "2"
        elif event.key == K_3:
          return "3"
        elif event.key == K_4:
          return "4"
        elif event.key == K_5:
          return "5"
        elif event.key == K_6:
          return "6"
        elif event.key == K_7:
          return "7"
        elif event.key == K_8:
          return "8"
        elif event.key == K_9:
          return "9"
        elif event.key == K_a:
          return "a"
        elif event.key == K_b:
          return "b"
        elif event.key == K_c:
          return "c"
        elif event.key == K_d:
          return "d"
        elif event.key == K_e:
          return "e"
        elif event.key == K_f:
          return "f"
        elif event.key == K_g:
          return "g"
        elif event.key == K_h:
          return "h"
        elif event.key == K_i:
          return "i"
        elif event.key == K_j:
          return "j"
        elif event.key == K_k:
          return "k"
        elif event.key == K_l:
          return "l"
        elif event.key == K_m:
          return "m"
        elif event.key == K_n:
          return "n"
        elif event.key == K_o:
          return "o"
        elif event.key == K_p:
          return "p"
        elif event.key == K_q:
          return "q"
        elif event.key == K_r:
          return "r"
        elif event.key == K_s:
          return "s"
        elif event.key == K_t:
          return "t"
        elif event.key == K_u:
          return "u"
        elif event.key == K_v:
          return "v"
        elif event.key == K_w:
          return "w"
        elif event.key == K_x:
          return "x"
        elif event.key == K_y:
          return "y"
        elif event.key == K_z:
          return "z"
        elif event.key == K_SPACE:
          return " "
        elif event.key == K_BACKSPACE:
          return "delete"
        elif event.key == K_RETURN:
          return "check"
        elif event.unicode == "_":
            return "_"
        else:
          return "Invalid"
# recursive function that allows for spreading of zeros
def spread(x, y, h, w):
    # ensures that program does not check outside of the grid
    if x > w+side-1 or y > h+down-1 or x < side or y < down:
        return 0
    # appends it as a checked variable
    check.append([x, y])
    next = adj(x, y)
    # draws the cell
    pygame.draw.rect(screen, white, (x * 30 - 30, y * 30 - 30, 30, 30))
    pygame.draw.rect(screen, grey, (x * 30 - 30, y * 30 - 30, 30, 30), 1)
    text = font.render(str(next), True, red)
    screen.blit(text, (x * 30 - 20, y * 30 - 25))
    # calls the function for all cells around it if the value of the cell is 0
    if next == 0:
        if [x + 1, y] not in check:
            spread(x + 1, y, h, w)
        if [x - 1, y] not in check:
            spread(x - 1, y, h, w)
        if [x, y + 1] not in check:
            spread(x, y + 1, h, w)
        if [x, y - 1] not in check:
            spread(x, y - 1, h, w)
        if [x + 1, y + 1] not in check:
            spread(x + 1, y + 1, h, w)
        if [x - 1, y + 1] not in check:
            spread(x - 1, y + 1, h, w)
        if [x - 1, y - 1] not in check:
            spread(x - 1, y - 1, h, w)
        if [x + 1, y - 1] not in check:
            spread(x + 1, y - 1, h, w)
# locates which square is being clicked
def locate(x):
	return int(math.ceil(x / 30))
# check for adjacent mines
def adj(x, y):
    anum = 0
    if [x+1, y] in  location:
        anum += 1
    if [x-1, y] in  location:
        anum += 1
    if [x, y+1] in  location:
        anum += 1
    if [x, y-1] in  location:
        anum += 1
    if [x+1, y-1] in  location:
        anum += 1
    if [x+1, y+1] in  location:
        anum += 1
    if [x-1, y+1] in  location:
        anum += 1
    if [x-1, y-1] in  location:
        anum += 1
    return anum
# runs the minesweeper game
def collecter(h , w, mines):
    # defining global variables
    global location, flaged, check, down, side
    # creating variables that decide how much to move the grid to the side and down to center the grid
    down = int((25 - h)/2-1)
    side = int((35-w)/2-1)
    # creating important variables for the game
    wipe()
    grid = []
    location = []
    flaged = []
    check = []
    # loading the postions of the mines
    for i in range(mines):
        mx = random.randrange(side, w+side-1)
        my = random.randrange(down, h+down-1)
        point = [mx, my]
        while point in location:
            mx = random.randrange(side, w + side)
            my = random.randrange(down, h + down)
            point = [mx, my]
        location.append([mx, my])
    # drawing the base grid
    for i in range(down, h+down):
        for j in range(side, w+side):
            grid.append([j, i])
            pygame.draw.rect(screen, white, (j * 30 - 30, i * 30 - 30, 30, 30))
            pygame.draw.rect(screen, grey, (j * 30 - 30, i * 30 - 30, 30, 30), 1)
    pygame.event.get()
    pygame.display.update()
    # running the game
    while True:
        # checking if the game has been won
        if len(check) >= h * w - mines:
            return True
        # checking for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # checking if the mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # checking wether to return to the menu
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    d = ((x - 450) ** 2 + (y - 570) ** 2)
                    d = d ** (1 / 2)
                    if round(d) <= 20:
                        menu()
                # checking which cell was clicked
                x, y = event.pos
                x = locate(x)
                y = locate(y)
                if [x, y] in grid:
                    # checking wether to display the value of the cell
                    if event.button == 1:
                        if [x, y] in location:
                            for i in range(down, h+down):
                                for j in range(side, w+side):
                                    p = [j, i]
                                    if p in location:
                                        pygame.draw.rect(screen, green, (j * 30 - 30, i * 30 - 30, 30, 30))
                                    pygame.draw.rect(screen, grey, (j * 30 - 30, i * 30 - 30, 30, 30), 1)
                            pygame.display.update()
                            return False
                        else:
                            spread(x, y, h, w)
                            pygame.display.update()
                    # checking wether to flag the cell
                    if event.button == 3:
                        if [x, y] in flaged:
                            if [x, y] in check:
                                spot = check.index([x, y])
                                check.pop(spot)
                            pygame.draw.rect(screen, white, (x*30-30, y*30-30, 30, 30))
                            pygame.draw.rect(screen, grey, (x * 30 - 30, y * 30 - 30, 30, 30), 1)
                            gone = flaged.index([x, y])
                            flaged.pop(gone)
                        else:
                            pygame.draw.rect(screen, red, (x * 30 - 30, y * 30 - 30, 30, 30))
                            pygame.draw.rect(screen, grey, (x * 30 - 30, y * 30 - 30, 30, 30), 1)
                            flaged.append([x, y])
                        pygame.display.update()
# loading code for the compacter
score = 0
image = pygame.image.load("trash.png")
image = pygame.transform.scale(image, (150, 150))
# draws the current board
def draw(board):
    wipe()
    global score
    points = fontv2.render(str(score), True, red)
    screen.blit(points, (0, 0))
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                size = get_font(str(board[i][j]), 130)
                font = pygame.font.SysFont("Times New Roman", size)
                value = font.render(str(board[i][j]), True, black)
                text_rect = value.get_rect()
                square = pygame.Rect((i*150+150, j*150),(150, 150) )
                text_rect.center = square.center
                screen.blit(image, (i * 150+150, j * 150))
                screen.blit(value, text_rect)
                pygame.draw.rect(screen, black, (i * 150+150, j * 150, 150, 150), 3)
            else:
                pygame.draw.rect(screen, grey, (i * 150+150, j * 150, 150, 150))
                pygame.draw.rect(screen, black, (i * 150+150, j * 150, 150, 150), 3)
    pygame.event.get()
    pygame.display.update()
# shifts everything to the left and combines what needs to be combined
def shift_left(board):
    global score
    empty = []
    # creating the coumn
    for j in range(4):
        column = []
        for i in range(4):
            if board[i][j] != 0:
                column.append(board[i][j])
        for i in range(1, len(column)):
            if column[i] == column[i-1]:
                column[i] = 0
                column[i-1] *= 2
                score += column[i - 1]
        column = [cell for cell in column if cell != 0]
        # Pad the column with empty cells
        while len(column) < 4:
            column.append(0)
        # Update the board with the new column
        for i in range(4):
            board[i][j] = column[i]
            if column[i] == 0:
                empty.append([i, j])
    return board, empty
# getting the font for the number that is displayed on the cell
def get_font(num, font):
    fontx = pygame.font.SysFont("Times New Roman", font)
    text = fontx.render(num, True, numred)
    text_rect = text.get_rect()
    while text_rect.width > 130 or text_rect.height > 130:
        font -= 1
        fontx = pygame.font.SysFont("Times New Roman", font)
        text = fontx.render(num, True, numred)
        text_rect = text.get_rect()
    else:
        return font
# checking if the game should end
def lose(board):
    for i in range(4):
        if board[0][i] == 0 or board[i][0] == 0:
            return False
    for i in range(4):
        for j in range(1, 4):
            if board[i][j] == 0:
                return False
            if board[i][j] == board[i][j-1]:
                return False
    for i in range(4):
        for j in range(1, 4):
            if board[j][i] == 0:
                return False
            if board[j][i] == board[j-1][i]:
                return False
    return True
# shift everything to the right and combines what needs to be combined
def shift_right(board):
    global score
    empty = []
    # creating column
    for j in range(4):
        column = []
        for i in range(3,-1, -1):
            if board[i][j] != 0:
                column.append(board[i][j])
        for i in range(1, len(column)):
            if column[i] == column[i-1]:
                column[i] = 0
                column[i-1] *= 2
                score += column[i - 1]
        column = [cell for cell in column if cell != 0]
        # Pad the column with empty cells
        while len(column) < 4:
            column.append(0)
        # Update the board with the new column
        count = 0
        for i in range(3, -1, -1):
            board[i][j] = column[count]
            if column[count] == 0:
                empty.append([i, j])
            count += 1

    return board, empty
# shifting everything down and combining cells
def shift_down(board):
    global score
    empty = []
    # creating the column
    for i in range(4):
        column = []
        for j in range(4):
          if board[i][j] != 0:
            column.append(board[i][j])
        for j in range(1, len(column)):
          if column[j] == column[j-1]:
            column[j-1] *= 2
            score += column[j - 1]
            column[j] = 0
        column = [cell for cell in column if cell != 0]
        # Pad the column with empty cells
        while len(column) < 4:
          column = [0] + column
        # Update the board with the new column
        for j in range(4):
          board[i][j] = column[j]
          if column[j] == 0:
              empty.append([i, j])
    return board, empty
def shift_up(board):
    global score
    empty = []
    # creating column
    for i in range(4):
        column = []
        for j in range(4):
          if board[i][j] != 0:
            column.append(board[i][j])
        for j in range(1, len(column)):
          if column[j] == column[j-1]:
            column[j-1] *= 2
            score += column[j-1]
            column[j] = 0
        column = [cell for cell in column if cell != 0]
        # Pad the column with empty cells
        while len(column) < 4:
          column.append(0)
        # Update the board with the new column
        for j in range(4):
          board[i][j] = column[j]
          if column[j] == 0:
              empty.append([i, j])
    return board, empty
# run the compacter
def compacter():
    global score
    # create the board and random starting positions for the first 2 cells
    score = 0
    board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    x1 = random.randint(0, 3)
    y1 = random.randint(0, 3)
    x2 = random.randint(0, 3)
    y2 = random.randint(0, 3)
    board[x1][y1] = 2
    board[x2][y2] = 2
    draw(board)
    # running the game
    while True:
        f = False
        # choosing wether the new spawned cell is a 2 or a 4
        switch = random.choices([2, 4], [0.7, 0.3])[0]
        if lose(board):
            return score
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    game_over = False
                    break
                if i > 0 and board[i][j] == board[i - 1][j]:
                    game_over = False
                    break
                if i < 3 and board[i][j] == board[i + 1][j]:
                    game_over = False
                    break
                if j > 0 and board[i][j] == board[i][j - 1]:
                    game_over = False
                    break
                if j < 3 and board[i][j] == board[i][j + 1]:
                    game_over = False
                    break
        # checking for which key is pressed
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    board, empty = shift_left(board)
                    f = True
                elif event.key == pygame.K_RIGHT:
                    board, empty = shift_right(board)
                    f = True
                elif event.key == pygame.K_UP:
                    board, empty = shift_up(board)
                    f = True
                elif event.key == pygame.K_DOWN:
                    board, empty = shift_down(board)
                    f = True
                # checking if up down left or right were pressed
                if f:
                    # checking wether are empty cells to add new cells
                    if empty == []:
                        if lose(board):
                            return score
                    else:
                        spot = random.choices(empty)[0]
                        board[spot[0]][spot[1]] = switch
                draw(board)


# wipes the screen and draws the home button
def wipe():
  screen.fill(black)
  pygame.draw.circle(screen, white, (450, 570), 20)
  pygame.draw.rect(screen, red, (440, 560, 20, 20))
#runs the menu
def menu():
  global restart, multi, total, tname, tpoint, username, password, score, total
  wipe()
  # checking wether to reset everything
  if restart:
      multi = 0.5
      score = 0
      restart = False
      # updating the leaderboard
      for i in range(len(tname)):
          if tname[i] == username:
              if total > int(tpoint[i]):
                  tpoint[i] = str(total)
              break
          elif total > int(tpoint[i]):
              tpoint = tpoint[:i] + [str(total)] + tpoint[i:-1]
              tname = tname[:i] + [username] + tname[i:-1]
              break
      write()
      leaderboard()
  # drawing the menu
  multiplyer = fontv2.render(str(multi), True, red)
  screen.blit(multiplyer, (850, 5))
  pygame.draw.rect(screen, red, (150, 30, 600, 420))
  pygame.draw.rect(screen, white, (150, 30, 600, 70), 3)
  pygame.draw.rect(screen, white, (150, 100, 600, 70), 3)
  pygame.draw.rect(screen, white, (150, 170, 600, 70), 3)
  pygame.draw.rect(screen, white, (150, 240, 600, 70), 3)
  pygame.draw.rect(screen, white, (150, 310, 600, 70), 3)
  pygame.draw.rect(screen, white, (150, 380, 600, 70), 3)
  op = font2.render("Instructions", True, white)
  text_rect = op.get_rect()
  square = pygame.Rect((150, 30), (600, 70))
  text_rect.center = square.center
  screen.blit(op, text_rect)
  op = font2.render("Easy", True, white)
  text_rect = op.get_rect()
  square = pygame.Rect((150, 100), (600, 70))
  text_rect.center = square.center
  screen.blit(op, text_rect)
  op = font2.render("Medium", True, white)
  text_rect = op.get_rect()
  square = pygame.Rect((150, 170), (600, 70))
  text_rect.center = square.center
  screen.blit(op, text_rect)
  op = font2.render("Hard", True, white)
  text_rect = op.get_rect()
  square = pygame.Rect((150, 240), (600, 70))
  text_rect.center = square.center
  screen.blit(op, text_rect)
  op = font2.render("Compacter", True, white)
  text_rect = op.get_rect()
  square = pygame.Rect((150, 310), (600, 70))
  text_rect.center = square.center
  screen.blit(op, text_rect)
  op = font2.render("Exit", True, white)
  text_rect = op.get_rect()
  square = pygame.Rect((150, 380), (600, 70))
  text_rect.center = square.center
  screen.blit(op, text_rect)
  pygame.display.update()
  while True:
    #   checking which funtion to call
    for event in pygame.event.get():
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          x, y = pygame.mouse.get_pos()
          if x >=150 and x <= 700:
            if y >= 30 and y < 100:
                instructions()
            elif y >= 100 and y < 170:
                if collecter(8, 8, 10):
                    multi += 0.5
                else:
                    restart = True
                time.wait(2000)
            elif y >= 170 and y < 240:
                if collecter(16, 16, 40):
                    multi += 2.5
                else:
                    restart = True
                time.wait(2000)
            elif y >= 240 and y < 310:
                if collecter(16, 30, 99):
                    multi += 5.5
                else:
                    restart = True
                time.wait(2000)
            elif y >= 310 and y < 380:
                wipe()
                total = float(compacter())
                total *= multi
                total = int(total)
                restart = True
                time.wait(2000)
            elif y >= 380 and y < 450:
              pygame.quit()
              sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                  x, y = pygame.mouse.get_pos()
                  d = ((x - 380)**2 + (y - 570)**2)
                  d = d**(1/2)
                  if round(d) <= 20:
                        menu()

            wipe()
            menu()
#  creating the login screen
def login():
    global aname, acode, tname, tpoint
    # reading from files
    n = open("acount.csv", "r")
    aname = []
    acode = []
    while True:
        text = n.readline()
        text = text[:-1]
        if text == "":
            break;
        comma = text.find(",")
        aname.append(text[:comma])
        acode.append(text[comma + 1:])
    n.close()
    n = open("leaderboard.csv", "r")
    tname = []
    tpoint = []
    while True:
        text = n.readline()
        text = text[:-1]
        if text == "":
            break;
        comma = text.find(",")
        tname.append(text[:comma])
        tpoint.append(text[comma + 1:])
    n.close()
    # drawing options and checking if user want to login or create a new acount
    pygame.draw.rect(screen, red,(100, 200, 700, 50))
    pygame.draw.rect(screen, red,(100, 350, 700, 50))
    n = font2.render("Sign Up", True, white)
    o = font2.render("Login", True, white)
    text_rect = n.get_rect()
    square = pygame.Rect((120, 195), (700, 50))
    text_rect.center = square.center
    screen.blit(o, text_rect)
    text_rect = o.get_rect()
    square = pygame.Rect((80, 345), (700, 50))
    text_rect.center = square.center
    screen.blit(n, text_rect)
    pygame.event.get()
    pygame.display.update()
    while True:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if x >= 100 and x <= 800:
                    if y >= 350 and y <= 400:
                        new()
                    elif y >= 200 and y <= 250:
                        old()
# login the user
def old():
    string = ""
    caption = font2.render("Input Username with a max of 10 charecters", True, white)
    global username, password
    while True:
        screen.fill(black)
        screen.blit(caption, (0, 0))
        pygame.draw.rect(screen, red, (100, 200, 700, 52))
        t = font2.render(string, True, white)
        screen.blit(t, (101, 195))
        if string not in aname:
            taken = fontv2.render("This Username does not exist", True, white)
            screen.blit(taken, (100, 160))
        pygame.event.get()
        pygame.display.update()
        k = key()
        if len(string) < 10 or k == "check" or k == "delete":
            if k == "Invalid":
                pass
            elif k == "check":
                if string in aname:
                    username = string
                    break
            elif k == "delete":
                string = string[:-1]
            else:
                string += k
    string = ""
    caption = font2.render("Input Password with a max of 10 charecters", True, white)
    name = aname.index(username)
    while True:
        screen.fill(black)
        screen.blit(caption, (0, 0))
        pygame.draw.rect(screen, red, (100, 200, 700, 52))
        t = font2.render(string, True, white)
        screen.blit(t, (101, 195))
        if string not in acode[name]:
            taken = fontv2.render("This Password is incorrect", True, white)
            screen.blit(taken, (100, 160))
        pygame.event.get()
        pygame.display.update()
        k = key()
        if len(string) < 10 or k == "check" or k == "delete":
            if k == "Invalid":
                pass
            elif k == "check":
                if string in acode[name]:
                    password = string
                    break
            elif k == "delete":
                string = string[:-1]
            else:
                string += k
    write()
    menu()
#  sign up the user
def new():
    string = ""
    caption = font2.render("Input Username with a max of 10 charecters",True, white)
    global username, password
    while True:
        screen.fill(black)
        screen.blit(caption,(0, 0))
        pygame.draw.rect(screen, red,(100, 200, 700, 52))
        t = font2.render(string, True, white)
        screen.blit(t, (101, 195))
        if string in aname:
            taken = fontv2.render("This Username is taken", True, white)
            screen.blit(taken, (100, 160))
        pygame.event.get()
        pygame.display.update()
        k = key()
        if len(string) < 10 or k == "check" or k == "delete":
            if k == "Invalid":
                pass
            elif k == "check":
                if string not in aname:
                    username = string
                    aname.append(string)
                    break
            elif k == "delete":
                string = string[:-1]
            else:
                string += k
    string = ""
    caption = font2.render("Input Password with a max of 10 charecters",True, white)
    while True:
        screen.fill(black)
        screen.blit(caption,(0, 0))
        pygame.draw.rect(screen, red,(100, 200, 700, 52))
        t = font2.render(string, True, white)
        screen.blit(t, (101, 195))
        pygame.event.get()
        pygame.display.update()
        k = key()
        if len(string) < 10 or k == "check" or k == "delete":
            if k == "Invalid":
                pass
            elif k == "check":
                password = string
                acode.append(string)
                break
            elif k == "delete":
                string = string[:-1]
            else:
                string += k
    write()
    menu()
# write information back to the files
def write():
    global tname, tpoint, aname, acode
    w = open("acount.csv", "w")
    for i in range(len(aname)):
        w.write(aname[i] + "," + acode[i] + "\n")
    w = open("leaderboard.csv", "w")
    for i in range(len(tname)):
        w.write(tname[i] + "," + tpoint[i] + "\n")
# draw the leaderboard
def leaderboard():
    global tname, tpoint, total
    wipe()
    for i in range(len(tname)):
        string = "%-3s%-30s" % (str(i+1) + ".", tname[i])
        leader = fontv2.render(string, True, pale)
        screen.blit(leader, (0, i*42))
        x = fontv2.render(tpoint[i], True, pale)
        screen.blit(x, (500, i * 42))
        x = fontv2.render("Your score: " + str(total), True, pale)
        screen.blit(x, (0, 462))
    pygame.event.get()
    pygame.display.update()
    total = 0
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                  x, y = pygame.mouse.get_pos()
                  d = ((x - 450)**2 + (y - 570)**2)
                  d = d**(1/2)
                  if round(d) <= 20:
                        menu()
# draw instructions
def instructions():
    # wipe the screen and create a home button
    wipe()
    text  = "You must clear e-waste filled areas without exploding upon exploding your multipyer and score will be reset. There are 3 diffrent zones easy, medium, and hard. Easy increase your multiplyer by 0.5, mediu by 2.5, and hard by 5.5. Within the zones the formations of some of the e-waste have created explosive that may threaten your life. Luckly you have a scanner that tells you how many mines are in the nearby 9 cells. To clear a cell left click on it and to mark it as a mine right click on it. After you have cleared your desired number of zones you may enter the compacter and compact e-waste. Simmalar values of e-waste will combine together to create more compact e-waste with a higher value. To return to the menu click the button at the bottom of the screen. Good Luck"
    text_render = minifont.render(text, True, (255, 255, 255))
    # Get the dimensions of the rendered text
    text_width, text_height = text_render.get_size()
    x = 0
    y = 0
    # Check if the width of the text is greater than the width of the screen
    if text_width > 700:
        # Split the text into multiple lines
        words = text.split(" ")
        current_line = ""
        for word in words:
            current_line += word + " "
            cline = minifont.render(current_line, True, (255, 255, 255))
            clinew, current_line_height = cline.get_size()
            if clinew > 700:
                screen.blit(cline, (x, y))
                y += text_height+10
                current_line = word + " "
        screen.blit(cline, (x, y))
    pygame.event.get()
    pygame.display.update()
    # go back to menu
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                  x, y = pygame.mouse.get_pos()
                  d = ((x - 450)**2 + (y - 570)**2)
                  d = d**(1/2)
                  if round(d) <= 20:
                        menu()
login()
# menu()
