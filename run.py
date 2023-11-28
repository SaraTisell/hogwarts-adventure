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
dormitories = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]
print(*dormitories, sep="\n")

# Select Dormitory
def select_dormitory():
    print("We need to know your strenghts to make sure to put you in the right dormitory.\nPlease choose one of these four skills that best describes you greates strength! ")
    dormitories_strengths = ["Bravery", "Curiosity", "Loyalty", "Ambition"]
    user_dormitory_strenght = input()
   # dormitory = input()

# Challenge description

print((f"{name} you have been placed in {dormitory}, which will suit you perfectly based on your skill {user_dormitory_strenght}!\n"
"We have a very important mission for you, we need you to find the Philosopher's stone before it is to late!\n"
"Find the stone while you explore the magic within Hogwarts, but be careful, challenges will come in your way.\n"
f"Use your skill {user_dormitory_strenght} well, and we will meet again in the end."
f"The best of luck to you {name}"))



def third_floor():

def dark_forest():

def fluffy_dog():

def hagrids_hut():

def hospital_wing():

def peeves_poltergeist():

def prof_dumbledore():

def game_lost():

def game_win():






