import random
def computer_interest():
    A=["snake","water","gun"]
    computer_decision=random.choice(A)
    return computer_decision
print("WELCOME TO OUR SNAKE WATER GUN GAME")
print("WOULD YOU LIKE TO CHALLENGE ME?")
T=input()
while T=="YES" or T=="Yes" or T=="yes":
    computer_roll=computer_interest()
    print("LET'S GO,MAKE YOUR ACTION!!!")
    Y=input()
    if Y=="snake"and computer_roll=="water":
        print("YOU WON,CONGRATULATIONS!!!")
    if Y=="snake"and computer_roll=="gun":
        print("COMPUTER WON")
    if  Y == "water" and computer_roll == "gun":
        print("YOU WON,CONGRATULATIONS!!!")
    if    Y == "water" and computer_roll == "snake":
        print("COMPUTER WON")
    if Y == "gun" and computer_roll == "snake":
        print("YOU WON,CONGRATULATIONS!!!")
    if Y == "gun" and computer_roll == "water":
        print("COMPUTER WON")
    if Y==computer_roll:
        print("Ohh,IT'S A DRAW")
    print("WOULD YOU LIKE TO PLAY AGAIN?")
    T=input()
print("THANKS FOR YOUR TIME")