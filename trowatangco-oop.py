#Name: Saint Trowa N. Tangco
#Course/Year/Section: BSCPE 1-2
#This program is called Infinite Tic Tac Toe, which inspired by the Giiker Infinite Tic Tac Toe.
#The rules is the as normal tic tac toe, but with a twist! After 3 turns, a player's symbol dissapears and ensuring that there will be no ties!
#The code of this program is heavily inspired by the video of "Code Coach", "Python TIC TAC TOE Tutorial | Beginner Friendly Tutorial"
#Link to the video, https://youtu.be/dK6gJw4-NCo?si=OaTSPygxyhVavRWW

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentplayer = "X"
winner = None
gamerunning = True

turns = [0] * 9


#To Print the Board
def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2] + "\n"
          + "---------" + "\n"
          + board[3] + " | " + board[4] + " | " + board[5] + "\n"
          + "---------" + "\n"
          + board[6] + " | " + board[7] + " | " + board[8])
    
#Takes the Players' Input
def playersinput(board):
    while True:
        if currentplayer == "X":
            inpt = int(input("Enter a number between 1 to 9! Player (X): "))
        else:
            inpt = int(input("Enter a number between 1 to 9! Player (O): "))
        
        if inpt >= 1 and inpt <=9 and board[inpt - 1] == "-":
            board[inpt - 1] = currentplayer
            turns[inpt - 1] = 6
            break
        
        else:
            if currentplayer == "X":
                print("Try Again, Player (X)")
            
            else:
                print("Try Again, Player (O)")
                
            printboard(board)

#To see how much turn left before the symbol dissapears
def turnscounter():
    global turns
    for i in range(9):
        if turns[i] > 0:
            turns[i] -= 1
            if turns[i] == 0:
                board[i] = "-"
 
 #Checking Horizontally to see if a player wins
def checkingHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = currentplayer
        return True
    
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = currentplayer
        return True
    
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = currentplayer
        return True
    
#Checking Vertically to see if a player wins
def checkingVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = currentplayer
        return True
    
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = currentplayer
        return True
    
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = currentplayer
        return True

#Checking Diagonally to see if a player wins
def checkingDiagonal(board):
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = currentplayer
        return True
    
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = currentplayer
        return True

#Check if 3 of checkers are activated
def checkwin():
    global currentplayer
    if checkingHorizontal(board) or checkingVertical(board) or checkingDiagonal(board):
        winner = currentplayer
        print(f"Theeeeeee Winner issss......" + winner)
        gamerunning = False
        return

#To switch the current player to the next player
def switchplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"
        
while gamerunning:
    printboard(board)
    playersinput(board)
    checkwin()
    if not gamerunning:
        break
    turnscounter()
    switchplayer()

          