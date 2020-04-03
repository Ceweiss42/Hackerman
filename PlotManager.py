import inventory
import BoolManager
import sys as application
import time as t
def startGame(enterName):
    inventory.name = enterName
    BoolManager.print_slow("Welcome to the Console, " + enterName, .06)
    levelOne(enterName)
    
def levelOne(name):
    BoolManager.level = "One"
    BoolManager.print_slow("\n~"+name+"$ host connect ______", .06)
    BoolManager.print_slow("\nWhat is the IP address you are connecting to? (openInv or IP Address)", .06)
    option = raw_input()
    if(option == "openInv"):
        inventory.openInventory()
        if "Hint Machine" not in inventory.inventory and BoolManager.hintUsed == "One":
            levelTwo(name)
        else:
            levelOne(name)

    elif(option == "12.544.178"):
        BoolManager.print_slow("\nYou have successfully connected to IP host: 12.544.178", .06)
        levelTwo(name)

    else:
        BoolManager.print_slow("\nincorrect option, please try again", .06)
        levelOne(name)

def levelTwo(name):
    BoolManager.level = "Two"
    BoolManager.print_slow("\n"+"~"+name+"$ IP.track", .06)
    BoolManager.print_slow("\nYou need to enter the password first", .06)
    password = raw_input()
    if password == "Yogi":
        BoolManager.print_slow("\ntracking successful", .06)
        levelThree(name)
    elif password == "openInv":
        inventory.openInventory()
        if "Hint Machine" not in inventory.inventory and BoolManager.hintUsed == "Two":
            levelThree(name)
        else:
            levelTwo(name)
    else:
        BoolManager.print_slow("\nincorrect option, try again", .06)
        levelTwo(name)
    
def levelThree(name):
    BoolManager.level = "Three"
    BoolManager.print_slow("\nIt Looks like there is a riddle we need to solve", .06)
    BoolManager.print_slow("\nWhat has to be Broken before you can use it?", .06)
    riddle = raw_input()
    if riddle == "openInv":
        inventory.openInventory()
        if "Hint Machine" not in inventory.inventory and BoolManager.hintUsed == "Three":
            levelFour(name)
        else:
            levelThree(name)
    elif riddle == "Egg":
        levelFour(name)
    
    else:
        levelThree(name)
        
def levelFour(name):
    BoolManager.level = "Four"
    BoolManager.print_slow("\naccess granted", .06)
    BoolManager.print_slow("\nWhat was the host?\n", .06)
    host = raw_input()
    if host == "pop3.ru":
        BoolManager.print_slow("\n~"+name+"$ IP connect host:pop3.ru", .06)
        BoolManager.print_slow("\n~"+name+"$ com.connect search file.contains(launchCode)", .06)
        for i in range(4):
            BoolManager.print_slow("\nfile "+str(i)+": clear", .06)
            t.sleep(.5)
        BoolManager.print_slow("\nfile 5: contains", .06)
        
        for i in range(4):
            BoolManager.print_slow("\nfile "+str(i + 6)+": clear", .06)
            t.sleep(.5)
        
        file = raw_input("\nselect a file number")
        if(file == "5"):
            levelFive(name)
        elif file == "openInv":
            inventory.openInventory()
            if "Hint Machine" not in inventory.inventory and BoolManager.hintUsed == "Four":
                levelFive(name)
            else:
                levelFour(name)
    
    elif host == "openInv":
        inventory.openInventory()
        if "Hint Machine" not in inventory.inventory and BoolManager.hintUsed == "Four":
            levelFive(name)
        else:
            levelFour(name)

def levelFive(name):
    BoolManager.print_slow("Congratulations, Agent! You have found the Nuclear Launch Codes! The United States thanks you!", .06)
    application.exit()