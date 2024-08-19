# This code represents the introduction to the game
run = True
menu = True
play = False
rules = False
key = False

# Health and attack of player
HP = 50
ATK = 3
x = 0
y = 0

# Create the map
map =


# This function will create a list containing the stats of the player
def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(x),
        str(y),
        str(key)
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
            print("Hi there traveller! feeling lost? not to worry, the rules are quite simple")
            print("1: Cook, 2: Please your customer: i'm sure you'll figure it out in no time")
            rules = False
            choice = ""
            input("> ")

        else:
            choice = input("# ")

        if choice == "1":

            elif choice == "2":
            f = open("load.txt", "r")
            load_list = f.readlines()
            if len(load_list) == 6:
                name = int(load_list[0][:-1])
                HP = int(load_list[1][:-1])
                ATK = int(load_list[2][:-1])
                x = int(load_list[3][:-1])
                y = int(load_list[4][:-1])
                key = bool(load_list[5][:-1])
            else:
                print("Corrupt save file!")
                input("> ")
            q = input("Hi Traveller! what's your name?")
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
