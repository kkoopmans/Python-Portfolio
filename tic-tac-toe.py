import os

def display_board(board):
  print(f' {board[0]} | {board[1]} | {board[2]}')
  print('-' * 11)
  print(f' {board[3]} | {board[4]} | {board[5]}')
  print('-' * 11)
  print(f' {board[6]} | {board[7]} | {board[8]}')

def check_valid_space(board, choice):
    '''
    This function will take the board and the chosen location and
    determine whether the player is allowed to play in that space.
    It should both determine whether the space exists (is in the range 
    of possible spaces), and whether the spot is empty. If the play is 
    valid, this function does nothing. If not, it will throw an exception.
    '''
    if 0 <= choice and choice <= 8 and board[choice] == " ":
        pass
    else:
        raise Exception("")
    
    

def choose_space(turn, board):
  ''' 
  This function will ask for input - a number representing the space
  the current player wants to play in. It will call check_valid_space
  to determine if the play is valid. If the play is valid, it will add
  the X or O to the space and return the board. If it's not valid, it will ask again
  '''
  print()
  print(f"It's {turn}'s turn")
  validguess = False
  while not(validguess):
    try:
        choice = int(input("Enter a number for a square:"))
        check_valid_space(board,choice)
        validguess = True
    except:
        print("Invalid Space, try again.")
    
  board[choice] = turn
  return board
  

def check_win(board):
  '''
  This function gets the board state and determines if the game is over.
  It will return a numeric code:
    1 if X wins
    2 if O wins
    0 if no one has won yet.
  '''
  
  if board[0] == "X" and board[1] == "X" and board[2] == "X":
    return 1
  elif board[3] == "X" and board[4] == "X" and board[5] == "X":
    return 1
  elif board[6] == "X" and board[7] == "X" and board[8]== "X":
    return 1
  elif board[0] == "X" and board[3] == "X" and board[6] == "X":
    return 1
  elif board[1] == "X" and board[4] == "X" and board[7] == "X":
    return 1
  elif board[2] == "X" and board[5] == "X" and board[8] == "X":
    return 1
  elif board[0] == "X" and board[4] == "X" and board[8] == "X":
    return 1
  elif board[2] == "X" and board[4] == "X" and board[6] == "X":
    return 1
  elif board[0] == "O" and board[1] == "O" and board[2] == "O":
    return 2
  elif board[3] == "O" and board[4] == "O" and board[5] == "O":
    return 2
  elif board[6] == "O" and board[7] == "O" and board[8]== "O":
    return 2
  elif board[0] == "O" and board[3] == "O" and board[6] == "O":
    return 2
  elif board[1] == "O" and board[4] == "O" and board[7] == "O":
    return 2
  elif board[2] == "O" and board[5] == "O" and board[8] == "O":
    return 2
  elif board[0] == "O" and board[4] == "O" and board[8] == "O":
    return 2
  elif board[2] == "O" and board[4] == "O" and board[6] == "O":
    return 2
  else:
    return 0

def game_over(state):
  '''
  This function is called when the game is over. It will print the results.
  This function does not need to return anything.
  '''
  if state == 1:
    print('The winner is: X!' )
  elif state == 2:
    print('The winner is: O!')
  else:
    print("It's a tie")
  
def pass_turn(turn, turn_num):
  '''
  this function will take the current turn value and "pass" the turn to the next player.
  ie. If turn = "X", this will return "O" and vice versa.
  '''
  if turn == "X":
    return "O", turn_num + 1
  elif turn == "O":
    return "X", turn_num + 1

def take_a_turn(board, turn):
  os.system('clear')
  display_board(board)
  board = choose_space(turn, board)
  state = check_win(board)
  return board, state

#set up
board = ["0","1", "2", "3" , "4" , "5" , "6" , "7" , "8"]
turn = "X"
state = 0
win = 0
turn_num = 1

#welcome
print("Let's Play Tic-Tac-Toe")
display_board(board)
board = [" "," ", " ", " " , " " , " " , " " , " " , " "]
input("Press enter to begin...")

# play
while state == 0:
  board, state = take_a_turn(board, turn)
  if turn_num == 9 or state != 0:
    game_over(state)
    break
  turn, turn_num = pass_turn(turn, turn_num)


# Unit Tests
sample_board = ["X","O"," ","O", "X", "O", "O", "X", "X"]
assert check_win(sample_board) == 1

sample_board = ["O","X"," ","X", "O", "X", "X", "O", "O"]
assert check_win(sample_board) == 2

sample_board = ["O","O","O","X","O","X","X","X"," "]
assert check_win(sample_board) == 2




  
  