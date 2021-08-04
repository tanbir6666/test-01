#print function

def p(Print_item):
    print(Print_item)



#the board of the Game
Game_Board=["-" ,"-" ,"-", "-" ,"-","-","-","-","-"]

###======game Variables ===========######
Which_column_won_info=[]

col_row=[]

winner=None

Game_should_continue=True


Flip_player=False

Now_playing_Player="X"


how_many_move=0

###======game Variables ===========######



#print board

def print_board():
    print(Game_Board[0] ," | ",Game_Board[1]," | ",Game_Board[2])
    print(Game_Board[3] ," | ",Game_Board[4]," | ",Game_Board[5])
    print(Game_Board[6] ," | ",Game_Board[7]," | ",Game_Board[8])



# winner function

def winner_massage():
    
    global winner , Which_column_won_info,col_row
    Massage = "player " + winner + " Won in "+ col_row[0]
    Which_column_won_info.append(Massage)
    print(Which_column_won_info[0])
    p("")
    p("========= GAME OVER =========")




def clear_data():
    global winner, Game_Board,col_row
    winner=None
    Game_Board=["-" ,"-" ,"-", "-" ,"-","-","-","-","-"]
    col_row.clear()




# What to to after win

def finish_game():
    global winner
    print_board()
    if winner:
        winner_massage()
    clear_data()
    exit()






##====  GAME LOGIC  ====############

def column_win_condition():
    global winner,Game_Board
    if Game_Board[0] == Game_Board[3] == Game_Board[6] not in "-":
       col_row.append("col-1")
       winner=Game_Board[0]
    elif Game_Board[1] == Game_Board[4] == Game_Board[7] not in "-":
        col_row.append("col-2")
        winner=Game_Board[1]
    elif Game_Board[2] == Game_Board[5] == Game_Board[8] not in "-":
        col_row.append("col-3")
        winner=Game_Board[2]    


def row_win_condition():
    global winner,Game_Board
    if Game_Board[0] == Game_Board[1] == Game_Board[2] not in "-":
         col_row.append("row-1")
         winner=Game_Board[0]
    elif Game_Board[3] == Game_Board[4] == Game_Board[5] not in "-":
         col_row.append("row-2")
         winner=Game_Board[3]
    elif Game_Board[6] == Game_Board[7] == Game_Board[8] not in "-":
        col_row.append("row-2")
        winner = Game_Board[6]



def diagonals_win_condition():
    global winner,Game_Board
    if Game_Board[0] == Game_Board[4] == Game_Board[8] not in "-":
        col_row.append("Top Left Diagonal")
        winner = Game_Board[0]
    elif Game_Board[2] == Game_Board[4] == Game_Board[6] not in "-":
        col_row.append("Top Right Diagonal")  
        winner = Game_Board[2]  



def tie_or_not():
    global how_many_move
    print(how_many_move , "From tie funtion")
    if how_many_move>=9:
        print("its a Tie Or Draw")
        p("========= GAME OVER =========")
        finish_game()
        Game_should_continue=False



def winner_declared_or_not():
    global winner,Game_should_continue
    if winner:
        Game_should_continue=False
        finish_game()
       

    else:
        Game_should_continue=True
      




def some_one_win_or_not():
    column_win_condition()
    row_win_condition()
    diagonals_win_condition()
    winner_declared_or_not()

  


##====  GAME LOGIC  ====############
def flip_player():
    global Now_playing_Player, Flip_player,how_many_move
    print(how_many_move, " : No Move")
    if Now_playing_Player=="X":
        Now_playing_Player="0"
        Flip_player=False
        p("0 -- Turn Now")
        
    else:
        Now_playing_Player="X"
        Flip_player=True
        p("X -- Turn Now")
        


def add_move(position,player):
    global how_many_move
    Game_Board[position]=player
    how_many_move+=1
    some_one_win_or_not()
    tie_or_not()
    
    


def wrong_move_warning(player):
    print("please Player " + player + " Input a Correct position")


def alreadey_given_move(position,player):
    if Game_Board[position]=="-":
        
        add_move(position,player)
        flip_player()
    elif position>9:
        wrong_move_warning(player)
    elif position is not int(position):
        wrong_move_warning(player)
    else:
        wrong_move_warning(player)





def giving_input():
    global Now_playing_Player
    position = input("Please Input Number Around 1 - 9 :")
    position_ab=int(position)-1
    player=Now_playing_Player
    alreadey_given_move(position_ab, player)











def play_Game():
    while Game_should_continue:
        print_board()
        giving_input()


play_Game()


