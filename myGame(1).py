def is_valid_move(board, row, column, direction):
    row-=1
    column-=1
    try:
        if board[row][column]=='@':
            if direction==1 and board[row-1][column]=='@' and board[row-2][column]=='-':
                return True
            if direction==2 and board[row+1][column]=='@' and board[row+2][column]=='-':
                return True
            if direction==3 and board[row][column-1]=='@' and board[row][column-2]=='-':
                return True
            if direction==4 and board[row][column+1]=='@' and board[row][column+2]=='-':
                return True
            else:
                return False
        else:
            return False
    except:
        return False
    """ checks move validity
	This method checks whether a specific move (column + row + direction) is
	valid within a specific board configuration.  In order for a move to be
	a valid: 1)there must be a peg at position row, column within the board,
	2)there must be another peg neighboring that first one in the specified
	direction, and 3)there must be an empty hole on the other side of that
	neighboring peg (further in the specified direction).  This method
	only returns true when all three of these conditions are met.  If any of
	the three positions being checked happen to fall beyond the bounds of 
	your board array, then this method should return false.  Note that the 
	row and column parameters here begin with one, and may need to be 
	adjusted if your programming language utilizes arrays with zero-based 
	indexing.
	
	- board: the state of the board that moves must be legal on.
	- row: the vertical position of the peg proposed to be moved.
	- column: the horizontal position of the peg proposed to be moved.
	- direction: the direction proposed to move/jump that peg in.
	- return true when the proposed move is legal, otherwise false.
    """

def perform_move(board, row, column, direction):
    row-=1
    column-=1
    if board[row][column]=='@':
        if direction==1 and board[row-1][column]=='@' and board[row-2][column]=='-':
            board[row][column]='-'
            board[row-1][column]='-'
            board[row-2][column]='@'
        if direction==2 and board[row+1][column]=='@' and board[row+2][column]=='-':
            board[row][column]='-'
            board[row+1][column]='-'
            board[row+2][column]='@'
        if direction==3 and board[row][column-1]=='@' and board[row][column-2]=='-':
            board[row][column]='-'
            board[row][column-1]='-'
            board[row][column-2]='@'
        if direction==4 and board[row][column+1]=='@' and board[row][column+2]=='-':
            board[row][column]='-'
            board[row][column+1]='-'
            board[row][column+2]='@'
    return board
    
    """ applies move to a board 
	The parameters of this method are the same as those of the isValidMove()
	method.  However this method changes the board state according to this
	move parameter (column + row + direction), instead of validating whether
	the move is valid.  If the move specification that is passed into this
	method does not represent a legal move, then do not modify the board.
	
	- board: the state of the board will be changed by this move.
	- row: the vertical position that a peg will be moved from.
	- column: the horizontal position that a peg will be moved from.
	- direction: the direction of the neighbor to jump this peg over.
	- return the updated board state after the specified move is taken.
    """

def count_pegs_remaining(board):
    num=0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=='@':
                num+=1
    return num
    """ returns the number of pegs left on a board 
	This method counts up the number of pegs left within a particular board 
	configuration, and returns that number.
	
	- board: the board that pegs are counted from.
	- return the number of pegs found in that board.
    """

def count_moves_available(board):
    legal=0
    for i in range(len(board)):
        for j in range(len(board)):
            for k in range(1,5):
                result= is_valid_move(board, i, j, k)
                if result==True:
                    legal+=1
    return legal
                    
    """ returns the number of possible moves available on a board 
	This method counts up the number of legal moves that are available to be
	performed in a given board configuration.
	
	HINT: Would it be possible to call the isValidMove() method for every
	direction and from every position within your board?  Counting up the
	number of these calls that return true should yield the total number of
	moves available within a specific board.
	
	- board: the board that possible moves are counted from.
	- return the number of legal moves found in that board.
    """
def read_valid_move(board):
    column=read_valid_int("Choose the COLUMN of a peg you'd like to move:", 1, len(board[0]))
    row=read_valid_int("Choose the ROW of a peg you'd like to move:", 1, len(board))
    direction=read_valid_int("Choose a DIRECTION to move that peg 1) UP, 2) DOWN, 3) LEFT, or 4) RIGHT:", 1, 4)
    validity=is_valid_move(board, row, column, direction)
    if validity==False:
        print("Your choice does not constitute a legal move. Please try again")
        choice=read_valid_move(board)
    else:
        choice=[column,row,direction]
    return choice
    
    """ reads a single peg jump move in from the user 
	This method is used to read in and validate each part of a user’s move 
	choice: the row and column that they wish to move a peg from, and the 
	direction that they would like to move/jump that peg in.  When the 
	player’s row, column, and direction selection does not represent a valid
	move, your program should report that their choice does not constitute a
	legal move before giving them another chance to enter a different move.  
	They should be given as many chances as necessary to enter a legal move.
	The array of three integers that this method returns will contain: the 
	user’s choice of column as the first integer, their choice of row as the
	second integer, and their choice of direction as the third.
	
	- board: the state of the board that moves must be legal on.
	- return the user's choice of column, row, and direction representing
	  a valid move and store in that order with an array.
    """

