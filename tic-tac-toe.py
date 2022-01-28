

def display_board(board):
    print('\n'*100)
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])



#GETTING X,O
def user_input():
    marker=''
    while marker != 'X' and marker != 'O':
        marker=input('Player 1,Choose X or O:').upper()

    if marker=='X':
        return('X','O')
    else:
        return('O','X')


#PLACING INPUT IN POSITION
def placement(board,marker,position):
    board[position]=marker


#WIN CHECK
def win_check(board, mark):
    return ((board[1]== mark and board[2]== mark and board[3]==mark) or #horizontal
            (board[4]== mark and board[5]== mark and board[6]==mark) or
            (board[7]== mark and board[8]== mark and board[9]==mark) or
            (board[1]== mark and board[4]== mark and board[7]==mark) or  #vertical
            (board[2]== mark and board[5]== mark and board[8]==mark) or
            (board[3]== mark and board[6]== mark and board[9]==mark) or
            (board[1]== mark and board[5]== mark and board[9]==mark) or #x
            (board[3]== mark and board[5]== mark and board[7]==mark)) 




#CHECKING SPACE
def space_check(board,position):
    return board[position]==' '



#CHECKING BOARD
def fullboard_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


#PLAYER CHOICE
def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('enter position(1-9):'))

    return position



#RANDOM START
import random
def random_start():
    if random.randint(0,1)==0:
        return 'Player 2'
    else:
        return 'Player 1'


#REPLAY
def replay():
    choice=''
    while choice not in ['Y','N']:
        choice=input('do you want to play again (Y or N):').capitalize()
    
    if choice=='Y':
        return True
    else:
        return False
        


#MAIN

print('WELCOME TO TIC-TAC-TOE')
while True:
    #display empty board
    theboard=[' ']*10
    player1_marker,player2_marker=user_input()
    turn=random_start()
    print(turn + 'will go first')

    playgame=input('Do you want to play the game (y or n):').upper()

    if playgame=='Y':
        gameon=True
    else:
        gameon=False

    #GAMEON
    while gameon:


        if turn=='Player 1':
            #SHOW BOARD
            display_board(theboard)
            #CHOOSE PLACEMENT
            position=player_choice(theboard)
            #PLACE MARKER
            placement(theboard,player1_marker,position)
            #CHECK WON
            if win_check(theboard,player1_marker):
                display_board(theboard)
                print('PLAYER 1 WON!!!')
                gameon=False
            else:   #CHECK TIE
                if fullboard_check(theboard):
                    display_board(theboard)
                    print('TIE')
                    gameon=False
                else:   #NO TIE AND NO WIN ,NEXT PLAYERS TURN
                    turn='Player 2'

         
        

        else:   #PLAYER2

            #SHOW BOARD
            display_board(theboard)
            #CHOOSE PLACEMENT
            position=player_choice(theboard)
            #PLACE MARKER
            placement(theboard,player2_marker,position)
            #CHECK WON
            if win_check(theboard,player2_marker):
                display_board(theboard)
                print('PLAYER 2 WON!!!')
                gameon=False
            else:   #CHECK TIE
                if fullboard_check(theboard):
                    display_board(theboard)
                    print('TIE')
                    gameon=False
                else:   #NO TIE AND NO WIN ,NEXT PLAYERS TURN
                    turn='Player 1'

    if not replay():
        break

        

         
        
