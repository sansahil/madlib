import random
from words import words
import string


def get_vaild_word(words):
    word = random.choice(words)  #randomly chooses something from the list
    while '-' in word or ' ' in word:
          word = random.choice(words)

    return word


def hangman():
     word = get_vaild_word(words)
     word_letters = set(word) # letter in the word
     alphabet = set (string.ascii_uppercase)
     used_letter = set() # what the user has guessed

     #getting user input
     while len (word_letters) > 0:
           #letters used
           #' '.join({'a' ,'b' , 'cd'}) -- 'a b cd '
           print('you have used these letters: ',' '.join(used_letters))
                 
           # what current word is (ie W- R D)
           word_list = [letter if letter in used_letters else '-' for letter in word]
           print('current word: ', ' '.join(word_list))

           used_letter = input('guess a letter: ').upper()
           if user_letter in alphabet - used_letters:
              user_letters.add(user_letter)
              if used_letter in word_letters:
                 word_letters.remove(used_letter)   

           elif user_letter in used_letters:
                 print('you have already used that character. please try again.')

           else:
                print('invalid character.please try again.')
           

hungam()
       


    
