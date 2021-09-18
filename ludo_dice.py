import random
def user_interest():
    random_number=random.randint(1,6)
    return random_number
print("WELCOME TO OUR LUDO DICE ROLL GAME")
print("WOULD YOU LIKE TO ROLL THE DICE:")
T=input()
while T=="YES" or T=="Yes" or T=="yes":
    user_roll=user_interest()
    print(user_roll)
    print("WOULD YOU LIKE TO PLAY AGAIN")
    T=input()
print("THANKS FOR YOUR TIME")