import random
from words import words 
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' 'in word:
        word = random.choice(words)

    return word 


def hangman(): 
    word = get_valid_word(words)
    word_letters = set(word) #letter in the word
    alphabet = set(string.ascil_uppercase)
    used_letter = set() # what the user has guessed

    # getting user input
    while len(word_letter) > 0:
        print('you have used these letter:', ' '.join(used_letter))

        # what current word is (ie w-r d)
        word_list = (letter if letter in used_letter else '-' for letter in word)
        print('current word:  ',' '.join(word_list))
              
    user_letter = input('guess a the a latter:'). upper()
    if user_letter in alphabet - used_letter:
       user_letter.add(user_latter)
       if user_letter in word_letters:
          word_letter.remove(user_letter)

    elif user_letter in used_letter:
         print('you have already used that character. please try again') 

    else:
        print('invalid character. please try again')          

hangman()



   
 