def display_board(board):
    for i in range(len(board[0])+1):
        print(i,end='')
    print('')
    for i in range(len(board)):
        print(i+1,end='')
        for j in range(len(board[i])):
            print(board[i][j],end='')
        print()
        
    """ prints out the contents of a board for the player to see 
	This method prints out the contents of the specified board using @s to 
	represent pegs, -s to represent empty hole, and #s to represent empty 
	positions that are neither pegs nor holes.  In addition to this, the 
	columns and rows of this board should be labelled with numbers starting 
	at one and increasing from left to right (for column labels) and from 
	top to bottom (for row labels).  See the Sample Runs for examples of how
	these labels appear next to boards with different dimensions.
	
	- board: the current state of the board being drawn.
    """

def create_board(board_type):
    
    if board_type==1:
        board=[["#","#","#","@","@","@","#","#","#"],["#","#","#","@","@","@","#","#","#"],["@","@","@","@","@","@","@","@","@"],["@","@","@","@","-","@","@","@","@"],["@","@","@","@","@","@","@","@","@"],["#","#","#","@","@","@","#","#","#"],["#","#","#","@","@","@","#","#","#"]]
    elif board_type==2:
        board=[["#","-","@","@","-","#"],["-","@","@","@","@","-"],["@","@","@","@","@","@"],["@","@","@","@","@","@"],["-","@","@","@","@","-"],["#","-","@","@","-","#"]]
    elif board_type==3:
        board=[["#","#","#","-","@","-","#","#","#"],["#","#","-","@","@","@","-","#","#"],["#","-","@","@","-","@","@","-","#"], ["-","@","@","@","@","@","@","@","-"]]
    elif board_type==4:
        board=[["-","-","-","-","-"],["-","@","@","@","-"],["-","-","@","-","-"],["-","-","@","-","-"],["-","-","-","-","-"]]
    
    return board

    """ returns a list of lists initialized according to a specific board type 
	This method creates, initializes, and then returns a rectangular two 
	dimensional array of characters according to the specified boardType.  
	Initial configurations for each of the possible board types are depicted
	below.  Note that pegs are displayed as @s, empty holes are displayed as
	-s, and extra blank positions that are neither pegs nor holes within 
	each rectangular array are displayed as #s.
	
	- boardType: 1-4 indicating one of the following initial patterns:
	  1) Cross
	    ###@@@###
	    ###@@@###
	    @@@@@@@@@
	    @@@@-@@@@
	    @@@@@@@@@
	    ###@@@###
	    ###@@@###
	    
	  2) Circle
	    #-@@-#
	    -@@@@-
	    @@@@@@
	    @@@@@@
	    -@@@@-
	    #-@@-#
	    
	  3) Triangle
	    ###-@-###
	    ##-@@@-##
	    #-@@-@@-#
	    -@@@@@@@-
	    
	  4) Simple T
	    -----
	    -@@@-
	    --@--
	    --@--
	    -----
	    
	return the fully initialized two dimensional array.
    """

def read_valid_int(prompt, min, max):
    print(prompt)
    a=int(input())
    if a>=min and a<=max:
        return a
    else:
        print("Please input an integer between",min," and ",max)
        a=read_valid_int(prompt, min, max)
        return a
        
    """ returns a valid integer from the user 
	This method is used to read in all inputs from the user.  After printing
	the specified prompt, it will check whether the user’s input is in fact
	an integer within the specified range.  If the user’s input does not 
	represent an integer or does not fall within the required range, print
	an error message asking for a value within that range before giving the
	user another chance to enter valid input.  The user should be given as
	many chances as they need to enter a valid integer within the specified
	range.  See the Sample Runs to see how these error messages should be 
	phrased, and to see how the prompts are repeated when multiple invalid 
	inputs are entered by the user.
	
	- prompt: message describing what the user is expected to enter.
	- min: the smallest valid integer that the user may enter.
	- max: the largest valid integer that the user may enter.
	- return the valid integer between min and max entered by the user.	
    """

def main():
                          
    welcome=" WELCOME TO CS300 PEG SOLITAIRE!\n===============================\nBoard Style Menu\n1) Cross\n2) Circle\n3) Triangle\n4) Simple T\nChoose a board style:"
    board_type=read_valid_int(welcome, 1, 4)
    board=create_board(board_type)
    count=0
    legal=True
    while(count!=1):
         if legal==True:
            display_board(board)
         choice=read_valid_move(board)
         legal=is_valid_move(board, choice[1],choice[0],choice[2])
         if legal==True:
              board=perform_move(board,choice[1],choice[0],choice[2])
         else:
             print("Moving a peg from row", choice[1]," and column ",choice[0]," ",choice[2]," is not currently a legal move.") 
         peg=count_pegs_remaining(board)
         if peg==1:
             print("Congrats, you won!")             
             count=1
             break
         moves=count_moves_available(board)
         if moves==0:
             print("It looks like there are no more legal moves.  Please try again.")              
             count=1
             break
    print("\n==========================================\nTHANK YOU FOR PLAYING CS300 PEG SOLITAIRE!")          
    
    """ drives the entire game application 
	This method is responsible for everything from displaying the opening 
	welcome message to printing out the final thank you.  It will clearly be
	helpful to call several of the following methods from here, and from the
	methods called from here.  See the Sample Runs below for a more complete
	idea of everything this method is responsible for.
    """
if __name__ == "__main__":
	main()
