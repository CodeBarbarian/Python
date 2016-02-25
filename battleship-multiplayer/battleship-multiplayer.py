# Importing the Operative System module
import os
# Importing the random module
import random
# Importing the time module
import time

""" 
GAME SPECIFIC AUTHOR CONFIGURATION
"""
# Application Name
app_name = "BattleShip Multiplayer"
# Application Version
app_version = "1.3"
# Application Author
app_author = "CodeBarbarian"



# Function to clear the console screen on *nix and windows systems
def clearScreen():
    os.system(['clear', 'cls'][os.name == 'nt'])


"""""""""""""""""""""""""""""""""
GAME SPECIFIC VARIABLES BELOW
"""""""""""""""""""""""""""""""""
# Player boards
player1_board = []
player2_board = []

# Player Names
player1_name = ""
player2_name = ""

# Overall Game Conditions
gameWon = False
gameTurns = 1
gameWinner = ""
gameLoser = ""

# When the game begins in seconds
gameStart_time = 0
# When the game ends in seconds
gameEnd_time = 0

# Player one's ship location
player1_ship_row = 0
player1_ship_col = 0

# Player two's ship location
player2_ship_row = 0
player2_ship_col = 0

# How large should the battlefield be? 
boardColRow = 10

# Ship Character
shipChar = "S"

# Fired character
firedChar = "X"

# Board Character
boardChar = "   "

# Ocean Character
oceanChar = "O"

"""""""""""""""""""""""""""""""""
GAME SPECIFIC DEFINITIONS BELOW
"""""""""""""""""""""""""""""""""
def gameLogo():
    print '''
    ______       _   _   _      _____ _     _        
    | ___ \     | | | | | |    /  ___| |   (_)       
    | |_/ / __ _| |_| |_| | ___\ `--.| |__  _ _ __   
    | ___ \/ _` | __| __| |/ _ \`--. | '_ \| | '_ \  
    | |_/ | (_| | |_| |_| |  __/\__/ | | | | | |_) | 
    \____/ \__,_|\__|\__|_|\___\____/|_| |_|_| .__/  
                                             | |     
                                             |_|

    '''
    print "              Version " + str(app_version)
    print "         Created by " + str(app_author)
    print
    print 


def randomizePosition(board):
    return random.randint(0, len(player1_board) -1)

def printPlayerBoard(board, row, col, boardChar, shipChar):
    board[row][col] = str(shipChar)
    
    for i in board:
        print str(boardChar).join(i)
    board[row][col] = oceanChar

def printPlayerOppositeBoard(board, boardChar):
    for i in board:
        print str(boardChar).join(i)

def acknowledge(player1name, player2name):
    clearScreen()
    gameLogo()
    print
    print
    return raw_input(str(player1name) + "'s turn! " + str(player2name) + ", turn away from the screen!" + " (When ready, hit ENTER)")
 
def acknowledgeFailure():
    return raw_input("To continue press enter...")

def displayMessage(errNumber, playername=""):
    message = {
        1: "Congratz! You sunk " + str(playername) + "'s battleship!",
        2: "We are at sea " + str(playername) + ", why are you targeting at land?",
        3: "You have already shoot there!",
        4: str(playername) + ": Haha! You've missed my battleship!",
        5: str(playername) + "'s board with your fired attempts!",
        6: "Your board with ship location and " + str(playername) + "'s fired attempts!"
    }
    return str(message[errNumber])


"""""""""""""""""""""""""""""""""
GAME SPECIFIC LOGIC
"""""""""""""""""""""""""""""""""
# Appending the vowel oceanChar to the boards
for i in range(boardColRow):
    player1_board.append([str(oceanChar)] * boardColRow)
    player2_board.append([str(oceanChar)] * boardColRow)


# Setting the position of player one's ship
player1_ship_row = randomizePosition(player1_board)
player1_ship_col = randomizePosition(player1_board)

# Setting the position of player two's ship
player2_ship_row = randomizePosition(player2_board)
player2_ship_col = randomizePosition(player2_board)


"""""""""""""""""""""""""""""""""
GAME START
"""""""""""""""""""""""""""""""""
# Clear the screen to make it prettier
clearScreen()
# Print the game logo
gameLogo()

