name = input("Your Name: ")
age = int(input("Your Age: "))

if 31 > age > 17:
    print(f"Welcome Mr {name}.")
else:
    if age <= 17:
        print(f"Grow older Mr {name}.")
    else:
        print(f"Too old Mr {name}.")
