from db import db
import sys
# this is where I will have a lot of the options come from

class Characters:
    def __init__(self,story, choices):
        self.story = story
        self.choices = choices

class Cowboy(Characters):
    def __init__(self, story, choices):
        super().__init__(story, choices)

    #make a new method seperate from the init method
        self.story = db["cowboy_intro"]
        print(self.story)
        self.choice = input("Do you shoot back? (yes/no) ").lower().strip()
        if self.choice == "yes":
            self.story = db["cowboy text"]
            print(self.story)
            self.choice = input("Do you go back to the police station? (yes/no) ").lower().strip()
            if self.choice == "yes":
                self.story = db["cowboy ending"]
                print(self.story)
                self.story = db["end"]
                print(self.story)
                sys.exit()
            elif self.choice == "no":
                self.story = db["cowboy bad ending"]
                print(self.story)
                self.story = db["end"]
                print(self.story)
                sys.exit()
        # second quest line
        elif self.choice == "no":
            self.story = db["cowboy 2 text"]
            print(self.story)
            self.choice = input("Do you go after the bank robber? (yes/no) ").lower().strip()
            if self.choice == "yes":
                self.story = db["cowboy 2 bad ending"]
                print(self.story)
                self.story = db["end"]
                print(self.story)
                sys.exit()
            elif self.choice == "no":
                self.story = db["cowboy 2 ending"]
                print(self.story)
                self.story = db["end"]
                print(self.story)
                sys.exit()

# SPACE MARINE
class SpaceMarine(Characters):
    def __init__(self, story, choices):
        super().__init__(story, choices)
        self.story = db["space marine intro"]
        print(self.story)
        self.choice = input("Do you open the door? (yes/no) ").lower().strip()
        if self.choice == "yes":
            self.story = db["space marine text"]
            print(self.story)
            self.choice = input("Do you blow up the building? (yes/no) ").lower().strip()
            if self.choice == "yes":
                self.story = db["space marine ending"]
                print(self.story)
                self.story = db["end"]
                print(self.story)
                sys.exit()
            elif self.choice == "no":
                self.story = db["space marine lose"]
                print(self.story)
                self.story = db["end"]
                print(self.story)
                sys.exit()
        # second quest line
        elif self.choice == "no":
            self.story = db["space marine 2 text"]
            print(self.story)
            self.choice = input("Do you stay on course for the subway? (yes/no) ").lower().strip()
            if self.choice == "yes":
                self.story = db["space marine 2 ending"]
                print(self.story)
                self.story = db["end"]
                print(self.story)
                sys.exit()
            elif self.choice == "no":
                self.story = db["space marine 2 lose"]
                print(self.story)
                self.story = db["end"]
                print(self.story)
                sys.exit()

# KNIGHT
class Knight(Characters):
    def __init__(self, story, choices):
        super().__init__(story, choices)
        self.story = db["knight intro"]
        print(self.story)
        self.choice = input("Do you go left or right? (left/right)").lower().strip()
        if self.choice == "left":
            self.story = db["knight text"]
            print(self.story)
            self.choice = input("do you go down the hill? (yes/no) ").lower().strip()
            if self.choice == "yes":
                self.story = db["knight ending"]
                print(self.story)
                self.story = db["end"]
                print(self.story)
                sys.exit()
            elif self.choice == "no":
                self.story = db["knight lose"]
                print(self.story)
                self.story = db["end"]
                print(self.story)
                sys.exit()

        # second quest line
        elif self.choice == "right":
            self.story = db["knight 2 text"]
            print(self.story)
            self.choice = input("Do i get off the horse? (yes/no)").lower().strip()
            if self.choice == "yes":
                self.story = db["knight 2 ending"]
                print(self.story)
                self.story = db["end"]
                print(self.story)
                sys.exit()
            elif self.choice == "no":
                self.story = db["knight 2 lost"]
                print(self.story)
                self.story = db["end"]
                print(self.story)
                sys.exit()
