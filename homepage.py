from user import *
import sys
# this is where i will create the menu function and all of the visual side of code
print("-----------------------WELCOME TO TEXT ADVENTURE-----------------------")
intro_text = """
This is a text adventure game where you get to select between 3 interactive stories set in
3 alternate time periods. Once you have selected your story, you will make decisions that have 
consequences. \n 
"""

cowboy_text = """
1) COWBOY:
It's the early 1920's. You are a cowboy with a prestigeous title. You are well known for being
a bounty hunter.\n 
"""

space_marine_text = """
2) SPACE MARINE:
The world has been invaded by an unknown entity that is causing chaos in New York City
your mission is to figure why they have invaded Earth.\n
"""

knight_text = """
3) KNIGHT:
A kingdom is worried after the Kings right hand knight went out into the wilderness
plains outside the castle to find his daughter after she had been kidnapped.\n
"""

def introduction():
    user_input = input("would you like to play? (yes/no) ").lower().strip()
    if user_input == "yes":
        print(cowboy_text)
        print(space_marine_text)
        print(knight_text)
        print("4) Exit game")
    elif user_input == "no":
        print("Good Bye")
        sys.exit()
    else:
        print("Invalid please try again")
        user_input = input("would you like to play? (yes/no) \n").lower().strip()
        if user_input != "yes":
            sys.exit()

# this is where the user selects what story they would like to partake in
def story_selector():
    input_user = int(input("choose a story : "))
    if input_user == 1:
        print("You have selected COWBOY...")
        cowboy = Cowboy("cowboy_story","cowboy_choice")
        print(Cowboy("cowboy_story","cowboy_choice"))
    if input_user == 2:
        print("You have selected SPACE MARINE...")
        space_marine = SpaceMarine("knight_story","knight_choice")
        print(SpaceMarine("knight_story","knight_chocie"))
    if input_user == 3:
        print("You have selected KNIGHT...")
        knight = Knight("knight_story","knight_choice")
        print(Knight("knight_story","knight_choice"))
    elif input_user == 4:
        print("You have left game")
        sys.exit()