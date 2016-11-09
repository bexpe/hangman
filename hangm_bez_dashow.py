import sys
import random
import time
import os


INSTRUCTION_TEXT = ""
STORY = """
    Evil SKYNET is trying to take control over the world.
    You are the only hope to save it by showing your inteligence and skills.
    Prove it by guessing all of CAPITALS OF EUROPE.
    You can guessing by one letter or show that you are the smartest and guess
    all capital at once! Let's do this!
    """ #a story telling how to play

def string_to_list(word_to_guess):
    """function changing one string to a list of letters"""
    word_to_guess_letter_list = [] #list of letters from the word to guess
    for c in word_to_guess:
        word_to_guess_letter_list.append(c)
    return word_to_guess_letter_list


def letter_to_dashes(word_to_guess):
    """puting dashes in the place of each letter (variable answer_from_letters)
        preparing to guessing letters."""
    answer_from_letters = [] #variable from dashes being changed for letters
    for c in word_to_guess:
        if c == " ":
            answer_from_letters.append("   ") #if a word has a space then this
            #condition will put a space instead of dash.
        else:
            answer_from_letters.append(" _ ")# it changes a letter to a dash
    return answer_from_letters


def show_dashes(answer_from_letters):
    """shows dashes in a place of letters in the word to guess. Its the
        beginning of game"""
    print("")
    for dash in answer_from_letters:
        print(dash, " ", end="") #changing letters from word to guess into
        #dashes divided by spaces
    print()


def adding_letter(word_to_guess, answer_from_letters):
    global lives
    global num #this variable will be counting how many letters were inputed
    #before guessing the capital
    input_letter = input("Input letter: ")
    print()
    while True:
        if input_letter.isalpha(): #checking if user is printing letters only
            if input_letter == "exit":
                sys.exit("Looser!")
            else    :
                input_letter=input_letter.strip()
                if len(input_letter)>1:
                    input_letter = input("Input only one letter: ")
                else:
                    input_letter = input_letter.upper()#changing for capital letters
                    num += 1
                    break
        else:
            print("Only letters allowed")
            break

    how_many_letters_in_word = word_to_guess.count(input_letter)
    #print("You have " + str(how_many_letters_in_word) + " '" +
    #str(input_letter) + "' in this word")
    print()
    input_letter_all_positions=[] #creates new list with an answer which is
    #comparing with a word to guess by how_many_letters_in_word
    searching_start=0
    for i in range(how_many_letters_in_word):
            input_letter_position=word_to_guess.find(input_letter,searching_start)
            input_letter_all_positions.append(input_letter_position)
            searching_start=input_letter_position+1
    if how_many_letters_in_word == 0:
        lives = lives-1
        print("Lost one life!!! :( ")
        print()
    if lives:
        print("You have" + " \u2665 " * int(lives) + " lives")
        if lives == 1:
            print()
            print("!!! HINT: The capitol of", country, "....")
    else:
        print("You have no more lives")
    print()
    for i in input_letter_all_positions:
        answer_from_letters[i] = input_letter

    for answer in answer_from_letters:
        print(" " + answer + " ", end="")
    print()


def entering_full_answer(word_to_guess):
    global full_answer
    global lives
    full_answer = input("Give me full answer: ")
    full_answer = full_answer.strip()
    if all(c.isalpha() or c.isspace() for c in full_answer): #checking if the
    #full answer consists only from letters and has spaces
        if full_answer == "exit":
            sys.exit("Looser!")
        full_answer = full_answer.upper()
        print()
        if full_answer == word_to_guess:
            print("It's correct answer!")
        else:
            print("It wasn't correct answer :( ")
            lives = lives-2
            if lives > 1:
                print()
                print("Lost two lives!!! :( ")
            if lives == 1:
                print()
                print("!!!!! HINT: The capitol of", country, "....")
            print()
            if lives > 0:
                print("You have" + " \u2665 " * int(lives) + " lives")
            else:
                print("You have no more lives !!!")

    else:
        print("It wasn't correct answer")
        lives = lives-2
        print("Lost two lives!!! :( ")
        if lives > 0:
            print("You have" + " \u2665 " * int(lives) + " lives")
        else:
            print("You have no more lives")


