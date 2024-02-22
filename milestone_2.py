import random 

word_list = ['Banana', 'Strawberry', 'Grape', 'Mango', 'Satsuma']

#print(random.choice(word_list))

word = random.choices(word_list)

#print(word)

guess = input('Please enter a single letter')

#print(guess)

if (len(guess)) ==1:
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')