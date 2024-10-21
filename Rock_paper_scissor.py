"""
WORKFLOW OF PROJECT 
1- Input from user(Rock,paper,scissor)
2- Computer choice (computer will choose randomly not conditonally)
3- Result print

Cases:
A - Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B - Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C - Scissor
Scissor - Scissor = tie
Scissor - Paper = Scissor win
Scissor - Rock = Rock win

"""

import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock , Paper , Scissor = ")
comp_choice = random.choice(item_list)

# print(f"User choice = {user_choice} , Computer choice = {comp_choice}")
print("User choice = ",user_choice)
print("computer choice = ",comp_choice)
if( user_choice == comp_choice):
    print("Both chooses same: = Match Tie..!")

elif (user_choice == "Rock"):
    if (comp_choice == "Paper"):
        print("Paper covers Rock = Computer win... ")
    else:
        print("Rock smashes Scissor = You win...")

elif (user_choice == "Paper"):
    if (comp_choice =="Scissor"):
        print("Scissor cuts paper = Computer win...")
    else:
        print("Paper covers rock = You win...")

elif (user_choice =="Scissor"):
    if (comp_choice =="Paper"):
        print("Scissor cuts paper = You win...")
    else:
        print("Rock smashes scissor = Computer win...")
