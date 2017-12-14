import random
import os

def header():
    print ("Hangman; created by Coop Dogg and made better by Kenneth Alexander")

    
def splash_screen():
    path = "art"

    file = 'art/splash_screen.txt'

    with open(file, 'r') as f:
        lines = f.read()
    print(lines)
    
def show_credits():
    path = "art"

    files = 'art/credits.txt'

    with open(files, 'r') as f:
        lines = f.read()
        
    print(lines)


def get_name():
    print("What is your name?")
    name = input()
    
    print("It is nice to meet you, " + name + ".")
    return name
    

def get_puzzle():

    path = "data"
    funz_file= ""
    file_names = os.listdir(path)

    for i, f in enumerate(file_names):
        this_file = f
        with open(path + "/" + this_file, 'r') as f:
            beginning_lines = f.read().splitlines()
        category_name = beginning_lines[0] 
        print(str(i + 1)+ " " + category_name)
        print()

    choice = input("pick one ")
    choice = int(choice)-1

    file = path + "/" + file_names[choice]


    with open(file, 'r') as f:
        lines = f.read().splitlines()

    print(lines)

    puzzle = random.choice( lines[1:] )

    return puzzle
    
    

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        elif letter == " ":
            solved += " "
        else:
            solved += "-"

    return solved

def get_guess(name):
    while True:
        letter = input("Guess a letter " + str(name) + "!")

        if len(letter) == 1 and letter.isalpha():
            return letter
        else:
            print("Please enter a letter")
        

def display_board(solved, strikes):
    print(solved)
    print("Sttrikes: " + str(strikes))
    
    

def show_result(strikes):
    if strikes < limit:
        print(" You have won")

    else:
        print("You lost")
    

    
def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")
    
def play(name, strikes, limit):
    puzzle = get_puzzle()
    guesses= ""
    right_guesses = ""
    wrong_guesses = ""
    solved = "-" * len(puzzle)

    strikes= 0
    limit = 6
    result = 0
    
 
    display_board(solved, strikes)
    
    while solved != puzzle:
        letter = get_guess(name)

        if letter not in puzzle:
            strikes += 1
            wrong_guesses += letter
            if strikes == limit:
                break
        else:
            right_guesses += letter
            
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved, strikes)

    show_result(strikes)
    

header()
splash_screen()
name = get_name()

playing = True

while playing:
    strikes = 0
    limit = 6
    
    play(name, strikes, limit)
    playing= play_again()

show_credits()
