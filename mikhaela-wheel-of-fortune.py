#Wheel of Fortune

import random

def random_word(fname):
    word_dictionary = open("words.txt")
    the_word = random.choice(word_dictionary.read().split())
    word_dictionary.close()
    return the_word

the_word = random_word('words.txt')

the_word = list(the_word)

correct_letters = []

for char in the_word: # for the character in the word, it will change the blank spaces to include the new guessed letter
        correct_letters.append("_")

player_guess = False

players = [1,2,3]

player_bank = 0

guesses_made = []

vowels = ['a', 'e', 'i', 'o', 'u']

the_wheel =  [200, 400, 250, 150, 400, 600, 250, 350, 750, 800, 300, 200, 100, 500, 400, 300, 200, 700, 200, 150, 450, "BANKRUPTCY", "Lose a Turn"]

def spin_wheel():
    wheel_choice = random.choice(the_wheel)
    print(wheel_choice)
    return wheel_choice

# This will have to go in the loop after spin_wheel is called because you can't have a "break" outside of the loop
#  if wheel_choice.isalpha and wheel_choice == "BANKRUPTCY":
#         player_bank = 0
#     elif wheel_choice.isalpha and wheel_choice == "Lose a TUrn":
#         break

def play_again():
    response = input("Do you want to play again? y = yes, n = no: ")
    if response == 'y':
        normal_round()
    else: 
        print('Thanks for playing!')


