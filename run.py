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

def select_dormitory():
    print("We need to know your strenghts to make sure to put you in the right dormitory.\nPlease choose one of these four skills that best describes you greates strength! ")
    dormitories_strengths = ["Bravery", "Curiosity", "Loyalty", "Ambition"]



# Dormitories options
