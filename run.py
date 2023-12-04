import os  # For clear screen function
import time  # For time delay between prints
from colorama import Fore, Back, Style  # Add styling to text

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
    # Hogwarts logo borrowed from
    # https://emojicombos.com/harry-potter-ascii-art

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

    print(f"Dear, {name}\nYou have been accepted "
          "to Hogwarts School for Witchcraft and Wizardry!")
    time.sleep(1)
    print("It is time to place you in the right dormitory, "
          "our four dormitories are:")
    for dormitory in dormitories.values():
        print("<---", dormitory, "--->")
    time.sleep(1)


def select_dormitory():

    """
    Function to assagin the user into the right dormitory
    based on user input from key values in dormitory list
    """
    print()
    print("We need to know your strenghts "
          "to make sure to put you in the right dormitory.\n"
          "Please choose one of these four skills "
          "that best describes you greates strength!")
    for dormitory_strength in dormitories.keys():
        print(dormitory_strength)
    # Make this global to use in show_dormitory_shield
    global user_dormitory_strength
    user_dormitory_strength = input("Please write your selected "
                                    "strength:\n").capitalize()
    while user_dormitory_strength not in dormitories.keys():
        print("Strengths: Bravery, Curiosity, Loyalty, Ambition")
        user_dormitory_strength = input("Please write your selected "
                                        "strength:\n").capitalize()

    global user_dormitory
    user_dormitory = dormitories.get(user_dormitory_strength)

    clear_screen()
    # Challenge description
    print((f"{name} you have been placed in {user_dormitory},\n"
          f"which will suit you perfectly based on your skill "
           f"{user_dormitory_strength}!\n"
           "We have a very important mission for you, we need you to find\n"
           "the Philosopher's stone before it is to late!\n"
           "Find the stone while you explore the magic within Hogwarts,\n"
           "but be careful, challenges will come in your way.\n"
           f"Use your skill {user_dormitory_strength} well,\n"
           "We will meet again in the end.\n"
           f"The best of luck to you {name}"))
    print()
    time.sleep(1)


def start_exploring():

    """
    Function structure borrowed from
    https://www.makeuseof.com/python-text-adventure-game-create/
    First choise for user to determine path
    """
    option = ["1", "2"]
    print(("It is time to begin your jorney to find the Philosopher's stone,\n"
          "you can either go to the Third Floor or the Dark Forest\n"
           "Select 1 for Third Floor\n"
           "Selecet 2 for Dark Forest "))  # Challenge description for the user
    user_input = input()
    # Displays message until user inupt is valid to option
    while user_input not in option:
        print("Please select 1 or 2")
        user_input = input()
    if user_input == "1":  # Takes the user to the Third Floor
        clear_screen()
        third_floor()
    else:
        if user_input == "2":  # Takes the user to the Dark Forest
            clear_screen()
            dark_forest()


def third_floor():

    """
    Function for challenge at the Third Floor
    Containing challenge description
    User input will determine the games path
    """
    # Text to show user where they are
    print(Fore.MAGENTA +
          "---YOU HAVE ENTERED THE THIRD FLOOR---" + Style.RESET_ALL)
    option = ["1", "2"]
    print(("The Third Floor is a higly forbidden area as very dangerous "
          "creatures roam here\n"
           "And yet here you are..\n"
           "You are not allowed to stay here..\nMr Filch is on his way "
           "to catch you and drag you to the principal's office\n"
           "Take action now! You can either Hide or Run\n"
           "Select 1 to Run\n"
           "Select 2 to Hide"))  # Challenge description for the user
    user_input = input()
    # Displays message until user inupt is valid to option
    while user_input not in option:
        print("Please select 1 or 2")
        user_input = input()
    if user_input == "1":  # Takes the user to the Dark Forest
        clear_screen()
        dark_forest()
    else:
        if user_input == "2":  # Takes the user to meet Fluffy
            clear_screen()
            fluffy_dog()


