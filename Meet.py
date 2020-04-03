import time as t
import inventory
import PlotManager
import BoolManager

name = ""
meetupNames = ["Eric", "Russel", "Katherine"]
person = ""


def meetKatherine():
    t.sleep(1)
    BoolManager.print_slow("Hello There, my Name is Katherine, and I am your technical analyst.\n", .06)
    t.sleep(2)
    BoolManager.print_slow("Here is your file for your mission.\n", .06)
    t.sleep(1)
    BoolManager.print_slow("Obtained ", .06),
    print("\033[1;32;40m Target Info File "),
    BoolManager.print_slow("from Katherine!\n", .06)
    inventory.inventory.append("Target Info File")
    t.sleep(1)
    BoolManager.print_slow("Good Luck Agent!\n\n", .06)
    t.sleep(1)
    whoToGoTo()
    
def meetEric():
    t.sleep(1)
    BoolManager.print_slow("Hello There, I am Eric. I will be your hacker assistant.\n", .06)
    t.sleep(2)
    BoolManager.print_slow("Simply use this item, and recieve a hint!\n", .06)
    t.sleep(1)
    BoolManager.print_slow("Obtained ", .06),
    print("\033[1;32;40m Hint Machine "),
    BoolManager.print_slow("from Eric!\n", .06)
    inventory.inventory.append("Hint Machine")
    t.sleep(1)
    BoolManager.print_slow("Careful though, there is only one use!\n\n", .06)
    t.sleep(1)
    whoToGoTo()
    
    
def meetRussel():
    t.sleep(1)
    BoolManager.print_slow("Hey There. I have nothing to give you, but Good Luck!\n\n", .06)
    whoToGoTo()

def Meetup(goToPerson):
    person = goToPerson
    if(person not in meetupNames):
        BoolManager.print_slow("You silly goose, choose a name from the list!\n", .06)
        whoToGoTo()
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
            BoolManager.print_slow("Let's get started\n", .06)
            print("---------------------------------------------------------------------------------------\n")
            PlotManager.startGame(name)
        else:
            BoolManager.print_slow("See you later!", .06)
            application.exit()
        
    else:
        BoolManager.print_slow("Who would you like to go to? (", .06),
        for i in range(len(meetupNames)):
            if(i is not len(meetupNames) - 1):
                BoolManager.print_slow(meetupNames[i] + ", ", .06),
            else:
                BoolManager.print_slow(meetupNames[i] + ")\n", .06)
        goToPerson = raw_input()
        Meetup(goToPerson)
