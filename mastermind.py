# Mastermind är ett spel där datorn slumpar fram 4 siffror mellan 1 och 6
# Spelaren gissar, på 12 gissningar, på vad dessa siffror kan vara
# datorn ger "R" om gissningen är rätt siffra och rätt plats
#   "X" om gissningen är rätt siffra i fel plats
#   och " " om siffran inte är med
# Det finns 2 svårighetsgrader, lättare (alla siffror är anurlunda) 
#   och svårare (det kan vara vilka siffror som hälst)

import random

guess1, guess2, guess3, guess4, guess5, guess6, guess7, guess8, guess9, guess10, guess11, guess12 = "", "", "", "", "", "", "", "", "", "", "", ""
guesses_list: list = [guess1, guess2, guess3, guess4, guess5, guess6, guess7, guess8, guess9, guess10, guess11, guess12]

feedback1, feedback2, feedback3, feedback4, feedback5, feedback6, feedback7, feedback8, feedback9, feedback10, feedback11, feedback12 = "", "", "", "", "", "", "", "", "", "", "", ""
feedback_list: list = [feedback1, feedback2, feedback3, feedback4, feedback5, feedback6, feedback7, feedback8, feedback9, feedback10, feedback11, feedback12]

seperation: int = 18
guess_count: int = 0

game_on: bool = True

table: str = f"""
gissning# {"gissning":^10} feedback
12 {guess12:^{seperation}} {feedback12}
11 {guess11:^{seperation}} {feedback11}
10 {guess10:^{seperation}} {feedback10}
 9 {guess9:^{seperation}} {feedback9}
 8 {guess8:^{seperation}} {feedback8}
 7 {guess7:^{seperation}} {feedback7}
 6 {guess6:^{seperation}} {feedback6}
 5 {guess5:^{seperation}} {feedback5}
 4 {guess4:^{seperation}} {feedback4}
 3 {guess3:^{seperation}} {feedback3}
 2 {guess2:^{seperation}} {feedback2}
 1 {guess1:^{seperation}} {feedback1}
"""

last_table: str = table

numbers: list = []

def update_table(list_of_guesses: list, list_of_feedback: list, seperation: int):
     table: str = f"""
gissning# {"gissning":^10} feedback
12 {str(list_of_guesses[11]):^{seperation}} {list_of_feedback[11]}
11 {str(list_of_guesses[10]):^{seperation}} {list_of_feedback[10]}
10 {str(list_of_guesses[9]):^{seperation}} {list_of_feedback[9]}
 9 {str(list_of_guesses[8]):^{seperation}} {list_of_feedback[8]}
 8 {str(list_of_guesses[7]):^{seperation}} {list_of_feedback[7]}
 7 {str(list_of_guesses[6]):^{seperation}} {list_of_feedback[6]}
 6 {str(list_of_guesses[5]):^{seperation}} {list_of_feedback[5]}
 5 {str(list_of_guesses[4]):^{seperation}} {list_of_feedback[4]}
 4 {str(list_of_guesses[3]):^{seperation}} {list_of_feedback[3]}
 3 {str(list_of_guesses[2]):^{seperation}} {list_of_feedback[2]}
 2 {str(list_of_guesses[1]):^{seperation}} {list_of_feedback[1]}
 1 {str(list_of_guesses[0]):^{seperation}} {list_of_feedback[0]}
"""
     return table


while True: #kollar vilken svårighet användaren vill ha
    diff_answer = input("välj svårighet, lättare (1) eller svårare (2) > ")
    if diff_answer in ["1","2"]:
        if diff_answer == "1":
            easy = True
        else:
            easy = False
        break
    else:
        print("Jag fattade inte det där.")

def number_gen(): # skapar en lista av 4 hemliga siffror mellan 1 och 6
    while True:
        added_number: int = random.randint(1,6)
        if not (easy and (added_number in numbers)):
            numbers.append(added_number)
        if len(numbers) == 4:
            return numbers

def feedbacker(guess, correct_guess): # matchar gissning med svar och ger feedback
    feedback = [" ", " ", " ", " "]
    guess_after = []
    correct_after = []

    for index in range(4): #är det helt korrect? (R)
        if guess[index] == correct_guess[index]:
            feedback[index] = "R"
        else: #sparar det som inte är helt korrect
            guess_after.append(guess[index])
            correct_after.append(correct_guess[index])
    
    for index in range(4): #om inte helt rätt, kollar om delvis rätt
        if feedback[index] == " ":
            if guess[index] in correct_after:
                feedback[index] = "X"
                correct_after.remove[{guess[index]}]
    
    return feedback

secret_numbers: list = number_gen()

while game_on:
    if table != last_table: 
        print(table)

    last_table = table

    guess = input(f"vad tror du siffrorna är? (separera siffror med ' ') > ")
    guess = guess.split()

    if not(len(guess) == 4 and all(item in ["1","2","3","4","5","6"] for item in guess)):
        print("det behöver vara 4 siffror (1-6) separerade med ' ' (mellanrum) ")

    else:
        for item in guess:
            guess[guess.index(item)] = int(item)
        guesses_list[guess_count] = [str(item) for item in guess]
        feedback = [" ", " ", " ", " "]

        feedback = feedbacker(guess, secret_numbers)

        feedback_list[guess_count] = feedback
        guesses_list[guess_count] = guess
        if feedback == ["R", "R", "R", "R"]:
            game_on = False
            print(f"\nBra gjort! Det är korrekt, {guess} är mina hämliga siffor!\n")
        guess_count += 1
        table = update_table(guesses_list, feedback_list, 18)