import random
from word import words

def get_valid_word(words):
    word = random.choice(word)
    while '-' in word or ' 'in word:
        word = random.choice(words)

    return word 


def hangman
    word = et_valid_word(words)
    word_letters = set(word) #letter in the word
    