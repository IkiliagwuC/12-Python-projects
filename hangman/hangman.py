import random
import string

from words import words

#function chooses a random word for user to guess from word module
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word: 
        word = random.choice(words)

    return word.upper()


def hangmann():
    word = get_valid_word(words)
    word_letters = set(word) #actual letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #keep track of what the user has guessed

    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #show the uset the letters used
        print("you have" ,lives, "lives left and you have used these letters", ' '.join(used_letters))

        #tell the user what the current word is with dashes with list comprehension
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', '-'.join(word_list))
        user_letter = input("guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else: 
                lives = lives - 1 #takes away one life if wrong
                print("letter not in word")

        elif user_letter in used_letters:
            print("you have already used that letter, please try again")
        
        else: 
            print('Invalid Character, please try again!')
    if lives == 0:
        print('You died sorry')
    print("You have guessed the word", word, '!!')


hangmann()