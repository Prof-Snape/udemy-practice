a = "a"

while a != "0":
    if a not in "1, 2, 3, 4":
        print("Chose a number between 1 to 4: ")
        print("1:\tOption 1")
        print("2:\tOption 2")
        print("3:\tOption 3")
        print("4:\tOption 4")
        print("0:\tQuit")
    else:
        print("You chose {}.".format(a))

    a = input()

print("You Quit.")
