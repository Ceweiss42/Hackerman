import time as t
import sys as application
import Meet 
import inventory
import BoolManager


def startup():
    print("Connecting...")
    t.sleep(2)
    print("Loading"),
    BoolManager.print_slow("............Done!\n", .15)
    t.sleep(1)
    print("---------------------------------------------------------------------------------------\n")
    
def Introduction(enterName):
    BoolManager.print_slow("Welcome back, Agent " + enterName + ". We have just recieved intel from HQ that the CCCP has hacked \n", .06)
    BoolManager.print_slow("into our system and taken our Nuclear Launch Codes!\n\n", .06)
    t.sleep(1)
    BoolManager.print_slow("Your mission is to stop them from creating Nuclear Fallout by hacking into \ntheir systems ", .06)
    BoolManager.print_slow("and taking those codes back. Hurry, the United States is counting on YOU, " + enterName + "!\n\n", .06)
    t.sleep(1)

BoolManager.print_slow("Welcome to Hacker Man. \n", .06)
enterName = raw_input("Please Enter Your Name\n")
Meet.name = enterName





startup()
Introduction(enterName)


Meet.whoToGoTo()
