# Mastermind är ett spel där datorn slumpar fram 4 siffror mellan 1 och 6
# Spelaren gissar, på 12 gissningar, på vad dessa siffror kan vara
# datorn ger "R" om gissningen är rätt siffra och rätt plats
#   "X" om gissningen är rätt siffra i fel plats
#   och " " om siffran inte är med
# Det finns 2 svårighetsgrader, lättare (alla siffror är anurlunda) 
#   och svårare (det kan vara vilka siffror som hälst)

import random



gissning12, gissning11, gissning10, gissning9, gissning8, gissning7 = "", "", "", "", "", ""
gissning6, gissning5, gissning4, gissning3, gissning2, gissning1 = "", "", "", "", "", ""

feedback12, feedback11, feedback10, feedback9, feedback8, feedback7 = "", "", "", "", "", ""
feedback6, feedback5, feedback4, feedback3, feedback2, feedback1 = "", "", "", "", "", ""

seperation: int = 18

table: str = f"""
gissning# {"gissning":^10} feedback
12 {gissning12:^{seperation}} {feedback12}
11 {gissning11:^{seperation}} {feedback11}
10 {gissning10:^{seperation}} {feedback10}
 9 {gissning9:^{seperation}} {feedback9}
 8 {gissning8:^{seperation}} {feedback8}
 7 {gissning7:^{seperation}} {feedback7}
 6 {gissning6:^{seperation}} {feedback6}
 5 {gissning5:^{seperation}} {feedback5}
 4 {gissning4:^{seperation}} {feedback4}
 3 {gissning3:^{seperation}} {feedback3}
 2 {gissning2:^{seperation}} {feedback2}
 1 {gissning1:^{seperation}} {feedback1}
"""

numbers: list = []

while True:
    diff_answer = input("välj svårighet, lättare (1) eller svårare (2) > ")
    if diff_answer in ["1","2"]:
        if diff_answer == "1":
            easy = False
        else:
            easy = True
        break
    else:
        print("Jag fattade inte det där.")

while True:
    added_number: int = random.randint(1,6)
    if not (easy == True and (added_number in numbers)):
        numbers.append(added_number)
    if len(numbers) == 4:
        break

while True:
    print(table)
    guess = input(f"vad tror du siffrorna är? (separera siffror med ' ') > ")
    guess = guess.split(" ")