# Set the player names
player1_name = raw_input("Player One's Name: ")
player2_name = raw_input("Player Two's Name: ")

# Begin the take time sequence
gameStart_time = time.time()

# The gameloop
while 1:
    if gameTurns <= 1:
        acknowledge(player1_name, player2_name)
    """ 
    Player One's Gaming Conditions
    """
    clearScreen()
    gameLogo()
    print
    print "Number of turns played: " + str(gameTurns)
    print
    print str(player1_name) + "'s turn!"
    print
    
    print displayMessage(5, player2_name)
    # Print Player 2's Ocean without the ship on it
    printPlayerOppositeBoard(player2_board, boardChar)

    print
    print
    print displayMessage(6, player2_name)
    # Print Player 1's Ocean with ship on it
    printPlayerBoard(player1_board, player1_ship_row, player1_ship_col, boardChar, shipChar)
    # General Game Conditions
    print
    print
    player1_guessedRow = input(str(player1_name) + " Guess Row: ")
    player1_guessedCol = input(str(player1_name) + " Guess Col: ")

    if player1_guessedRow == player2_ship_row and player1_guessedCol == player2_ship_col:
        print displayMessage(1, player2_name)
        gameWon = True
        gameWiner = str(player1_name)
        gameLoser = str(player2_name)
        break
    else:
        if (player1_guessedRow < 0 or player1_guessedRow >= boardColRow) \
        or (player1_guessedCol < 0 or player1_guessedCol >= boardColRow):
            print
            print displayMessage(2)
            print
            acknowledgeFailure()
            acknowledge(player2_name, player1_name)
        elif player2_board[player1_guessedRow][player1_guessedCol] == str(firedChar):
            print
            print displayMessage(3)
            print
            acknowledgeFailure()
            acknowledge(player2_name, player1_name)
        else:
            print
            print displayMessage(4, player2_name)
            print
            acknowledgeFailure()
            player2_board[player1_guessedRow][player1_guessedCol] = str(firedChar)
            acknowledge(player2_name, player1_name)

    """ 
    Player Two's Gaming Conditions
    """
    clearScreen()
    gameLogo()
    print
    print "Number of turns played: " + str(gameTurns)
    print
    print str(player2_name) + "'s turn!"
    print

    print displayMessage(5, player1_name)
    # Print Player 2's Ocean without the ship on it
    printPlayerOppositeBoard(player1_board, boardChar)

    print
    print
    print displayMessage(6, player1_name)
    # Print Player 1's Ocean with ship on it
    printPlayerBoard(player2_board, player2_ship_row, player2_ship_col, boardChar, shipChar)
    # General Game Conditions
    print
    print
    player2_guessedRow = input(str(player2_name) + " Guess Row: ")
    player2_guessedCol = input(str(player2_name) + " Guess Col: ")
    if player2_guessedRow == player1_ship_row and player2_guessedCol == player1_ship_col:
            print displayMessage(1, player1_name)
            gameWon = True
            gameWinner = str(player2_name)
            gameLoser = str(player1_name)
            break
    else:
        if (player2_guessedRow < 0 or player2_guessedRow >= boardColRow) \
        or (player2_guessedCol < 0 or player2_guessedCol >= boardColRow):
            print
            print displayMessage(2)
            print
            acknowledgeFailure()
            acknowledge(player2_name, player2_name)
        elif player1_board[player2_guessedRow][player2_guessedCol] == str(firedChar):
            print
            print displayMessage(3)
            print
            acknowledgeFailure()
            acknowledge(player2_name, player2_name)
        else:
            print
            print displayMessage(4, player1_name)
            print
            acknowledgeFailure()
            player1_board[player2_guessedRow][player2_guessedCol] = str(firedChar)
            acknowledge(player2_name, player2_name)
        gameTurns += 1


if gameWon:
    # End the take time sequence
    gameEnd_time = time.time()
    # Print congratulation message
    print "Congratulations " + str(gameWinner) + " for shooting down " + str(gameLoser) + "'s ship! in " + str(gameTurns) + " turns!"
    print
    # Print game time
    print "The game took, " + str(gameEnd_time - gameStart_time) + " seconds to play!"


