import random

while True:
    word_list = ['Banana', 'Strawberry', 'Grape', 'Mango', 'Satsuma']
    word = random.choice(word_list)
    guess = input('Please guess a letter: ')
    
    if len(guess) == 1 and guess.isalpha():
        #print(f'Good guess, your input of "{guess}" is correct!')
        break
    else:
        print('Invalid letter. Please enter a single alphabetical character')

if guess.lower() in word.lower():
    print(f'Good guess! "{guess}" is in the word.')
else:
    print(f'Nope, sorry. "{guess}" is not in the word. Try again.')


#HERE THEY ARE AS FUNCTIONS NOT JUST SHITTY CODE 

word_list = ['Banana', 'Strawberry', 'Grape', 'Mango', 'Satsuma']

word = random.choice(word_list)

def check_guess(guess):
    if len(guess) == 1 and guess.isalpha():
        if guess.lower() in word.lower():
            print(f'Good guess! "{guess}" is in the word.')
        else:
            print(f'Nope, sorry. "{guess}" is not in the word. Try again.')
    else:
        print('Invalid letter. Please enter a single alphabetical character')

def ask_for_input():
    guess = input('Please guess a letter: ')
    check_guess(guess)

ask_for_input()


