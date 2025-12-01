# Mastermind är ett spel där datorn slumpar fram 4 siffror mellan 1 och 6
# Spelaren gissar, på 12 gissningar, på vad dessa siffror kan vara
# datorn ger "R" om gissningen är rätt siffra och rätt plats
#   "X" om gissningen är rätt siffra i fel plats
#   och " " om siffran inte är med
# Det finns 2 svårighetsgrader, lättare (alla siffror är annorlunda)
#   och svårare (det kan vara vilka siffror som helst)

import random

# Förbereder 12 gissning och feedback som tomma strängar, ska användas för table 
guess1, guess2, guess3, guess4, guess5, guess6, guess7, guess8, guess9, \
guess10, guess11, guess12 = "", "", "", "", "", "", "", "", "", "", "", ""
guesses_list: list = [
    guess1, guess2, guess3, guess4, guess5, guess6,
    guess7, guess8, guess9, guess10, guess11, guess12
]

feedback1, feedback2, feedback3, feedback4, feedback5, feedback6, \
feedback7, feedback8, feedback9, feedback10, feedback11, feedback12 = \
    "", "", "", "", "", "", "", "", "", "", "", ""
feedback_list: list = [
    feedback1, feedback2, feedback3, feedback4, feedback5, feedback6,
    feedback7, feedback8, feedback9, feedback10, feedback11, feedback12
]

seperation: int = 18  # kolumnbredd för tabellformat
guess_count: int = 0  # räknare för antal gjorda gissningar

game_on: bool = True  # spelstatus

# Starttabell (alla värden är tomma tills spelaren gissar)
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

last_table: str = table  # används för att avgöra om tabellen ändrats

numbers: list = []  # placeholder för de hemliga siffrorna


def update_table(list_of_guesses: list, list_of_feedback: list, seperation: int):
    """
    Bygger och returnerar tabellsträngen baserat på listor med gissningar
    och feedback. Index 0 motsvarar gissning 1 (nederst i tabellen).
    """
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


# Väljer svårighetsgrad — körs vid spelstart
while True:  # kollar vilken svårighet användaren vill ha
    diff_answer = input("välj svårighet, lättare (1) eller svårare (2) > ")
    if diff_answer in ["1", "2"]:
        if diff_answer == "1":
            easy = True
        else:
            easy = False
        break
    else:
        print("Jag fattade inte det där.")  # ogiltigt svar — be användaren försöka igen


def number_gen():
    """
    Skapar en lista av 4 hemliga siffror mellan 1 och 6.
    Om 'easy' är True tillåts inga dubbletter.
    """
    while True:
        added_number: int = random.randint(1, 6)
        # lägg till talet om det inte bryter mot 'easy'-regeln
        if not (easy and (added_number in numbers)):
            numbers.append(added_number)
        if len(numbers) == 4:
            return numbers


def feedbacker(guess, correct_guess):
    """
    Matchar en gissning med det korrekta svaret och returnerar feedback-lista:
    - "R" för rätt siffra på rätt plats
    - "X" för rätt siffra på fel plats
    - " " (mellanslag) för siffra som inte finns i svaret
    """
    feedback = [" ", " ", " ", " "]
    guess_after = []
    correct_after = []

    # Markera exakta träffar ("R") och spara övriga positioner för senare kontroll
    for index in range(4):
        if guess[index] == correct_guess[index]:
            feedback[index] = "R"
        else:
            guess_after.append(guess[index])
            correct_after.append(correct_guess[index])

    # För positioner som inte redan är "R", kolla om siffran finns i correct_after
    for index in range(4):
        if feedback[index] == " ":
            if guess[index] in correct_after:
                feedback[index] = "X"
                correct_after.remove(guess[index])

    return feedback



# Generera hemliga siffror (nummerlista)
secret_numbers: list = number_gen()

# Huvudloop för spelet, tar emot gissningar och uppdaterar tabellen
while game_on:
    if table != last_table:
        print(table)

    last_table = table

    guess = input(f"vad tror du siffrorna är? (separera siffror med ' ') > ")
    guess = guess.split()

    # Validera inmatning: måste vara 4 siffror mellan 1 och 6
    if not (len(guess) == 4 and all(item in ["1", "2", "3", "4", "5", "6"] for item in guess)):
        print("det behöver vara 4 siffror (1-6) separerade med ' ' (mellanrum) ")

    else:
        # Konvertera strängarna till int (ersätter varje element med int-version)
        for item in guess:
            guess[guess.index(item)] = int(item)

        guesses_list[guess_count] = [str(item) for item in guess]  # för visning i tabellen
        feedback = [" ", " ", " ", " "]

        # Skapa feedback för gissningen mot de hemliga siffrorna
        feedback = feedbacker(guess, secret_numbers)

        feedback_list[guess_count] = feedback
        guesses_list[guess_count] = guess

        # Kontrollera om spelaren vann (alla fyra R)
        if feedback == ["R", "R", "R", "R"]:
            game_on = False
            print(f"\nBra gjort! Det är korrekt, {guess} är mina hämliga siffor!\n")

        guess_count += 1
        table = update_table(guesses_list, feedback_list, 18)
