import os
import time
from colorama import Fore, Back, Style

# Global list to use in functions
dormitories = {"Bravery": Fore.RED + "Gryffindor" + Style.RESET_ALL,
               "Curiosity": Fore.BLUE + "Ravenclaw" + Style.RESET_ALL,
               "Loyalty": Fore.YELLOW + "Hufflepuff" + Style.RESET_ALL,
               "Ambition": Fore.GREEN + "Slytherin" + Style.RESET_ALL
               }




def welcome_to():

    """
    Welcome text to user
    Asking for name input to start of the game
    """
    #Hogwarts logo borrowed from https://emojicombos.com/harry-potter-ascii-art
    
    print("""⠀⠀⠀⠀⠀⢠⣾⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠟⢂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣦⣄⣀⡀⠀⠀⣀⣀⣠⠞⣉⡀⠀⠀⠂⢀⠀⠀⠀⠀
⠀⣠⣶⣿⣿⣿⣇⢶⢹⡿⠋⠻⣿⣿⣦⠞⠛⣽⣷⡿⠟⢿⣦⢀⣴⡿⠿⣶⠀⠀
⠀⢿⡄⠀⠙⣿⣿⣾⣸⠃⠀⠀⣨⣿⣿⠀⠸⠗⠉⢀⣠⣼⡿⣾⠃⠀⣠⡿⠀⠀
⠀⠈⠛⢶⣄⢸⣿⢧⣿⠃⠀⠀⣉⣿⣿⠀⠀⣠⣾⠿⠛⠁⢸⣿⠀⡾⠋⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⡜⠁⠀⣰⣤⣍⣙⣿⣀⣸⣿⣷⣄⣴⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⡿⠋⠀⠀⣹⣷⡀⢰⣿⣷⡄⢰⣿⣿⣷⢟⣿⢿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⣿⣘⣿⣎⣛⣿⠇⢈⡁⢙⡃⢘⣽⣤⣽⣿⣿⣼⣷⡀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⠋⢉⡩⠭⡉⢉⣿⡇⢸⣿⣿⡇⢸⣟⣉⠝⠻⣿⣿⠙⢷⡀⠀⠀⠀
⠀⠀⣰⣿⡃⢀⣾⣿⡥⠜⢸⣿⠃⣸⣿⣟⣁⡘⣿⣿⠃⠀⠘⠁⠀⠈⢿⣦⡀⠀
⢀⣾⠟⠘⠻⢿⣿⣿⣿⣷⣬⡛⠉⠉⢸⣿⣿⠉⠛⠉⠀⠀⠀⣆⠀⠀⢸⣿⣿⣦
⠙⢷⣄⣀⣀⣼⡿⢿⣿⣿⣿⣿⣦⡀⢸⣿⣿⠀⠀⢀⠀⠀⢀⣿⣀⡀⣘⣿⡟⠁
⠀⠀⠙⢿⡁⣀⡀⠀⠙⢿⣿⣿⣿⡇⠈⣿⣿⡆⢀⣼⡄⣀⣼⢿⣿⣿⣿⠋⠀⠀
⠀⠀⠀⠀⠿⠟⠻⣦⣀⣀⣿⢿⣏⢷⠀⣿⣿⣷⣾⡿⢱⣏⣼⠟⠉⠻⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢴⣾⣋⠀⠀⣿⣿⣿⣻⣴⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢷⣤⣿⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
    print("Welcome to Hogwarts Adventure")
    print("If you are ready to play the game please enter your name")
    global name
    name = input().capitalize()
    print("Thank you, lets play and have fun!")
    clear_screen()


    """
    Start game
    Welcome letter containing dormitories
    """
    
    print(f"Dear, {name}\nYou have been accepted"
            "to Hogwarts School for Witchcraft and Wizardry!")
    time.sleep(1)
    print("It is time to place you in the right dormitory, our four dormitories are:")
    for dormitory in dormitories.values():
        print("<---", dormitory, "--->")
    time.sleep(2)




def select_dormitory():

    """
    Function to assagin the user in to the right dormitory based on user input from key values in dormitory list
    """
    print()
    print("We need to know your strenghts to make sure to put you in the right dormitory.\n"
            "Please choose one of these four skills that best describes you greates strength!")
    for dormitory_strength in dormitories.keys():
        print(dormitory_strength)
    global user_dormitory_strength
    user_dormitory_strength = input("Please write your selected strength:\n").capitalize()
    while user_dormitory_strength not in dormitories.keys():
        print("Strengths: Bravery, Curiosity, Loyalty, Ambition")
        user_dormitory_strength = input("Please write your selected strength:\n").capitalize()   

    user_dormitory = dormitories.get(user_dormitory_strength)

    clear_screen()
    # Challenge description
    print((f"{name} you have been placed in {user_dormitory},\n"
            f"which will suit you perfectly based on your skill {user_dormitory_strength}!\n"
            "We have a very important mission for you, we need you to find\n"
            "the Philosopher's stone before it is to late!\n"
            "Find the stone while you explore the magic within Hogwarts,\n" 
            "but be careful, challenges will come in your way.\n"
            f"Use your skill {user_dormitory_strength} well,\n"
            "We will meet again in the end.\n"
            f"The best of luck to you {name}"))
    print()
    time.sleep(2)
    

   


def start_exploring():

    """
    Function structure borrowed from https://www.makeuseof.com/python-text-adventure-game-create/
    First choise for user to determine path
    """
    option = ["1", "2"]
    print(("It is time to begin your jorney to find the Philosopher's stone,\n"
            "you can either go to the Third Floor or the Dark Forest\n"
            "Select 1 for Third Floor\n"
            "Selecet 2 for Dark Forest ")) # Challenge description for the user
    user_input = input()
    while user_input not in option: # Displays message until user inupt is valid to option
        print("Please select 1 or 2")
        user_input = input()
    if user_input == "1": # Takes the user to the Third Floor
        clear_screen()
        third_floor() 
    else:
        if user_input == "2": # Takes the user to the Dark Forest
            clear_screen()
            dark_forest() 
    
        

def third_floor():

    """
    Function for challenge at the Third Floor
    Containing challenge description
    User input will determine the games path
    """
    print(Fore.MAGENTA + "---YOU HAVE ENTERED THE THIRD FLOOR---" + Style.RESET_ALL) # Text to show user where they are
    option = ["1", "2"]
    print(("The Third Floor is a higly forbidden area as very dangerous creatures roam here.. And yet here you are..\n"
            "You are not allowed to stay here and Mr Filch is on his way to catch you and drag you to the principal's office\n"
            "Take action now! You can either Hide or Run\n"
            "Select 1 to Run\n"
            "Select 2 to Hide")) # Challenge description for the user
    user_input = input()
    while user_input not in option: # Displays message until user inupt is valid to option
        print("Please select 1 or 2")
        user_input = input()
    if user_input == "1": # Takes the user to the Dark Forest
        clear_screen()
        dark_forest() 
    else:
        if user_input == "2": # Takes the user to meet Fluffy
            clear_screen()
            fluffy_dog() 
    




def dark_forest():

    """
    Function for challenge the Dark Forest
    Containing challenge description
    User input will determine game path
    """
    print(Fore.MAGENTA +"---YOU HAVE ENTERED THE DARK FOREST---" + Style.RESET_ALL) # Text to show user where they are
    option = ["1", "2"]
    print(("There are many magical creatures living in this forest, some of them are good and some are you worst nightmare!\n"
            f"The Dark Forest is no safe place for students, especially not you {name}..\n"
            "The Dark Lord knows what you are up to, he knows what you are trying to find\n"
            "He wants to stop you and have sent Dementors in your way\n"
            "Time to protect yourself, FAST cast a spell\n"
            "Select 1 for Expecto Patronum\n"
            "Select 2 for Expelliarmus")) # Challenge description for the user
    user_input = input()
    while user_input not in option: # Displays message until user inupt is valid to option
        print("Please select 1 or 2")
        user_input = input()
    if user_input == "1": # Takes the user to Hagrid's Hut
        clear_screen()
        hagrids_hut()
    else:
        if user_input == "2": # Takes the user to Hospital Wing
            clear_screen()
            print(Fore.MAGENTA +"---YOU HAVE ENTERED THE HOSPITAL WING---" + Style.RESET_ALL) # Text to show user where they are
            print("The dementors is to strong to be beaten by the expelliarmus spell, you are alive but hurt. Madame Pomfrey will meet you at the hospital wing.")
            hospital_wing() 
    
    

def fluffy_dog():

    """
    Function for challenge Fluffy the three headed dog
    Containing challenge description
    User input will determine game path
    """
    option = ["1", "2"]
    print(("You were able to escape Mr Filch,\n"
            "but we told you dangerous creatures roam here at the third floor\n"
            "And you hide inside the same room as Fluffy, Hagrid's three-headed dog!\n"
            "Fluffy does not like other people than his loving Hagrid, but can easily be calmed down.\n"
            "He is on hiw way to attack you! You have to distract him\n"
            "Select 1 to Play Music\n"
            "Select 2 to Jump")) # Challenge description for the user
    user_input = input()
    while user_input not in option: # Displays message until user inupt is valid to option
        print("Please selecet 1 or 2")
        user_input = input()
    if user_input == "1": # Takes the user to meet Peeves the poltergeist
        clear_screen()
        print(Fore.MAGENTA +"---YOU HAVE ENTERED THE CORRIDOR---" + Style.RESET_ALL)
        peeves_poltergeist()
    else:
        if user_input == "2": # Takes the user to Hospital wing
            clear_screen()
            print(Fore.MAGENTA +"---YOU HAVE ENTERED THE HOSPITAL VING---" + Style.RESET_ALL) # Text to show user where they are
            print("Jumping was not the way to calm that three-headed dog down\nYou are hurt and will meet madam Pomfrey at the hospital wing.")
            hospital_wing()




def hagrids_hut():
    print(Fore.MAGENTA +"---YOU HAVE ENTERED HAGRID'S HUT---" + Style.RESET_ALL) # Text to show user where they are
    option = ["1", "2"]
    print((f"Oh dear, you must be {name}, nice to finally meet you, I am Hagrid - the groundskeeper here at Hogwarts\n"
            "I saw what happened in the Dark Forest, nice patrounus you got there, the really scared the dementors away!\n"
            f"You are not far from finding the Philosopher's stone now {name}..\n"
            "I can not tell you how to find it, but if you are able to answer my question, this adventure will soon be over\n"
            "Who is the only known maker of the Philosopher's stone?\n"
            "Select 1 for Nicolas Flamel\n"
            "Select 2 for Gellert Grindelwald")) # Challenge description for the user
    user_input = input()
    while user_input not in option: # Displays message until user inupt is valid to option
        print("Please selecet 1 or 2")
        user_input = input()
    if user_input == "1": # The answer is correct and the user wins the game
        clear_screen()
        game_win()
    else:
        if user_input == "2": # Takes the user to meet Proffessor Dumbledore
            clear_screen()
            prof_dumbledore()

def hospital_wing():
    option = ["1", "2"]
    print((f"Poor {name}, finally you woke up!\n"
            "You had some serious injuries, but no worries I was able to cure them.\n"
            "Your friends left you a lot of sweets to make you feel better.\n"
            "Here try one, and you will be up walking again.\n"
            "Select 1 for Bertie Botts Every Flavor Beans\n"
            "Select 2 for Lemon Drop")) # Challenge description for the user
    user_input = input()
    while user_input not in option: # Displays message until user inupt is valid to option
        print("Please selecet 1 or 2")
        user_input = input()
    if user_input == "1": # Takes the user to meet Peeves the poltergeist
        clear_screen()
        print("---YOU HAVE ENTERED THE CORRIDOR---") # Text to show user where they are
        print("Eeeew I bet you got a bugger flavor on that bean!") # Comment from Peeves
        peeves_poltergeist()
    else:
        if user_input == "2": # Takes the user to meet Proffessor Dumbledore
            clear_screen()
            print("---YOU HAVE ENTERED THE CORRIDOR---") # Text to show user where they are
            print("Oh a Lemon Drop, that is my favourite") #Comment from Proffessor Dumbledore
            prof_dumbledore()

def peeves_poltergeist():
    option = ["1", "2"]
    print((f"HAHAHA, you silly goose, I am Peeves the poltergeist that makes Hogwarts so fun!\n"    
            "I bet you walking these corridors to find a particular stone?\n"
            "YOU WILL NOT FIND IT!!!\n"
            "Here AT LEAST...\n"
            "If you answer my question correct, you can be lucky\n"
            "But if you are wrong, this will be the end for you!!\n"
            "HAHA just kidding, but it will be the end of your journey\n"
            f"So {name}, What Is the ability of the Philosopher's Stone?\n"
            "Select 1 for the ability to make a person immortal \n"
            "Select 2 for the ability to wake people from the dead")) # Challenge description for the user
    user_input = input()
    while user_input not in option: # Displays message until user inupt is valid to option
        print("Please selecet 1 or 2")
        user_input = input()
    if user_input == "1": # The answer is correct and the user wins the game
        clear_screen()
        game_win()
    else:
        if user_input == "2": # The answer is wrong and the user loses the game
            clear_screen()
            game_lost()

def prof_dumbledore():
    option = ["1", "2"]
    print((f"It is an honor to meet you {name}, I am professor Albus Dumbledore\n"    
            "You have done a fantastic job during you journey here at Hogwarts\n"
            "I am more than impressed over you ability to fight the challenges that have come in your way.\n"
            f"You are just one step away from finding the stone now {name}\n"
            "All you have to do is to answer my question...\n"
            "Nicolas Flamel an I came up with a very clever idéa on how the stone could be found...\n"
            "So how can a person find the stone?\n"
            "Select 1 for the Desire to find it and use it\n"
            "Select 2 for the Desire to find it and not use it")) # Challenge description for the user
    user_input = input()
    while user_input not in option: # Displays message until user inupt is valid to option
        print("Please selecet 1 or 2")
        user_input = input()
    if user_input == "1": # The asnwer is wrong and the user loses the game
        clear_screen()
        game_lost()
    else:
        if user_input == "2": # The answer is correct and the user wins the game
            clear_screen()
            game_win()

def game_lost():
    option = ["Yes", "No"]
    print((f"You were not able to find the Philosopher's stone this time {name}\n"
            "Would you like to play again? Yes/No"))
    user_input = input().capitalize()
    while user_input not in option: # Displays message until user inupt is valid to option
        print("Please write Yes or No")
        user_input = input().capitalize()
    if user_input == "Yes":
        clear_screen()
        main()
    else:
        if user_input == "No":
            clear_screen()
            print(f"Thank you {name} for playing")
            

def game_win():
    show_dormitory_shield()
    option = ["Yes", "No"]
    print((f"⌁☍꒷₊˚ {name} ꒷₊˚⌁☍\n"
            "Would you like to play again? Yes/No"))
    user_input = input().capitalize()
    while user_input not in option: # Displays message until user inupt is valid to option
        print("Please write Yes or No")
        user_input = input().capitalize()
    if user_input == "Yes":
        clear_screen()
        main()
    else:
        if user_input == "No":
            clear_screen()
            print(f"Thank you {name} for playing")



def show_dormitory_shield():
    if user_dormitory_strength == "Bravery":
        print("""⬜⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛⬜
⬛⬛🟥🟥🟥🟥⬛⬛⬛⬛🟨🟨🟨🟨⬛⬛
⬛🟥🟥🟥🟥🟥🟥⬛⬛🟨🟨🟨🟨🟨🟨⬛
⬛🟥🟥🟥🟥🟥🟥🟥🟨🟨🟨🟨🟨🟨🟨⬛
⬛⬛🟥⬛🟥🟥⬛⬛⬛🟨🟨🟨⬛🟨⬛⬛
⬜⬛⬛🟥🟥⬛🟥🟥🟨⬛🟨🟨🟨⬛⬛⬜
⬜⬛⬛🟥🟥⬛🟥🟥🟨🟨🟨🟨🟨⬛⬛⬜
⬛⬛🟨🟨🟨⬛🟨🟨⬛⬛⬛🟥🟥🟥⬛⬛
⬛🟨🟨🟨🟨⬛🟨🟨🟥⬛🟥🟥🟥🟥🟥⬛
⬛🟨🟨🟨🟨🟨⬛⬛⬛⬛🟥🟥🟥🟥🟥⬛
⬛⬛🟨🟨🟨🟨🟨🟨🟥🟥🟥🟥🟥🟥⬛⬛
⬜⬛⬛⬛🟨🟨🟨🟨🟥🟥🟥🟥⬛⬛⬛⬜
⬜⬜⬜⬛⬛🟨🟨🟨🟥🟥🟥⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛🟨🟥⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜""")
    elif user_dormitory_strength == "Curiosity":
        print("""⬜⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛⬜
⬛⬛🟦🟦🟦🟦⬛⬛⬛⬛🏽🏽🏽🏽⬛⬛
⬛🟦🟦🟦🟦🟦🟦⬛⬛🏽🏽🏽🏽🏽🏽⬛
⬛🟦⬛🟦🟦🟦🟦🟦🏽🏽🏽🏽🏽⬛🏽⬛
⬛⬛🟦🟦🟦⬛⬛⬛⬛🏽🏽🏽🏽🏽⬛⬛
⬜⬛⬛🟦🟦🟦⬛🟦🏽⬛🏽🏽🏽⬛⬛⬜
⬜⬛⬛🟦🟦🟦⬛⬛⬛⬛🏽🏽🏽⬛⬛⬜
⬛⬛🏽🏽🏽🏽⬛🏽⬛🟦🟦🟦🟦🟦⬛⬛
⬛🏽🏽🏽🏽🏽⬛🏽🟦⬛🟦⬛🟦🟦🟦⬛
⬛🏽🏽🏽🏽⬛⬛🏽🟦🟦⬛🟦🟦🟦🟦⬛
⬛⬛🏽🏽🏽🏽🏽🏽🟦🟦🟦🟦🟦🟦⬛⬛
⬜⬛⬛⬛🏽🏽🏽🏽🟦🟦🟦🟦⬛⬛⬛⬜
⬜⬜⬜⬛⬛🏽🏽🏽🟦🟦🟦⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛🏽🟦⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜""")
    elif user_dormitory_strength == "Loyalty":
        print("""⬜⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛⬜
⬛⬛🟨🟨🟨🟨⬛⬛⬛⬛🏽🏽🏽🏽⬛⬛
⬛🟨🟨🟨🟨🟨🟨⬛⬛🏽🏽🏽🏽🏽🏽⬛
⬛🟨⬛🟨🟨🟨🟨🟨🏽🏽🏽🏽🏽⬛🏽⬛
⬛⬛🟨🟨🟨⬛⬛🟨🏽⬛⬛🏽🏽🏽⬛⬛
⬜⬛⬛🟨🟨🟨⬛🟨🏽⬛🏽🏽🏽⬛⬛⬜
⬜⬛⬛🟨🟨🟨⬛⬛⬛⬛🏽🏽🏽⬛⬛⬜
⬛⬛🏽🏽🏽🏽⬛🏽🟨⬛🟨🟨🟨🟨⬛⬛
⬛🏽🏽🏽🏽🏽⬛🏽🟨⬛🟨🟨🟨🟨🟨⬛
⬛🏽🏽🏽🏽⬛⬛🏽🟨⬛⬛🟨🟨🟨🟨⬛
⬛⬛🏽🏽🏽🏽🏽🏽🟨🟨🟨🟨🟨🟨⬛⬛
⬜⬛⬛⬛🏽🏽🏽🏽🟨🟨🟨🟨⬛⬛⬛⬜
⬜⬜⬜⬛⬛🏽🏽🏽🟨🟨🟨⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛🏽🟨⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜""")

    else:
        if user_dormitory_strength == "Ambition":
            print("""⬜⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛⬜
⬛⬛🟩🟩🟩🟩⬛⬛⬛⬛🏽🏽🏽🏽⬛⬛
⬛🟩🟩🟩🟩🟩🟩⬛⬛🏽🏽🏽🏽🏽🏽⬛
⬛🟩⬛🟩🟩🟩🟩🟩🏽🏽🏽🏽🏽⬛🏽⬛
⬛⬛🟩🟩🟩🟩🟩⬛⬛🏽🏽🏽🏽🏽⬛⬛
⬜⬛⬛🟩🟩🟩⬛🟩🏽⬛🏽🏽🏽⬛⬛⬜
⬜⬛⬛🟩🟩🟩⬛🟩🏽🏽🏽🏽🏽⬛⬛⬜
⬛⬛🏽🏽🏽🏽🏽⬛⬛⬛🟩🟩🟩🟩⬛⬛
⬛🏽🏽🏽🏽🏽🏽🏽🟩🟩⬛🟩🟩🟩🟩⬛
⬛🏽🏽🏽🏽⬛🏽🏽🟩🟩⬛🟩🟩🟩🟩⬛
⬛⬛🏽🏽🏽🏽⬛⬛⬛⬛🟩🟩🟩🟩⬛⬛
⬜⬛⬛⬛🏽🏽🏽🏽🟩🟩🟩🟩⬛⬛⬛⬜
⬜⬜⬜⬛⬛🏽🏽🏽🟩🟩🟩⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛🏽🟩⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜""")


"""
Borrowed from https://www.101computing.net/python-typing-text-effect/
Function to clear screen bwtween every challenge (function).
"""
def clear_screen():
    os.system("clear")


"""
Function to start the game
"""
def main():
    welcome_to()
    select_dormitory()
    start_exploring()
    show_dormitory_shield()


main ()

