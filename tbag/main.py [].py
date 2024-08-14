import os
# This code represents the introduction to the game
run = True
menu = True
play = False
rules = False

# Health and attack of player
HP = 50
ATK = 3

def clear():
    os.system("cls")


# This function will create a list containing the stats of the player
def save():
    list = [
        name,
        str(HP),
        str(ATK)
    ]
    # Open load.txt file in write mode that's in the directory of the game
    txt = open("load.txt", "w")
    for item in list:
        txt.write(item + "\n")
    txt.close()


while run:
    while menu:
        print("1, ˚୨୧⋆NEW GAME")
        print("2, LOAD GAME")
        print("3, RULES")
        print("4, ˚୨୧⋆QUIT GAME")

        if rules:
            print("Hi there traveller! feeling lost? not to worry, here are the rules")
            rules = False
            choice = ""
            input("> ")

        else:
            choice = input("# ")

        if choice == "1":
            name = input("Hi Traveller! what's your name?")
            menu = False
            play = True

        elif choice == "2":
            f = open("load.txt", "r")
            load_list = f.readlines()
            name = load_list[0][:-1]
            HP = load_list[1][:-1]
            ATK = load_list[2][:-1]
            print("Welcome back, " + name + "!")
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()

    while play:
        save()  # Auto save

        loc = input("# ")

        if loc == "0":
            play = False
            menu = True
            save()
