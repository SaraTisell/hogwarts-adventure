# Global list to use in functions
dormitories = {"Bravery": "Gryffindor", "Curiosity": "Ravenclaw", "Loyalty": "Hufflepuff", "Ambition": "Slytherin"}



"""
Welcome text to user
"""
def welcome_to():
    print("Welcome to Hogwarts Adventure")
    print("If you are ready to play the game please enter your name")
    global name
    name = input().capitalize()
    print("Thank you, lets play and have fun!")
    print()

    """
    Start game
    Welcome letter
    """
    print(f"Dear, {name}\nYou have been accepted to Hogwarts School for Witchcraft and Wizardry!")
    print("It is time to place you in the right dormitory, our four dormitories are:")
    for dormitory in dormitories.values():
        print(dormitory)



# Select Dormitory
def select_dormitory():
    print("We need to know your strenghts to make sure to put you in the right dormitory.\nPlease choose one of these four skills that best describes you greates strength! ")
    for dormitory_strength in dormitories.keys():
        print(dormitory_strength)
    user_dormitory_strength = input("Please write your selected strength:\n").capitalize()
    while user_dormitory_strength not in dormitories.keys():
        print("Strengths: Bravery, Curiosity, Loyalty, Ambition")
        user_dormitory_strength = input("Please write your selected strength:\n").capitalize()   
    
    user_dormitory = dormitories.get(user_dormitory_strength)
    
    # Challenge description
    print((f"{name} you have been placed in {user_dormitory} , which will suit you perfectly based on your skill {user_dormitory_strength}!\n"
        "We have a very important mission for you, we need you to find the Philosopher's stone before it is to late!\n"
        "Find the stone while you explore the magic within Hogwarts, but be careful, challenges will come in your way.\n"
        f"Use your skill {user_dormitory_strength} well, and we will meet again in the end.\n"
        f"The best of luck to you {name}"))


"""
Function structure borrowed from https://www.makeuseof.com/python-text-adventure-game-create/
"""
def start_exploring():
    option = ["1", "2"]
    print(("It is time to begin your jorney to find the Philosopher's stone, you can either go to the Third Floor or the Dark Forest\n"
        "Select 1 for Third Floor\n"
        "Selecet 2 for Dark Forest "))
    user_input = input()
    while user_input not in option:
        print("Please select 1 or 2")
        user_input = input()
    if user_input == "1":
        third_floor()
    else:
        if user_input == "2":
            dark_forest()
    
        

def third_floor():
    option = ["1", "2"]
    print(("The Third Floor is a higly forbidden area as very dangerous creatures roam here.. And yet here you are..\n"
        "You are not allowed to stay here and Mr Filch is on his way to catch you and drag you to the principal's office\n"
        "Take action now! You can either Hide or Run\n"
        "Select 1 to Run\n"
        "Select 2 to Hide"))
    user_input = input()
    while user_input not in option:
        print("Please select 1 or 2")
        user_input = input()
    if user_input == "1":
        dark_forest()
    else:
        if user_input == "2":
            fluffy_dog()
    




def dark_forest():
    option = ["1", "2"]
    print(("There are many magical creatures living in this forest, some of them are good and some are you worst nightmare!\n"
        f"The Dark Forest is no safe place for students, especially not you {name}..\n"
        "The Dark Lord knows what you are up to, he knows what you are trying to find\n"
        "He wants to stop you and have sent Dementors in your way\n"
        "Time to protect yourself, FAST cast a spell\n"
        "Select 1 for Expecto Patronum\n"
        "Select 2 for Expelliarmus"))
    user_input = input()
    while user_input not in option:
        print("Please select 1 or 2")
        user_input = input()
    if user_input == "1":
        hagrids_hut()
    else:
        if user_input == "2":
            hospital_wing()
    
    

def fluffy_dog():
    option = ["1", "2"]
    print(("You were able to escape Mr Filch, but we told you dangerous creatures roam here at the third floor\n"
        "And you hide inside the same room as Fluffy, Hagrid's three-headed dog!\n"
        "Fluffy does not like other people than his loving Hagrid, but can easily be calmed down.\n"
        "He is on hiw way to attack you! You have to distract him\n"
        "Select 1 to Play Music\n"
        "Select 2 to Jump"))
    user_input = input()
    while user_input not in option:
        print("Please selecet 1 or 2")
        user_input = input()
    if user_input == "1":
        peeves_poltergeist()
    else:
        if user_input == "2":
            print("Jumping was not the way to calm that three-headed dog down\nYou are hurt and will meet madam Pomfrey at the hospital wing.")
            hospital_wing()



"""
def hagrids_hut():

def hospital_wing():

def peeves_poltergeist():

def prof_dumbledore():

def game_lost():

def game_win():



"""
"""
Function to start the game
"""
def main():
    welcome_to()
    select_dormitory()
    start_exploring()
    third_floor()
    dark_forest()

main ()

