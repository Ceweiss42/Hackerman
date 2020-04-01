import time as t
import inventory
#import hackerman

name = ""
meetupNames = ["Eric", "Russel", "Katherine"]
person = ""


def meetKatherine():
    t.sleep(1)
    print("Hello There, my Name is Katherine, and I am your technical analyst.")
    t.sleep(2)
    print("Here is your file for your mission.")
    t.sleep(1)
    print("Obtained "),
    print("\033[1;32;40m Target Info File"),
    print("from Katherine!")
    inventory.inventory[1] = "Target Info File"
    t.sleep(1)
    print("Good Luck Agent!\n\n")
    t.sleep(1)
    whoToGoTo()
    
def meetEric():
    t.sleep(1)
    print("Hello There, I am Eric. I will be your hacker assistant.")
    t.sleep(2)
    print("Simply use this item, and recieve a hint!")
    t.sleep(1)
    print("Obtained "),
    print("\033[1;32;40m Hint Machine"),
    print("from Eric!")
    inventory.inventory[2] = "Hint Machine " + "(" + str(inventory.hints) + ")"
    t.sleep(1)
    print("Careful though, there are only three uses!\n\n")
    t.sleep(1)
    whoToGoTo()
    
    
def meetRussel():
    t.sleep(1)
    print("Hey There. I have nothing to give you, but Good Luck!\n\n")
    whoToGoTo()

def Meetup(goToPerson):
    person = goToPerson
    if(person not in meetupNames):
        print("You silly goose, choose a name from the list!")
        Meet.whoToGoTo()
        goToPerson = raw_input()
    else:
        meetupNames.remove(goToPerson)
        
    if(goToPerson.strip() == "Katherine"):
        meetKatherine()
    
    elif(goToPerson.strip() == "Russel"):
        meetRussel()
    
    elif(goToPerson.strip() == "Eric"):
        meetEric()
    
def whoToGoTo():
    if(len(meetupNames) < 1):
        ready = raw_input("Are you ready? (y/n)")
        ready = ready.lower()
        ready = ready.strip()
        if(ready == "y" or ready == "yes"):
            print("Let's get started")
            print("---------------------------------------------------------------------------------------\n")
            hackerman.startGame(name)
        else:
            print("See you later!")
            application.exit()
        
    
    else:
        print("Who would you like to go to? ("),
        for i in range(len(meetupNames)):
            if(i is not len(meetupNames) - 1):
                print(meetupNames[i] + ", "),
            else:
                print(meetupNames[i] + ")")
        goToPerson = raw_input()
        Meetup(goToPerson)
        
