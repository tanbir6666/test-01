# game Board of Backend
# display Game Board
# Play Game
# handle turn

# check win
    #check rows
    # check Columns
    # check diagonals

# check tie

# flip player
# -------Global Variable
# -------Global Variable


Board = ["-", "-", "-", "-", "-", "-", "-", "-", "-",]
#'Board' will display Board Of the game


game_still_going=True;
# 'game_still_going' will conform that Game is over Or not


sd=1
# 'sd' is a random word . It define which player is now playing
# 1 means it's X Turn &             0 means it's '0' Turn


Each_move=[]
# if any play his move this list will add that move. If player press '4' than "Each_move will Record it and "
# in future this list will let us know that it's a Draw or not By counting the length of this list.
# this game is a "9" move game . if after 9 move no one wins that this must be a tie. and that's the logic





winner=None
# -------Global Variable
# -------Global Variable


def displayBoard():
    #this function will show the area for possible visualization

    print(Board[0], " | ", Board[1], " | ", Board[2])
    print(Board[3], " | ", Board[4], " | ", Board[5])
    print(Board[6], " | ", Board[7], " | ", Board[8])


def Reset_board():
    #this function will Reset the game if the win or tie condition is true

    global Board,winner
    #each time we use a Global Variable, we need to define that We are useing a Global Variable. Else this will take value only inside of that function
    # in python each value is a Let value of Javascript. like that.. not 100% . not even 80% 

    displayBoard()
    Board = ["-", "-", "-", "-", "-", "-", "-", "-", "-", ]
    #Board need to be Clean if the game is reset
    #Board need to reset if exit() is not exist

    print("======GAME OVER=======")
    print("===== ", winner, "Won ======")
    # this massage will appere when game will restart

    winner=None
    #winner need to reset if exit() is not exist
    exit()
    #exit will immediately take out of the while loop



def NeedTo_reset_or_not():
    # NeedTo_reset_or_not() function will deside that Need to Reset or not

    global game_still_going, winner
    # we are using global variable so just Define it like before

    if winner=="X" or winner=="0":
        #if "X" or "0" is the winner then the must need a reset
        #and the while loop need to stop

        game_still_going=False
        #while loop is going on this condition that "game_still_going"=True
        #But Now "game_still_going"=False . Now loop will stop

        Reset_board()
        #calling the Reset Board

def flip_player():
    # flip_player() will Change player after each correct move
    global sd


    if sd == 1:
              # its seems that Now player 1="X" is playing
              # so now it's time to play a move for next player
              #   
              sd = 0
              #now sd=0 so player is now "0"
    else:       
              #sd==0
              # so need to change the other player
              # let's change it
                
              sd = 1
              # now player one will play his move




def play_game():
    #this is the main() function
    # display_board
    # display board will appere  if someone play the game 

    while game_still_going:
        # this is the loop for all thing
        # if game_still_going is True then play the game By showing the board of the game 
        
        displayBoard() 

        current_player="Player X"
        # I am trying to pass data about which player is now playing
         
        if sd==1:
            # I am telling the computer that sd=1 means "Player X"
           current_player = "Player X"
        else:
           # I am telling the computer that sd=1 means "Player Zero"
           current_player="Player Zero"

        handle_turn(current_player)
        # after giving the info of "current_player" Now let's pass that value inside the function
        #current_player define the player whose Turn was that

        
        Check_game_over_or_NOT()
        # By "Check_game_over_or_NOT()"  after each turn Check that the game is over or not

        
        flip_player()
        # after checking Check_game_over_or_NOT() Flip the Turn


