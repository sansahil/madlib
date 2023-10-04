from player import Humanplayer, randomcomputerplayer

class tictactoe:
    def __init__(self):
        self.bord = [' 'for _ in range(9)]  # we will use a single list to rep 3x3 board
        self.current_winner = None # keep track of winner !
    
    def print_board(self):
        #this is just getting the rows
        for row in [self.board[i*3:(i+1)*3]for i in range(3)]:
            print('|'+' |'.join(row)+ ' |')

    @staticmethod
    def print_board_num():
        #0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i)for i in range(j+1, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| '+' | '.join(row) + ' |')

    def availble_moves(self):
        return [i for i, spot in enumerate(self.bord) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.bord
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # if vaild move, then make (assign square to letter)
        # then return ture. if invalid, return false
        if self.bord[square] == ' ':
            self.bord[square] = letter 
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in arow anywhere..we have to cheak all of these!
        # first let's cheak the row
        row_ind = square // 3 
        row = self.board[row_ind*3 : (row_ind +1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # cheak column
        col_int = square % 3
        column = [self.board[col_int+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return Ture
        
        # cheake diagonals
        # but only if the sqare is sn even number (0,2,4,6,8)
        # these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal = [self.board[i] for i in [0,4,8]] # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                 return Ture 
            diagonal = [self.board[i] for i in [0,4,6]] # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                 return Ture 
            
        # if all of these fail
        return false    
         
def play(game, x_player, o_player, print_game=True):
    # return the winner of the game (the letter)! or none for tie
    if print_game:
        game.print_board_num()

    letter = 'x' # starting letter
    # iterate while the game still has empty square
    # (we dont\'t have to worry about winner because we'll just return that
    #  which breaks the loop)
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == '0':
            square = o_player.get_move(game) 
        else:
            square = x_player.get_move(game) 

            # let's define a function to make a move!  
            if game.make_move(square, letter):
                if print_game:
                    print_(letter + f' make a move to square {square}')
                    game.print_board()
                    print('') #just empty line

                if game.current_winner:
                    if print_game:
                        print(letter + ' wins!')
                    return letter   


                # after we made our move, we need to alternate letters
                letter = 'o' if letter == 'x' else 'x' # switches player
                
            if print_game:
                print('it\'s a tie!') 

if __name__ ==  '__main__': 
    x_player = Humanplayer('x')       
    o_player = randomcomputerplayer('o')
    t = tictactoe()
    play(t, x_player, o_player, print_game=True)
                 
                    
                
                            

            

