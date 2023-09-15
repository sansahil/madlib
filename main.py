import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
          guess= int(input(f'Guess a number between 1 and {x}:'))
          if guess < random_number:
             print('sorry,guess again.too low.')
          elif guess > random_number:
             print('sorry,guess again.too high.')

    print(f'yay congrats. you have guessed the number {random_number} correctly!!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
           guess = random.randint(low,high)
        else:
           guess = low # could also be high b/c low =high
        feedback = input(f'is{guess} too high (h),too low(l), or correct (c)?? '). lower()
        if feedback =='h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'yay! the cpmputer guessed your number,{guess}, correctly!')
guess(10)




