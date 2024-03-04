import random 

class Hangman: 
    def __init__(self, word_list, num_lives=5):
        self.word_list = ['Banana', 'Strawberry', 'Grape', 'Mango', 'Satsuma']
        self.num_lives = int(num_lives)
        self.word = random.choice(word_list)
        self.word_guessed=len(word) * ['_']
        self.num_letters = int(len(self.word))
        self.list_of_guesses=list_of_guesses or []
    

    def ask_for_input():
        while True:
            guess = input('Please guess a letter: ')
            if len(guess) != 1 or guess.isdigit():
                print('Invalid letter. Please enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


    def check_guess(self, guess): 
        # Function for checking if the guessed letter input by the user is in the word 
        if guess.lower() in self.word.lower():
            print(f'Good guess! "{guess}" is in the word.')

            # Loop through each letter in the word
            for i in range(len(self.word)):
                letter = self.word[i]

                # Check if the letter is equal to the guess
                if letter.lower() == guess.lower():
                    # Replace the corresponding "_" in word_guessed with the guess
                    self.word_guessed[i] = guess

            # Reduce the variable num_letters by 1
            self.num_letters -= 1
        else:
            # Reduce num_lives by 1
            self.num_lives -= 1

            # Print a message for incorrect guess
            print(f'Sorry, "{guess}" is not in the word.')

            # Print the number of lives left
            print(f'You have {self.num_lives} lives left.')