def Check_wrong_turn(move_of_player, current_player):
    # this function will check  it's a wrong move or not
    # wrong move means somebaddy play a move which are already played
    #  
    global Each_move
    # print(len(Each_move))
    Wrong_Move=False
    # at first computer wil know that move is correct
    # But it need to go threw some condition

    if (int(move_of_player))<10 :
        # if 'move_of_player' is under 10 then it means player 
        for moves in Each_move:
            if move_of_player == moves:
                print("============ Wrong Move ===========")
                print("========= please Try Again ========")
                Wrong_Move=True
                tie_Conform()
            else:
                Wrong_Move=False
        if Wrong_Move==False:
            
            Each_move.append(move_of_player)
            addPosition_to_the_board(move_of_player, current_player)
            tie_Conform()
        elif Wrong_Move==True:
            handle_turn(current_player)
    else:
        #print("int(move_of_player)==9")
        print("============ Wrong Move ===========")
        print("========= please Try Again ========")
        Wrong_Move = True
        tie_Conform()
        handle_turn(current_player)
      
def addPosition_to_the_board(position, current_player):
        if position:
            position = int(position)-1
        plX = "Player X"
        plZ = "Player Zero"

        if current_player==plX:
                Board[position] = "X"
                
                
               
            
        elif current_player == plZ:
                Board[position] = "0"
               
               
               
        else:
            return None  

def handle_turn(current_player):
    position=input("Choose a position from 1-9 : ")
    #print(position)
    #print(type(position))

    #while loop is better do coding faster
    # while position not in ["1","2","3","4","5","6","7","8",9]:
          #position=input("Choose a position from 1-9 : ")


    if position == None or str(position) or position == "" or position == False:
        position==563435
        Check_wrong_turn(position, current_player)

    else:

        Check_wrong_turn(position, current_player)
    

    
         
    

    
    


def Check_game_over_or_NOT():
    global winner
    # Who won the game will define by this Function
    Check_if_win()
    #print(winner)
    # Check Game is the game Round Tie Or not
    Check_if_tie()
    #print("checked Check_game_over_or_NOT")
    NeedTo_reset_or_not()

def Check_if_win():
    # check Rows
    # check Columns
    # Check  diagonals
    #print("checked Check_if_win")
    global winner
    if Check_rows():
        winner = Check_rows()
        #print(winner)
        game_still_going = False
        return winner
    elif Check_column():
        winner = Check_column()
        game_still_going = False
        #print(winner)
        return winner
    elif Check_diagonals():
        winner = Check_diagonals()
        game_still_going=False
        #print(winner)
        return winner
    else:
        print("nothing Found")
    
def Check_rows():
    #this will give the computer information About the Board Pattern List item
    # if X won
       
    if Board[0] == Board[1] == Board[2]:
        # X X X
        # 0 0 0
        # 0 0 0
        return Board[0]
    elif Board[3] == Board[4] == Board[5]:
        # 0 0 0
        # X X X
        # 0 0 0
        return Board[3]
    elif Board[6] == Board[7] == Board[8]:
        # 0 0 0
        # 0 0 0
        # X X X
        return Board[6]
       
def Check_column():
    
    if Board[0] == Board[3] == Board[6]:
        # X 0 0
        # X 0 0
        # X 0 0
        return Board[0]
    elif Board[1] == Board[4] == Board[7]:
        # 0 X 0
        # 0 X 0
        # 0 X 0
        return Board[1]
    elif Board[2] == Board[5] == Board[8]:
        # 0 0 X
        # 0 0 X
        # 0 0 X
        return Board[2]


def Check_diagonals():
    if Board[0] == Board[4] == Board[8]:
        # X 0 0
        # 0 X 0
        # 0 0 X
        return Board[0]
    elif Board[2] == Board[4] == Board[6]:
        # 0 0 X
        # 0 X 0
        # X 0 0
        return Board[2]
    




def tie_Conform():
        global Each_move, winner, game_still_going

        # this game has only have 9 moves
        # so Game Must over after 9 moves 
        
        if len(Each_move) >= 9:
            print("Tie Conformed")
            winner = "It's a Draw No one "
            game_still_going = False
            Reset_board()


def Check_if_tie():
    #print("Tie Or Not")
    # check Rows
    # check Columns
    # Check  diagonals

    # ****This thing is useless

    global Each_move,winner
   


play_game()
