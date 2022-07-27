############## Milestone Project    #####################
# from Ipython.display import clear_output 
import os
# this function displays the board.
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
invalid_index = []   #to avoid placing of two inputs at one same index.

def display_board(board):
    # clear_output()
    # print('\n'*100)
    os.system('cls')  #this is to clear the previous board displayed earlier.
    print("   |"+"   |")
    print(" "+board[7]+" | "+board[8]+" | "+board[9])
    print("   |"+"   |")
    print("-----------")
    print("   |"+"   |")
    print(" "+board[4]+" | "+board[5]+" | "+board[6])
    print("   |"+"   |")
    print("-----------")
    print("   |"+"   |")
    print(" "+board[1]+" | "+board[2]+" | "+board[3])
    print("   |"+"   |")


# This function assigns the appropriate marker to each player.
def player_marker():
    marker = " "
    while marker not in ['X','O']:
        marker = input("Player1: Please select a marker..........X or O: ")
        if marker not in ['X','O']:
            print("Please enter a valid marker to play!!")
    player1 = marker
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    return player1,player2       # <--returns a tuple.-->



def user_input():    #user input with surity that one space doesn't get repeated more than once
    index_choice = -1
    while index_choice not in [1,2,3,4,5,6,7,8,9] or index_choice in invalid_index:
        index_choice = int(input("Please enter an index to place your marker there!: "))
        if index_choice not in range(1,10):
            print("Please enter a valid index to put your marker there!")
            continue
        elif index_choice in range(1,10) and index_choice in invalid_index:
            print("This space has already been occupied !!")
            continue
        elif index_choice in range(1,10) and index_choice not in invalid_index:
            invalid_index.append(index_choice)
        else:
            print("Invalid input!!")
        #print(index_choice)    
        return index_choice

def input_replacement_player1(board,position):
    board[position] = player1_marker
    return board

def input_replacement_player2(board,position):
    board[position] = player2_marker
    return board

#winning function
def winner(board):      #only one set of if else can be used but this is more visible.
    if board[1]==board[2]==board[3]==player1_marker:
        print("Player1 has won the match")
        return True
    elif board[1]==board[2]==board[3]==player2_marker: 
        print("Player2 has won the match")
        return True
    elif board[4]==board[5]==board[6]==player1_marker:
        print("Player1 has won the match")
        return True
    elif board[4]==board[5]==board[6]==player2_marker:
        print("Player2 has won the match")
        return True
    elif board[7]==board[8]==board[9]==player1_marker:
        print("Player1 has won the match")
        return True
    elif board[7]==board[8]==board[9]==player2_marker:
        print("Player2 has won the match")
        return True
    elif board[1]==board[4]==board[7]==player1_marker:
        print("Player1 has won the match")
        return True
    elif board[1]==board[4]==board[7]==player2_marker:
        print("Player2 has won the match")
        return True
    elif board[2]==board[5]==board[8]==player1_marker:
        print("Player1 has won the match")
        return True
    elif board[2]==board[5]==board[8]==player2_marker:
        print("Player2 has won the match")
        return True
    elif board[3]==board[6]==board[9]==player1_marker:
        print("Player1 has won the match")
        return True
    elif board[3]==board[6]==board[9]==player2_marker:
        print("Player2 has won the match")
        return True
    elif board[1]==board[5]==board[9]==player1_marker:
        print("Player1 has won the match")
        return True
    elif board[1]==board[5]==board[9]==player2_marker:
        print("Player2 has won the match")
        return True
    elif board[3]==board[5]==board[7]==player1_marker:
        print("Player1 has won the match")
        return True
    elif board[3]==board[5]==board[7]==player2_marker:
        print("Player2 has won the match")
        return True


#tie
def tie(board):
    if ' ' in board and not winner(board):
        return False
    else:
        print("TIE!!")
        return True


#continue playing
def gameon_choice():
    global board
    global invalid_index
    game_choice = "wrong"
    while game_choice not in ['Y','N']:
        game_choice = input("Would you like to continue playing the game? Enter Y or N: ")
        if game_choice not in ['Y','N']:
            print("Please enter a valid input i.e., Y or N")
    if game_choice == "Y":
        board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        invalid_index = []
        return True
    else:
        return False

game_on = True
while game_on:
    display_board(board)
    player1_marker,player2_marker = player_marker()
    print("The player1 is playing as: {}".format(player1_marker))
    print("The player2 is playing as: {}".format(player2_marker))
    while not winner(board) and not tie(board):  #not operator doesn't execute the function.
        position = user_input()
        #print(position)
        board = input_replacement_player1(board,position)
        display_board(board)
        if winner(board):
            break
        position = user_input()
        board = input_replacement_player2(board,position)
        display_board(board)
    if winner:
        print("Congrats")
    else:
        tie(board)
        print("Tie")
    game_on = gameon_choice()