def results():
    """ this function is printing results in a new list 'results' which is
        collecting only ten results. In 'results' checking are such parametres
        as name, date, time, how many letters was used, and the word guessed """

    print ("          ######### HALL OF FAME ##########")
    print()
    print("place".ljust(5), "|    name    |     date     | time (s) | letters |   word")
    print()
    records=[]
    f=open('results', 'r')
    records=[ line.split(" | ") for line in f ]
    f.close()

    f=open('results', 'w') #writing result to the list
    place=0
    for record in sorted(records, key=lambda i: float(i[2])):
        #for every record in the list with results sort results by time
        place += 1 #every time we add some new result the place is one time bigger
        record[2]="{:.2f}".format(float(record[2]))#formating time to two decimal places
        s = record[0] + " | " + record[1] + " | " + record[2] + " | " + record[3] + " | " + record[4]
        f.write(s) #its writing new result in a list
        print(str(str(place) + ".").rjust(5), record[0].rjust(10), record[1].rjust(15), record[2].rjust(10), record[3].rjust(10), "  ", record[4].ljust(80) )
        #its printing the result, limiting the amount of characters to 5, 10 or 15.
        if place == 10: #we can write only ten results on a list
            break
    f.close() #every time the list is being closed


def game_ending(full_answer, word_to_guess, word_to_guess_letter_list, answer_from_letters):
    global lives
    global num
    print()
    f=open('results', 'a')
    if word_to_guess_letter_list == answer_from_letters or full_answer == word_to_guess:
        print("You won!!!")
        stop = time.time()
        tresult = round(stop - start, 2)#time results has only two decimal places
        date = time.strftime("%d/%m/%Y") #Return a string representing the date

        print()
        print("You guessed in", tresult, "seconds,", "after trying", num, "letters")
        print()
        name=input("What's your name?: ")
        if name.isalpha:
            if len(name) <= 8: #name can be 8 letters long only
                s=name + " | " + str(date) + " | " + str(tresult) + " | " + str(num) + " | " + word_to_guess + "\n"
                f.write(s)
                f.close()
            else:
                print("Name cannot be longer than 8 chars")
        else:
            print("Your name is incorrect will not save results")
        print()
        results()
        start_again()

    elif lives == 0 or full_answer != word_to_guess:
        print("You lost!!!")
        start_again()


def start_again():
    print()
    answer = input("Do you want to start again? [ Y / n ]: ")#Yes is a default option
    if answer == "n":
        sys.exit("See you")
    else:
        os.system('clear')

while True:
        os.system('clear')
        print(STORY)
        start = time.time()

        f = open('capitols', 'r')
        LIST_OF_PAIRS=[]
        for line in f:
            LIST_OF_PAIRS.append(line)
        f.close()
        
        pair_to_guess = random.choice(LIST_OF_PAIRS)
        country, word_to_guess = pair_to_guess.strip().split(" | ")
        word_to_guess = word_to_guess.upper()

        lives = 5
        num = 0
        full_answer = "" # variable with full answer input from player

        word_to_guess_letter_list = string_to_list(word_to_guess)# calls the
        #function changing string to the list of letters
        answer_from_letters = letter_to_dashes(word_to_guess)
        # calls the function changing letters to dashes
        show_dashes(answer_from_letters) #showing dashes instead of the correct answer
        while word_to_guess_letter_list != answer_from_letters and full_answer != word_to_guess and lives > 0:
            print()
            next_step = input("Do you want to input letter [1], input all answer [2] or print exit to end the game: ") #we are choosing one from 3 options
            if next_step == "1":
                print()
                adding_letter(word_to_guess, answer_from_letters)
            elif next_step == "2":
                print()
                entering_full_answer(word_to_guess)
            elif next_step == "exit":
                print()
                sys.exit("Looser!")

        game_ending(full_answer, word_to_guess, word_to_guess_letter_list, answer_from_letters)
        #while answer is incorrect or we loose all lives, game ends
