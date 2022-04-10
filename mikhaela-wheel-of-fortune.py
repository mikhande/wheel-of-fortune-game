#Wheel of Fortune

import random

# from sqlalchemy import false

def random_word(fname):
    word_dictionary = open("words.txt")
    the_word = random.choice(word_dictionary.read().split())
    word_dictionary.close()
    return the_word

the_word = random_word('words.txt')

the_word_list = list(the_word)

correct_letters = []

for char in the_word: # for the character in the word, it will change the blank spaces to include the new guessed letter
        correct_letters.append("_")

player_guess = False

players = [1,2,3]

player_turns = 0

player_bank = 0

guesses_made = []

vowels = ['a', 'e', 'i', 'o', 'u']

the_wheel =  [200, 400, 250, 150, 400, 600, 250, 350, 750, 800, 300, 200, 100, 500, 400, 300, 200, 700, 200, 150, 450, "BANKRUPTCY", "Lose a Turn"]

wheel_choice = random.choice(the_wheel)

def spin_wheel():
    global wheel_choice
    wheel_choice = random.choice(the_wheel)
    print(wheel_choice)
    return wheel_choice

# This will have to go in the loop after spin_wheel is called because you can't have a "break" outside of the loop
#  if wheel_choice.isalpha and wheel_choice == "BANKRUPTCY":
#         player_bank = 0
#     elif wheel_choice.isalpha and wheel_choice == "Lose a TUrn":
#         break
def guess_consonant():
    global consonant_guess
    consonant_guess = input("Guess a consonant: ")
    for position in range(len(the_word_list)):
        if the_word_list[position] == consonant_guess:
            correct_letters[position] = consonant_guess
    if consonant_guess.isalpha():
        if consonant_guess != vowels: #and consonant_guess == consonant_guess.isalpha():
            if consonant_guess in the_word and '_' in correct_letters: #This is if you have guessed a letter in the word but haven't guessed the full word
                guesses_made.append(consonant_guess)
                consonant_guess == True
                player_bank = player_bank + (wheel_choice * vowel_guess.count(correct_letters))
                print(correct_letters)
                print('That letter is in the word! That means you have won: $' + str(player_bank))
            elif '_' not in correct_letters: #This is if you have guessed the full word by guessing letters 
                player_bank = player_bank + (wheel_choice * vowel_guess.count(correct_letters))
                print("Congratulations, the word was " + str(the_word) + ". You got it! Your bank is now: $" + (player_bank))
                consonant_guess == True 
            elif consonant_guess != correct_letters:
                print("Sorry, that's not part of the word. It's the next contestant's turn.")
                consonant_guess == False
            else:
                print("That's not a consonant. Please try again.")
        #neede to finish this!!

def guess_vowel():
    global vowel_guess
    vowel_guess = input("$250 has been deducted from your bank. Please guess a vowel: ")
    player_bank == player_bank - 250
    for position in range(len(the_word_list)):
        if the_word_list[position] == vowel_guess:
            correct_letters[position] = vowel_guess
    if vowel_guess in the_word and '_' in correct_letters:
        print("That letter is in the word!")
        guesses_made.append(vowel_guess)
        vowel_guess == True
        print(correct_letters)
    elif '_' not in correct_letters:
        print("Congratulations, the word was " + str(the_word) + ". You got it!")
        vowel_guess == True
    elif vowel_guess != correct_letters:
        print("Sorry, that's not part of the word.")
        vowel_guess == False
    elif vowel_guess not in vowels:
        print("That's not a vowel. Try again.")


def word_guess():
    print("You can now guess make a guess!")
    if player_bank >= 250:
        guess_response = input("You can now guess a consonant or buy a vowel. for a Consonant, type ''C'' for Vowel, type ''V.'' If you buy a vowel, $250 will be subtracted from your bank:  ")
        if guess_response == "C":
            guess_consonant()
            if consonant_guess == True:
                player_bank = player_bank + wheel_choice * vowel_guess.count(correct_letters)
        if guess_response == "V":
            guess_vowel()
            if vowel_guess == True:
                player_bank = player_bank + wheel_choice
    elif player_bank < 250:
        guess_consonant()


def play_again():
    response = input("Do you want to play again? y = yes, n = no: ")
    if response == 'y':
        normal_round()
    else: 
        print('Thanks for playing!')

def begin_round1():
    # player_turns == 0
    if player_turns == 0: #or player_turns ==4:
        # players == 1
        print("It is WHEEL OF FORTUNE! Welcome, Player 1, here is the word: " + str(correct_letters))
    if player_turns == 1 or player_turns == 5:
        print("player 2")
        # players = 2
        # normal_round()
    if player_turns == 2 or player_turns == 6:
        print("player 3")
        # players = 3
        # normal_round()

# def begin_round2():
#     if player_turns == 0:
#         global random_player
#         random_player = random.choice(players)
#         print("Round 2! Player " str(random_player) " you start.")


def normal_round():

    while player_guess == False:
        print("It is WHEEL OF FORTUNE! Welcome, Player 1, here is the word: " + str(correct_letters))
        # begin_round1()
        # if player_turns == 0:
        #     players == 1
        #     print("It is WHEEL OF FORTUNE! Welcome, Player 1, here is the word: " + str(correct_letters))
        # elif player_turns == 1: #and player_turns == 5
        #     players == 2
        #     print("It's your turn player 2.")
        # elif player_turns == 2: #and player_turns == 6:
        #     players == 3
        #     print("Alright, player 3.")
        player_choice = input("Would you like to spin the wheel or make a guess? If spin the wheel, type in 'W' if guess, type in 'G': ")
        if player_choice == "W":
            spin_wheel()
            if wheel_choice == "BANKRUPTCY":
                print("Oh no! You landed on BANKRUPTCY and lost all your money...")
                player_bank == 0
                print("Your player bank is now: " + str(player_bank))
                player_turns += 1
                    # normal_round()
            elif wheel_choice == "Lose a Turn":
                print("Oops, you lost a turn.")
                player_turns += 1
                        # normal_round()
            else:
                    print("Nice! You now have the opportunity to make a guess.")
                    guess_consonant()
        elif player_choice == "G":
            guess_type = input("Would you like to guess the word or solve the puzzle? Type ''W'' for word and ''P'' for puzzle.")
            if guess_type == "W":
                word_guess()
                player_turns += 1
            elif guess_type == "P":
                puzzle_guess = input("Good luck! Please type in the word: ")
                if puzzle_guess == puzzle_guess.isalpha():
                    if puzzle_guess == the_word:
                        print("Congratulations, you got it! The word was" + str(the_word))
                        player_guess == True
                        normal_round()
                    elif puzzle_guess != the_word:
                        print("Sorry, that's not it!")
                        player_turns = player_turns + 1 # adding player turns
                else: 
                    print("That's not a word... Try again.")
                    
                        


                # guess = input("Great! Are you guessing a consonant or the word? Type ''C'' for consonant and ''W'' for the word: ")
                # for position in range(len(the_word_list)):
                #     if the_word_list[position] == guess:
                #         correct_letters[position] = guess
                # if guess == "C" and len(guess) == 1: # this is if they're guessing a letter
                #     print("not done")
                    
normal_round()
