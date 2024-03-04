import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = int(num_lives)
        self.word = random.choice(self.word_list)
        self.word_guessed = len(self.word) * ['_']
        self.num_letters = int(len(self.word))
        self.list_of_guesses = []


    def ask_for_input(self):
        while True:
            guess = input('Please guess a letter: ')
            if len(guess) != 1 or guess.isdigit():
                print('Invalid letter. Please enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

            # Print the current state of the word after each guess
            print('Current word:', ' '.join(self.word_guessed))
            print('Unguessed letters:', ' '.join(['_' if letter not in self.list_of_guesses else '' for letter in self.word]))

            if '_' not in self.word_guessed:
                print('Congratulations. You won the game!')
                break
            elif self.num_lives == 0:
                print('You lost!')
                break
            elif self.num_letters == 0:
                break  # added this line to break out when all letters are guessed

    def check_guess(self, guess):
        if guess.lower() in self.word.lower():
            print(f'Good guess! "{guess}" is in the word.')
            for i in range(len(self.word)):
                letter = self.word[i]
                if letter.lower() == guess.lower():
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, "{guess}" is not in the word.')
            print(f'You have {self.num_lives} lives left.')

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break


word_list = ['Banana', 'Strawberry', 'Grape', 'Mango', 'Satsuma']
play_game(word_list)




