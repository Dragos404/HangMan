import random,sys

def get_game_difficulty():
    print(hangman_pics[7])
    print('''
             Welcome to Hangman. To start the game, please choose a difficulty!
        1. For Easy Game - Where the word has less than/equal to 6 letters and 7 lives - press 1!
        2. For Hard Game - Where the word has more than 6 letters and 3 lives - press 2!
        ''')
    difficulty = ""
    while difficulty == "":
        difficulty = input('Please insert a number from above: ')
        if difficulty not in ["1", "2"]:
            difficulty = ""
            print("Invalid input.")
    return int(difficulty)
           
def get_word_to_be_guessed(difficulty):
    with open("countries-and-capitals.txt", "r") as f:
        words = f.readlines()
    while True:
        word = random.choice(words)[:-1]
        word = word.split("|")[0]
        word = word.replace(" ", "")
        #print(word)
        if difficulty == 1 and len(word) <= 6:
            return word
        elif difficulty == 2 and len(word) > 6:
            return word

def set_number_of_lives(difficulty):
    if difficulty == 1:
        return 7
    elif difficulty == 2:
        return 3

def get_letter():
    while True:
        letter = input("Please enter a letter: ").lower()
        if letter.isalpha():
            break
        print("Please enter characters A-Z only.")
    return letter

def print_unguessed_word(word,guessed_letters):
    hidden_word = ""
    for character in word:
        if character.lower() in guessed_letters:
            hidden_word = hidden_word + character + " "
        else:
            hidden_word = hidden_word + "_ "
    print(hidden_word) 

def is_letter_already_tried(letter,guessed_letters):
    if letter in guessed_letters:
        print("You have already tried this letter.")
        return True
    else:
        return False

def check_if_the_input_is_quit(letter):
    if letter.lower() == "QUIT".lower():
        return sys.exit ("Thank you for the game!")


def is_the_letter_in_word(letter,word):
    if letter.lower() in word.lower():
        return True
    else:
        return False


hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''   
                    __  ___                                    
                    | | | |                                         
                    | |_| | __ _ _ __   __ _ _ __ ___   __ _ _ _  
                    | '_  |/ _`| '_ \ / _` | '_ ` _ \ / _` | '_ \ 
                    | | | |(_| | | | | (_| | | | | | | (_| | | | |
                    |_| |_|\_,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                        _/ |                      
                                        __ /                  
''']

def print_hangman(lives):
    if lives == 6:
        print(hangman_pics[0])
    elif lives == 5:
        print(hangman_pics[1])
    elif lives == 4:
        print(hangman_pics[2])
    elif lives == 3:
        print(hangman_pics[3])
    elif lives == 2:
        print(hangman_pics[4])
    elif lives == 1:
        print(hangman_pics[5])
    elif lives == 0:
        print(hangman_pics[6])
    


def print_wrong_letters(wrong_letters):
    print(wrong_letters)

def is_game_won(word, guessed_letters):
    for letter in word:
        if letter.lower() not in guessed_letters:
            return False
    return True


def is_game_lost(lives):
    if lives == 0:
        return True
    else:
        return False

def play_game(word,lives):
    guessed_letters = set()
    wrong_letters = set()
    while True:
        print_unguessed_word(word, guessed_letters)
        letter = get_letter()
        check_if_the_input_is_quit(letter)
        if is_letter_already_tried(letter, guessed_letters):
            print("You have already tried this letter.")
        elif is_the_letter_in_word(letter,word):
            guessed_letters.add(letter)
            print_unguessed_word(word,guessed_letters)
            print(guessed_letters)
        else:
            lives = lives - 1  #lives -= 1 - e mai corect asa
            wrong_letters.add(letter)
            print_hangman(lives)
            print_wrong_letters(wrong_letters)
        if is_game_lost(lives):
            print("Sorry, game over. The word was: " + word + ".")
            break
        if is_game_won(word,guessed_letters):
            print("You have won the game! The word was: " + word + ".")
            break

def main():
    difficulty = get_game_difficulty()
    word = get_word_to_be_guessed(difficulty)
    lives = set_number_of_lives(difficulty)
    play_game(word,lives)

if __name__ == "__main__":
    main()