def dark_forest():

    """
    Function for challenge the Dark Forest
    Containing challenge description
    User input will determine game path
    """
    # Text to show user where they are
    print(Fore.MAGENTA +
          "---YOU HAVE ENTERED THE DARK FOREST---" + Style.RESET_ALL)
    option = ["1", "2"]
    print(("There are many magical creatures living in this forest, "
          "some of them are good..\nAnd some are you worst nightmare!\n"
           f"The Dark Forest is no safe place for students, "
           "especially not you {name}..\n"
           "The Dark Lord knows what you are up to, "
           "he knows what you are trying to find\n"
           "He wants to stop you and have sent Dementors in your way\n"
           "Time to protect yourself, FAST cast a spell\n"
           "Select 1 for Expecto Patronum\n"
           "Select 2 for Expelliarmus"))  # Challenge description for the user
    user_input = input()
    # Displays message until user inupt is valid to option
    while user_input not in option:
        print("Please select 1 or 2")
        user_input = input()
    if user_input == "1":  # Takes the user to Hagrid's Hut
        clear_screen()
        hagrids_hut()
    else:
        if user_input == "2":  # Takes the user to Hospital Wing
            clear_screen()
            # Text to show user where they are
            print(Fore.MAGENTA +
                  "---YOU HAVE ENTERED THE HOSPITAL WING---" + Style.RESET_ALL)
            print("The dementors is to strong to be beaten by the expelliarmus"
                  " spell,\n you are alive but hurt.\n"
                  "Madame Pomfrey will meet you at the hospital wing.")
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
           "And you hide inside the same room as Fluffy, "
           "Hagrid's three-headed dog!\n"
           "Fluffy does not like other people than his loving Hagrid,\n"
           "but can easily be calmed down.\n"
           "He is on hiw way to attack you! You have to distract him\n"
           "Select 1 to Play Music\n"
           "Select 2 to Jump"))  # Challenge description for the user
    user_input = input()
    # Displays message until user inupt is valid to option
    while user_input not in option:
        print("Please selecet 1 or 2")
        user_input = input()
    if user_input == "1":  # Takes the user to meet Peeves the poltergeist
        clear_screen()
        # Text to show user where they are
        print(Fore.MAGENTA +
              "---YOU HAVE ENTERED THE CORRIDOR---" + Style.RESET_ALL)
        print("I am chocked that horrible music could distract Fluffy,\n"
              "I was sure you were going to be dog food! ")
        peeves_poltergeist()
    else:
        if user_input == "2":  # Takes the user to Hospital wing
            clear_screen()
            # Text to show user where they are
            print(Fore.MAGENTA +
                  "---YOU HAVE ENTERED THE HOSPITAL VING---" + Style.RESET_ALL)
            print("Jumping was not the way to calmdown that three-headed dog\n"
                  "You are hurt and will meet madam Pomfrey "
                  "at the hospital wing.")
            hospital_wing()


def hagrids_hut():

    """
    Function for challenge Hagrid's Hut
    Containing challenge description
    User input will determine game path
    """
    # Text to show user where they are
    print(Fore.MAGENTA +
          "---YOU HAVE ENTERED HAGRID'S HUT---" + Style.RESET_ALL)
    option = ["1", "2"]
    # Challenge description for the user
    print((f"Oh, you must be {name}, nice to finally meet you, I am Hagrid\n"
          "The groundskeeper here at Hogwarts\n"
           "I saw what happened in the Dark Forest, that patronus really"
           " scared the dementors away!\n"
           f"You are not far from finding the Philosopher's stone now {name}\n"
           "I can not tell you how to find it, but if you are able to answer "
           "my question,\nthis adventure will soon be over..\n"
           "Who is the only known maker of the Philosopher's stone?\n"
           "Select 1 for Nicolas Flamel\n"
           "Select 2 for Gellert Grindelwald"))
    user_input = input()
    # Displays message until user inupt is valid to option
    while user_input not in option:
        print("Please selecet 1 or 2")
        user_input = input()
    if user_input == "1":  # The answer is correct and the user wins the game
        clear_screen()
        game_win()
    else:
        if user_input == "2":  # Takes the user to meet Proffessor Dumbledore
            clear_screen()
            print(f"To bad {name}, that was not the one... but come with me!"
                  "I want you to meet someone special.")
            print()
            prof_dumbledore()


def hospital_wing():

    """
    Function for challenge Hospital Wing
    Containing challenge description
    User input will determine game path
    """
    option = ["1", "2"]
    # Adding space between text when user comes from Hagrid's hut & Fluffy Dog
    print()
    time.sleep(1)
    print((f"Poor {name}, finally you woke up!\n"
           "You had some serious injuries, but no worries "
           "I was able to cure them.\n"
           "Your friends left you a lot of sweets to make you feel better.\n"
           "Here try one, and you will be up walking again.\n"
           "Select 1 for Bertie Botts Every Flavor Beans\n"
           "Select 2 for Lemon Drop"))  # Challenge description for the user
    user_input = input()
    # Displays message until user inupt is valid to option
    while user_input not in option:
        print("Please selecet 1 or 2")
        user_input = input()
    if user_input == "1":  # Takes the user to meet Peeves the poltergeist
        clear_screen()
        # Text to show user where they are
        print(Fore.MAGENTA +
              "---YOU HAVE ENTERED THE CORRIDOR---" + Style.RESET_ALL)
        # Comment from Peeves
        print("Eeeew I bet you got a bugger flavor on that bean!")
        peeves_poltergeist()
    else:
        if user_input == "2":  # Takes the user to meet Proffessor Dumbledore
            clear_screen()
            # Text to show user where they are
            print(Fore.MAGENTA +
                  "---YOU HAVE ENTERED THE CORRIDOR---" + Style.RESET_ALL)
            # Comment from Proffessor Dumbledore
            print("Oh a Lemon Drop, that is my favourite")
            prof_dumbledore()


