computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi cable"]
chosen_parts = []
choice = "100"

while choice != 0:
    if choice in range(1, len(computer_parts) + 1):
        print("Adding ", choice)
        chosen_parts.append(computer_parts[choice - 1])

    if choice not in range(1, len(computer_parts) + 1):
        print("Please add options from the list: ")
        for a in range(len(computer_parts)):
            print(a + 1, end=": ")
            print(computer_parts[a])
        print("0: to finish")

    choice = input()
    if choice.isnumeric():
        choice = int(choice)

print(chosen_parts)
