import math
import random

class player:
   def __init__(self, letter):
       #letter is x or o
       self.letter = letter
    
    # we want all players to get their next move given a game
   def get_moves(self,game):
        pass

class randomcomputerplayer(player):
      def __inti__(self, letter):
          supper()._inti_(letter)
        
      def get_move(self, game):
           # gwt a random vaild spot for our next move
           square = random.choice(game.available_moves())
           return square

class Humanplayer(player):
      def __inti__(self, letter):
         square()._init_(letter) 

      def get_move(self, game):
           vaild_square = False
           val = None
           while not vaild_square:
               square = input(self.letter + '\' turn. input move (0-9):')
               # we're going to check that this is correct value by tring to cast
               # it to an integer, and if it's not, tjen we say its invalid
               # if that spot is npot available on the board,we also say its invalid
               try:
                  val = int(square)
                  if val not in game.availble_moves():
                     raise ValueError
                  vaild_square = True cd  # if these are successful, then yay !
               except ValueError:
                    print('invalid square. try again.')     
                