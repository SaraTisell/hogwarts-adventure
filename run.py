# Global list to use in functions
dormitories = {"Gryffindor": "Bravery", "Ravenclaw": "Curiosity", "Hufflepuff": "Loyalty", "Slytherin": "Ambition"}

# Description for game
print("Welcome to Hogwarts Adventure")
print("If you are ready to play the game please enter your name")
name = input()
print("Thank you, lets play and have fun!")
print()

"""
Start game
Welcome letter
"""
print(f"Dear, {name}\nYou have been accepted to Hogwarts School for Witchcraft and Wizardry!")
print("It is time to place you in the right dormitory, our four dormitories are:")
for dormitory in dormitories.keys():
    print(dormitory)



# Select Dormitory
def select_dormitory():
    print("We need to know your strenghts to make sure to put you in the right dormitory.\nPlease choose one of these four skills that best describes you greates strength! ")
    for dormitory_strength in dormitories.values():
        print(dormitory_strength)
    print(Please write your selected strength)
    userDormitory = ""
    while userDormitory not in dormitories.values:
        print("Strengths: Bravery, Curiosity, Loyalty, Ambition")
        userDormitory = input()
        

# Challenge description
"""
print((f"{name} you have been placed in {dormitory}, which will suit you perfectly based on your skill {}!\n"
"We have a very important mission for you, we need you to find the Philosopher's stone before it is to late!\n"
"Find the stone while you explore the magic within Hogwarts, but be careful, challenges will come in your way.\n"
f"Use your skill {} well, and we will meet again in the end."
f"The best of luck to you {name}"))
"""
"""
Function structure borrowed from https://www.makeuseof.com/python-text-adventure-game-create/
"""
"""
def start_exploring():
    option = ["1", "2"]
    print(("It is time to begin your jorney to find the Philosopher's stone, you can either go to the Third Floor or the Dark Forest\n"
    "Select 1 for Third Floor\n"
    "Selecet 2 for Dark Forest "))
    userInput = ""
    while userInput not in option:
        print("Please selecet 1 or 2")
        userInput = input()
        if userInput == "1":
            third_floor()
        elif userInput == "2":
            dark_forest()
        else:
            print("Please select 1 for Third Floor or 2 for Dark Forest")

start_exploring()


def third_floor():
    option = ["1", "2"]
    print(("The Third Floor is a higly forbidden area as very dangerous creatures roam here.. And yet here you are..\n"
    "You are not allowed to stay here and Mr Filch is on his way to catch you and drag you to the principal's office\n"
    "Take action now! You can either Hide or Run\n"
    "Select 1 to Run\n"
    "Select 2 to Hide"))
    userInput = ""
    while userInput not in option:
        print("Please selecet 1 or 2")
        userInput = input()
        if userInput == "1":
            dark_forest()
        elif userInput == "2":
            fluffy_dog()
        else:
            print("Please select 1 to Run or 2 to Hide")

def dark_forest():

def fluffy_dog():

def hagrids_hut():

def hospital_wing():

def peeves_poltergeist():

def prof_dumbledore():

def game_lost():

def game_win():




"""

