import BoolManager

hintUsed = "false"

def useHint():
    print("\nYou used a hint!")
    inventory.remove("Hint Machine")
    BoolManager.hintUsed = BoolManager.level

def openInventory():
    print("Inventory:")
    for i in range(len(inventory)):
        print("|||" + inventory[i] + "|||"),
    
    choice = raw_input("\nWhat would you like to use?")
    if(choice.lower() == "file" or choice.lower() == "target info file"):
        openInfo()
    elif choice.lower() == "hint" or choice.lower() == "hint machine":
        if("Hint Machine" in inventory):
            useHint()


inventory = []
name = ""

def openInfo():
    print(" _______________________________________")
    BoolManager.print_slow("| Name: Vladimir Levin     Age: 25      |\n", .06)
    BoolManager.print_slow("| IP:12.544.178            Host:pop3.ru |\n", .06)
    BoolManager.print_slow("| Brother: Yogi                         |\n", .06)
    print(" _______________________________________")
