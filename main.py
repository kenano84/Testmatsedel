import os, sys, time
import random


sl = []
category = []
fish = []
meat = []
vego = []
chicken = []

try:
    f = open("fish.txt", "r")
    for line in f:
        fish.append(line.strip())
    f.close()
except:
    pass

try:
    f = open("meat.txt", "r")
    for line in f:
        meat.append(line.strip())
    f.close()
except:
    pass

try:
    f = open("vege.txt", "r")
    for line in f:
        vego.append(line.strip())
    f.close()
except:
    pass

try:
    f = open("chicken.txt", "r")
    for line in f:
        chicken.append(line.strip())
    f.close()
except:
    pass

try:
    f = open("shopping2.txt", "r")
    for line in f:
        sl.append(line.strip())
    f.close()
except:
    pass


def mainScreen():
    os.system('cls')  # for linux 'clear'
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("     Weekly foods!    ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("\n\nYour list contains", len(sl), "items.\n")
    print("Please choose from the following options:\n")
    print("(a)dd to the food list")
    print("(d)elete from food the list")
    print("(v)iew the food list")
    print("(q)uit the program")
    print("(r)andom weekly food list")
    choice = input("\nchoice: ")
    if len(choice) > 0:
        if choice.lower()[0] == "a":
            addScreen()
        elif choice.lower()[0] == "d":
            deleteScreen()
        elif choice.lower()[0] == "v":
            viewScreen()
        elif choice.lower()[0] == "q":
            sys.exit()
        elif choice.lower()[0] == "r":
            randomWeek()
        else:
            mainScreen()
    else:
        mainScreen()


def addScreen():
    global sl
    os.system('cls')  # for linux 'clear'
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("      LIST    ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("\n\nYour list contains", len(sl), "items.\n")
    print("Please choose from the following options:\n")
    print("(a)dd food to category")
    print("(d)elete from food the category")
    print("(v)iew the food from category")
    print("(m)ain menu")
    choice = input("\nchoice: ")
    if len(choice) > 0:
        if choice.lower()[0] == "a":
            addCategory()
        elif choice.lower()[0] == "d":
            deleteScreen()
        elif choice.lower()[0] == "v":
            viewScreen()
        elif choice.lower()[0] == "m":
            mainScreen()
        else:
            mainScreen()
    else:
        mainScreen()


def addCategory():
    global sl
    os.system('cls')  # for linux 'clear'
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("     Food Category    ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("\n\nYour list contains", len(sl+chicken+fish+meat), "items.\n")
    print("Please choose from the following options:\n")
    print("(f)ish food ")
    print("(m)eat food ")
    print("(v)egetarian food ")
    print("(c)hicken food ")
    print("(n)ew Category")
    print("(m)ain menu")
    choice = input("\nchoice: ")
    if len(choice) > 0:
        if choice.lower()[0] == "f":
            addFish()
        elif choice.lower()[0] == "m":
            addMeat()
        elif choice.lower()[0] == "v":
            addVego()
        elif choice.lower()[0] == "c":
            addChicken()
        elif choice.lower()[0] == "m":
            mainScreen()
        elif choice.lower()[0] == "n":
            newCat()
        else:
            mainScreen()
    else:
        mainScreen()

def newCat():
    global sl
    os.system('cls')  # for linux 'clear'
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("     New Category    ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("\n\nYour list contains", len(sl), "items.\n")
    print("Please enter the name of the new category:\n")
    f = open(input()+ ".txt", mode="w")
    print("Item added :-)")
    time.sleep(2)
    f.close
    addCategory()



def addFish():
    global sl
    os.system('cls')  # for linux 'clear'
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("     add fish dish    ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("\n\n")
    print("Please enter the name of the item that you want to add.")
    print("Press ENTER to return to the main menu.\n")
    item = input("\nItem: ")
    if len(item) > 0:
        fish.append(item)
        print("Item added :-)")
        saveFish()
        time.sleep(1)
        addFish()
    else:
        mainScreen()


def addMeat():
    global sl
    os.system('cls')  # for linux 'clear'
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("     add meat dish    ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    item = input("\nItem: ")
    if len(item) > 0:
        meat.append(item)
        print("Item added :-)")
        saveMeat()
        time.sleep(1)
        addMeat()
    else:
        mainScreen()


def addVego():
    global sl
    os.system('cls')  # for linux 'clear'
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("     add vegetarian dish    ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    item = input("\nItem: ")
    if len(item) > 0:
        vego.append(item)
        print("Item added :-)")
        saveVego()
        time.sleep(1)
        addVego()
    else:
        mainScreen()

def addChicken():
    global sl
    os.system('cls')  # for linux 'clear'
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("     add Chicken dish    ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("\n\n")
    print("Please enter the name of the item that you want to add.")
    print("Press ENTER to return to the main menu.\n")
    item = input("\nItem: ")
    if len(item) > 0:
        chicken.append(item)
        print("Item added :-)")
        saveChicken()
        time.sleep(1)
        addChicken()
    else:
        mainScreen()


def viewScreen():
    os.system('cls')  # for linux 'clear'
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("    View LIST    ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("\n\nYour list contains", len(sl), "items.\n")
    print("Please choose from the following options:\n")
    print("(f) to see your Fish list")
    print("(m) to see your Meat list")
    print("(v) to see your Vego list")
    print("(c) to see your Chicken list")
    print("(q)uit the program")

    choice = input("\nchoice: ")
    if len(choice) > 0:
        if choice.lower()[0] == "f":
            viewFish()
        elif choice.lower()[0] == "m":
            viewMeat()
        elif choice.lower()[0] == "v":
            viewvego()
        elif choice.lower()[0] == "c":
            viewChicken()
        elif choice.lower()[0] == "q":
            sys.exit()
        else:
            mainScreen()
    else:
        mainScreen()


def viewCat():
    os.system('cls')  # for linux 'clear'
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("     VIEW Category    ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("\n\n")
    for item in category:
        print(item)

    print("\n\n")
    print("Press enter to return to the main menu")
    input()
    mainScreen()


def viewFish():
    os.system('cls')  # for linux 'clear'
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("     VIEW Fish category    ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("\n\n")
    for item in fish:
        print(item)

    print("\n\n")
    print("Press enter to return to the main menu")
    input()
    mainScreen()


def viewMeat():
    os.system('cls')  # for linux 'clear'
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("     VIEW Meat category    ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("\n\n")
    for item in meat:
        print(item)

    print("\n\n")
    print("Press enter to return to the main menu")
    input()
    mainScreen()


def viewvego():
    os.system('cls')  # for linux 'clear'a
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("     VIEW Vego category    ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("\n\n")
    for item in vego:
        print(item)

    print("\n\n")
    print("Press enter to return to the main menu")
    input()
    mainScreen()

def viewChicken():
    os.system('cls')  # for linux 'clear'a
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("     VIEW Chicken category    ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("\n\n")
    for item in chicken:
        print(item)

    print("\n\n")
    print("Press enter to return to the main menu")
    input()
    mainScreen()


def deleteScreen():
    global sl
    os.system('cls')  # for linux 'clear'
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("     DELETE SCREEN    ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    count = 0
    for item in sl+meat+fish+vego:
        print(count, " - ", item)
        count = count + 1
    print("What number to delete?")
    choice = input("number: ")
    if len(choice) > 0:
        try:
            del sl[int(choice)]
            print("Item deleted...")
            saveList()
            time.sleep(1)
        except:
            print("Invalid number")
            time.sleep(1)
        deleteScreen()

    else:
        mainScreen()


def saveList():
    f = open("shopping2.txt", "w")
    for item in sl:
        f.write(item + "\n")
    f.close()


def saveCategory():
    f = open("categories.txt", "w")
    for item in category:
        f.write(item + "\n")
    f.close()


def saveFish():
    f = open("fish.txt", "w")
    for item in fish:
        f.write(item + "\n")
    f.close()


def saveMeat():
    f = open("meat.txt", "w")
    for item in meat:
        f.write(item + "\n")
    f.close()


def saveVego():
    f = open("vege.txt", "w")
    for item in vego:
        f.write(item + "\n")
    f.close()

def saveChicken():
    f = open("chicken.txt", "w")
    for item in vego:
        f.write(item + "\n")
    f.close()


def randomWeek():
    categories = ['Fish', 'Chicken', 'Meat', 'Vegetarian']


    week_days = ['Monday ', 'Tuesday ', 'Wednesday ',
                 'Thursday ', 'Friday ', 'Saturday ', 'Sunday ']

    for day in week_days:
        prevday = day

        print(prevday)
        categoryrandom = random.choice(categories)

        if categoryrandom == 'Fish':
            cat = fish
            prevday == categoryrandom
            n = random.randint(0, len(cat) - 1)
            meal = cat[n]
            print('Fish: ' + str(meal))

        if categoryrandom == 'Chicken':
            cat = chicken
            prevday == categoryrandom
            n = random.randint(0, len(cat) - 1)
            meal = cat[n]
            print('Chicken: ' + str(meal))

        if categoryrandom == 'Meat':
            cat = meat
            prevday == categoryrandom
            n = random.randint(0, len(cat) - 1)
            meal = cat[n]
            print('Meat: ' + str(meal))

        if categoryrandom == 'Vegetarian':
            cat = vego
            prevday == categoryrandom
            n = random.randint(0, len(cat) - 1)
            meal = cat[n]
            print('Vego: ' + str(meal))


mainScreen()
