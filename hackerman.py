import time as t
import sys as application
import Meet 
import inventory

def startup():
    print("Connecting...")
    t.sleep(2)
    print("Loading"),
    t.sleep(1)
    print("."),
    t.sleep(1)
    print("."),
    t.sleep(1)
    print("."),
    print("Done!")
    t.sleep(1)
    print("---------------------------------------------------------------------------------------\n")
    
def Introduction(enterName):
    print("Welcome back, Agent " + enterName + ". We have just recieved intel from HQ that the CCCP has hacked ")
    print("into our system and taken our Nuclear Launch Codes!\n\n")
    t.sleep(4)
    print("Your mission is to stop them from creating"),
    print("Nuclear Fallout by hacking into their systems")
    print("and taking those codes back. Hurry, the United States is counting on YOU, " + enterName + "!\n\n")
    t.sleep(8)

    


def startGame(enterName):
    print("Welcome to the Console, " + enterName)
    inventory.openInventory()


    
    

print "Welcome to Hacker Man. \n"
enterName = raw_input("Please Enter Your Name\n")
Meet.name = enterName





startup()
Introduction(enterName)


Meet.whoToGoTo()