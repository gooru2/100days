#TODO: Clear console DONE biblioteka os
#TODO: repair stages DONE uzycie zlego nawiasu

import random
from hangman_art import logo, stages
from hangman_words import word_list
import os

# adding game condition
chosen_word = random.choice(word_list)
lives = 6

print(logo)

#crating blank password
display= []
for letter in chosen_word:
    display.append('_')

# while there are any blanks in password
while '_' in display:
    #logic for guessing and assign to password
    guess = input("Guess a letter: ").lower()
    os.system('clear')
    if guess in display:
        print(f"You already guess this letter: {guess}")

#adding letter to corect place and print on the screeen
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = guess

#guees go bad
    if not guess in chosen_word:
        print("This letter is not in the password")
        lives -= 1
        print(stages[lives])
        print(f"You have {lives} livesc")
    if lives == 0:
        print(f"You LOOSER. Correct password is: {chosen_word} ")
        break

#print gueesed letters
    print(f"{' '.join(display)}")

if lives!=0:
    print ("WINNER")