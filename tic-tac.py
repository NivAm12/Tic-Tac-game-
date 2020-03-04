import random

def display_board(board): #to show the board
    print('\n'*100) #clear
    print(board[7]+' |'+board[8]+' |'+board[9])
    print('_________')
    print(board[4]+' |'+board[5]+' |'+board[6])
    print('_________')
    print(board[1]+' |'+board[2]+' |'+board[3])
    print('_________')

def player_input(): #set the markers
    marker=0
    while(marker!='X' and marker!='O'):
        marker=input("please take a mark X or O:").upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,marker,pos): #put the current marker on the board
    board[pos]=marker

def win_check(board,marker):
    #rows:
    if(marker==board[7] and marker==board[8] and marker==board[9]):
        return True
    elif(marker==board[4] and marker==board[5] and marker==board[6]):
        return True
    elif(marker==board[1] and marker==board[2] and marker==board[3]):
        return True         
    #cols:
    elif(marker==board[7] and marker==board[4] and marker==board[1]):
        return True
    elif(marker==board[8] and marker==board[5] and marker==board[2]):
        return True
    elif(marker==board[9] and marker==board[6] and marker==board[3]):
        return True         
    #diogonal:
    elif(marker==board[7] and marker==board[5] and marker==board[3]):
        return True
    elif(marker==board[9] and marker==board[5] and marker==board[1]):
        return True       
    else:
        return False                    

def choose_first():
    a=random.randint(1,2)
    if a==1:
        return 'player 1 starting'
    else:
        return 'player 2 starting'    

def space_check(board,pos):
    return board[pos]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    while(1):
        pos=int(input('what is your next position?'))
        if space_check(board,pos):
            return pos
        print('chose a free position')    

def replay():
    ans=input('would you like to play again? Y|N--->')
    return ans=='Y'        

#the game:
while(True):
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] #empty board
    print('welcome to tic tac game!')
    print(choose_first()) #chose who is the first one
    flag=True #player 1 turn
    temp=player_input()#set the markers
    while not full_board_check(board):
        display_board(board)
        if flag:
            marker=temp[0]
            print('player 1 turn')
        else:
            print('player 2 turn')
            marker=temp[1]
        pos=player_choice(board)
        place_marker(board,marker,pos)
        display_board(board)
        if win_check(board,marker):
            print('we have a winner!')
            break
        flag=not flag #switch to the other player
    if not replay():
        break





