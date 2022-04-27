import os, sys, time
import random

import item as item

sl = []
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
    print("     SHOPPING LIST    ")
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
    print("     SHOPPING LIST    ")
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
    print("\n\nYour list contains", len(sl), "items.\n")
    print("Please choose from the following options:\n")
    print("(f)ish food ")
    print("(m)eat food ")
    print("(v)egetarian food ")
    print("(m)ain menu")
    choice = input("\nchoice: ")
    if len(choice) > 0:
        if choice.lower()[0] == "f":
            addFish()
        elif choice.lower()[0] == "m":
            addMeat()
        elif choice.lower()[0] == "v":
            addVege()
        elif choice.lower()[0] == "m":
            mainScreen()
        else:
            mainScreen()
    else:
        mainScreen()


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
        sl.append(item)
        print("Item added :-)")
        saveList()
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
        sl.append(item)
        print("Item added :-)")
        saveList()
        time.sleep(1)
        addMeat()
    else:
        mainScreen()

def addVege():
    global sl
    os.system('cls')  # for linux 'clear'
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("     add vegetarian dish    ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    item = input("\nItem: ")
    if len(item) > 0:
        sl.append(item)
        print("Item added :-)")
        saveList()
        time.sleep(1)
        addVege()
    else:
        mainScreen()



def viewScreen():
    os.system('cls')  # for linux 'clear'
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("     VIEW SCREEN    ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("\n\n")
    for item in sl:
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
    for item in sl:
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


def randomWeek():

    categories = ['fisk', 'Kyckling', 'kött', 'vegetariskt']

    category = [
        ['Lax & potatis', 'Fiskpinnar & pommes',
         'Torsk & koktpotatis', 'Fiskgratäng', 'Fisksoppa'],
        ['Tikimasala & Ris', 'Kyckling grönpesto & pasta', 'Kycklingfile & klyftpotatis'],
        ['Korv & Makaroner', 'Köttbullar & Potatismos', 'ChiliConCarne',
         'Spagetti & köttfärsås', 'Lasange', 'Korvstroganoff', 'köttfärs Rödpesto & Ris'],
        ['Falafel', 'Mjadara', 'Spenatsoppa', 'Makhlota',
         'Kräftsoppa', 'Ärtsoppa', 'Bakpotatis']
    ]

    week_days = ['Monday ', 'Tuesday ', 'Wednesday ',
                 'Thursday ', 'Friday ', 'Saturday ', 'Sunday ']

    for day in week_days:
        prevday = day

        print(prevday)
        catrandom = random.choice(categories)
        todaycat = catrandom

        checkday = prevday == catrandom

        if catrandom == 'fisk':
            cat = category[0]
            prevday == catrandom
            n = random.randint(0, len(cat) - 1)
            meal = cat[n]
            print('Fisk: ' + str(meal))

        if catrandom == 'Kyckling':
            cat = category[1]
            prevday == catrandom
            n = random.randint(0, len(cat) - 1)
            meal = cat[n]
            print('Kyckling: ' + str(meal))

        if catrandom == 'kött':
            cat = category[2]
            prevday == catrandom
            n = random.randint(0, len(cat) - 1)
            meal = cat[n]
            print('Kött: ' + str(meal))

        if catrandom == 'vegetariskt':
            cat = category[3]
            prevday == catrandom
            n = random.randint(0, len(cat) - 1)
            meal = cat[n]
            print('Vegetarisk: ' + str(meal))


mainScreen()


