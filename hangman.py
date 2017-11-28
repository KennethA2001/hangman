import random

def header():
    print ("Hangman; created by Coop Dogg and made better by Kenneth Alexander")

    
def splash_screen():
    print(" _   _   ___   _   _ _____ ___  ___  ___   _   _  ")
    print("| | | | / _ \ | \ | |  __ \|  \/  | / _ \ | \ | | ")
    print("| |_| |/ /_\ \|  \| | |  \/| .  . |/ /_\ \|  \| | ")
    print("|  _  ||  _  || . ` | | __ | |\/| ||  _  || . ` | ")
    print("| | | || | | || |\  | |_\ \| |  | || | | || |\  | ")
    print("\_| |_/\_| |_/\_| \_/\____/\_|  |_/\_| |_/\_| \_/ " )
    print("")
    print("")

def show_credits():
    print(" _   __                      _   _       __   __      _______  __      _______  _____  __   ______")
    print("| | / /                     | | | |     /  | /  |    / / __  \/  |    / / __  \|  _  |/  | |___  /")
    print("| |/ /  ___ _ __  _ __   ___| |_| |__   `| | `| |   / /`' / /'`| |   / /`' / /'| |/' |`| |    / / ")
    print("|    \ / _ \ '_ \| '_ \ / _ \ __| '_ \   | |  | |  / /   / /   | |  / /   / /  |  /| | | |   / /  ")
    print("| |\  \  __/ | | | | | |  __/ |_| | | | _| |__| |_/ /  ./ /____| |_/ /  ./ /___\ |_/ /_| |_./ /   ")
    print("\_| \_/\___|_| |_|_| |_|\___|\__|_| |_| \___/\___/_/   \_____/\___/_/   \_____/ \___/ \___/\_/    ")
    print("")
    print("")


def get_name():
    print("What is your name?")
    name = input()
    
    print("It is nice to meet you, " + name + ".")
    return name
    

def get_puzzle():
    words = ["christmas", "computer programming", "easy", "hangman", "computer", "python", "winner", "turtle", "mouse", "cat", "pizza", "corndog", "ice cream"]
    return (random.choice(words))
    
    

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