def peeves_poltergeist():

    """
    Function for challenge Peeves Poltergeist
    Containing challenge description
    User input will lead to win or loss
    """
    option = ["1", "2"]
    # Challenge description for the user
    print((f"HAHAHA, you silly goose, I am Peeves the poltergeist "
          "that makes Hogwarts so fun!\n"
           "I bet you walking these corridors to find a particular stone?\n"
           "YOU WILL NOT FIND IT!!!\n"
           "Not here AT LEAST...\n"
           "If you answer my question correct, you can be lucky\n"
           "But if you are wrong, this will be the end for you!!\n"
           "HAHA just kidding, but it will be the end of your journey\n"
           f"So {name}, What Is the Ability of the Philosopher's Stone?\n"
           "Select 1 for the ability to make a person immortal \n"
           "Select 2 for the ability to wake people from the dead"))
    user_input = input()
    # Displays message until user inupt is valid to option
    while user_input not in option:
        print("Please selecet 1 or 2")
        user_input = input()
    if user_input == "1":  # The answer is correct and the user wins the game
        clear_screen()
        game_win()
    else:
        # The answer is wrong and the user loses the game
        if user_input == "2":
            clear_screen()
            game_lost()


def prof_dumbledore():

    """
    Function for challenge Prof Dumbledore
    Containing challenge description
    User input will lead to win or loss
    """
    option = ["1", "2"]
    # Challenge description for the user
    print((f"It is an honor to meet you {name}, "
          "I am professor Albus Dumbledore\n"
           "You have done a fantastic job during your "
           "journey here at Hogwarts\n"
           "I am more than impressed over you ability to fight the "
           "challenges\nthat have come in your way.\n"
           f"You are just one step away from finding the stone now {name}\n"
           "All you have to do is to answer my question...\n"
           "Nicolas Flamel an I came up with a very clever idéa\n"
           "on how the stone could be found...\n"
           "So how can a person find the stone?\n"
           "Select 1 for the Desire to find it and use it\n"
           "Select 2 for the Desire to find it and not use it"))
    user_input = input()
    # Displays message until user inupt is valid to option
    while user_input not in option:
        print("Please selecet 1 or 2")
        user_input = input()
    if user_input == "1":  # The asnwer is wrong and the user loses the game
        clear_screen()
        game_lost()
    else:
        # The answer is correct and the user wins the game
        if user_input == "2":
            clear_screen()
            game_win()


def game_lost():

    """
    Function for game lost
    Containing dormitory shield based on user input from dormitories list
    and text that user lost the game
    User will be asked to play again with input Yes/No
    If user input Yes, game will start over
    If user input No program will stop running.
    """
    show_dormitory_shield()
    print()  # Adding space between dormitory shield and text
    option = ["Yes", "No"]
    print((f"You were not able to find the Philosopher's stone this "
          "time {name}\n"
           "We are sure that you did your best!\n"
           f"And {user_dormitory} should be proud of having "
           "you in their dormitory!\n"
           "Would you like to play again? Yes/No"))
    user_input = input().capitalize()
    # Displays message until user inupt is valid to option
    while user_input not in option:
        print("Please write Yes or No")
        user_input = input().capitalize()
    if user_input == "Yes":
        clear_screen()
        main()
    else:
        if user_input == "No":
            clear_screen()
            print(f"Thank you {name} for playing!")


def game_win():

    """
    Function for Game Win
    Containing dormitory shield based on user input from dormitories list
    and text that user won the game
    User will be asked to play again with input Yes/No
    If user input Yes, game will start over
    If user input No program will stop running.
    """
    show_dormitory_shield()
    print()  # Adding space between dormitory shield and text
    option = ["Yes", "No"]
    print((f"⌁☍꒷₊˚ {user_dormitory} WINS! ꒷₊˚⌁☍\n"
          f"What a fantastic job you did {name}\n"
           "We are so proud of you that you saved Hogwarts "
           "by finding the stone!\n"
           "Would you like to play again? Yes/No"))
    user_input = input().capitalize()
    # Displays message until user inupt is valid to option
    while user_input not in option:
        print("Please write Yes or No")
        user_input = input().capitalize()
    if user_input == "Yes":
        clear_screen()
        main()
    else:
        if user_input == "No":
            clear_screen()
            print(f"Thank you {name} for playing!")


def show_dormitory_shield():

    """
    Function to show dormitory shield if game is won or lost
    Which shield that shows are based on the user input from dormitories list
    """
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


def clear_screen():
    """
    Borrowed from https://www.101computing.net/python-typing-text-effect/
    Function to clear screen bwtween every challenge (function).
    """
    os.system("clear")


def main():

    """
    Function to start the game
    """
    welcome_to()
    select_dormitory()
    start_exploring()


main()
