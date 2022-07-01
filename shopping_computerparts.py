"""We have been presented with a list of computer parts from which we need to make a user select what he/she wants to
purchase. The list may get edited in future as per inventory, so we need to design our code in such a way that it can
handle such changes as and when it happens.
        Capitalizing available items for better appearance with acceptance to acronyms such as HDMI.
        Further, added the ability to check if an item is already in cart before adding to avoid duplication.
        If the user selects any item again he/she presented with the option to remove it from the cart.
        Added the ability for the user to clear cart or view cart and remove any item from the cart.
        Added comments in code for better understanding.
"""

computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "HDMI cable"]
cart = []
click_count = 0
# Initializing choice to anything other than num 0.
choice = "100"
exit_choice = "100"

# Changing available computer parts in capitalized word for better appearance.
for i in range(len(computer_parts)):
    a = computer_parts[0]
    b = ""
    # Working at the first element of the list because we will be adding the formatted text in last position and
    # deleting the first element after adding its formatted version to the list.
    for j in range(len(a)):
        if j == 0:
            b += a[j].capitalize()
            # Capitalizing first character of the word.
        elif a[j].isupper():
            b += a[j]
            # Accepting acronyms as it is, i.e. HDMI.
        elif a[j] == " ":
            b += a[j]
            # Taking whitespace as it is.
        elif a[j - 1] == " ":
            b += a[j].capitalize()
            # Capitalizing first character after whitespace, i.e. first character of second word.
        else:
            b += a[j]
    computer_parts.append(b)
    # Adding formatted text at last position in the list.
    computer_parts.remove(a)
    # Removing first element from the list which was just formatted.
computer_parts.sort()

while exit_choice != 0:
    # Since num 0 is the option for ending shopping.
    print("Please select any option from the list:")
    for a in range(len(computer_parts)):
        print(a + 1, end=": {}.\n".format(computer_parts[a]))
    print(len(computer_parts) + 1, end=": View Cart.\n")
    print(len(computer_parts) + 2, end=": Clear Cart.\n")
    print("0: I am done with my shopping.\nYour Choice: ", end="")
    # All correct options will keep getting printed until user get done with shopping or entered any special mode
    # i.e. cart review mode.

    choice = input()
    click_count += 1
    if choice.isnumeric():
        choice = int(choice)

    if choice in range(1, len(computer_parts) + 1):
        # Checking if user have selected valid option for any item.
        if computer_parts[choice - 1] not in cart:
            # Checking if selected item is not already in cart then adding it to the cart.
            print("Adding {} to your cart.".format((computer_parts[choice - 1])))
            cart.append(computer_parts[choice - 1])
        else:
            # If selected item is already present in cart, presenting user option to remove the same item from
            # his/her cart.
            print("{0} is already in your cart. Do you want to remove {0} from your cart?\nEnter Y/y to remove:"
                  .format(computer_parts[choice - 1]), end=" ")
            remove_choice = input()
            click_count += 1
            if remove_choice == "Y" or remove_choice == "y":
                # Checking if the user choose to remove that item.
                print("Removing {} from your cart.".format(computer_parts[choice - 1]))
                cart.remove(computer_parts[choice - 1])
            else:
                # If user choose not to remove or any incorrect option then complete shopping list will be printed
                # again for the user.
                print("Incorrect option.")
                choice = remove_choice
    elif choice == len(computer_parts) + 1:
        # If user selects to view his cart, his/her cart will be displayed and if the cart is empty a sorry message
        # will be displayed stating the same.
        if len(cart) < 1:
            print("Your cart is currently empty.\n\tLet`s first add something to the cart.")
        else:
            cart.sort()
            print("You cart currently contains: ", end="")
            if len(cart) == 1:
                print(cart[0], end=".\n")
            else:
                for j in cart:
                    if j == cart[-1]:
                        print("and", j, end=".\n")
                    elif j == cart[-2]:
                        print(j, end=" ")
                    else:
                        print(j, end=", ")
            print("If you want to remove something from your cart reply with Y/y or reply with anything else for the "
                  "shopping mode.")
            # Presenting user option to remove any item from his/her cart.
            remove_choice = input()
            click_count += 1
            if remove_choice == "Y" or remove_choice == "y":
                # If user selects to remove something from his/her cart. He/She will be presented with the option to
                # select which item to remove.
                while remove_choice != 0:
                    # Since num 0 will be presented as an option to go back to the shopping mode.
                    if len(cart) == 0:
                        # When user deleted all items from the cart he/she will be presented with the shopping mode
                        # again.
                        print("Your cart is empty. Returning to the shopping mode.")
                        remove_choice = 0
                    else:
                        cart.sort()
                        print("Reply with corresponding option for removing item from your cart.")
                        for a in range(len(cart)):
                            print(a + 1, end=": {}.\n".format(cart[a]))
                        print("0: Done reviewing the cart.\nYour choice: ")
                        remove_choice = input()
                        click_count += 1
                        if remove_choice.isnumeric():
                            remove_choice = int(remove_choice)
                            if remove_choice in range(1, len(cart) + 1):
                                # If user selects an available option the corresponding item will be removed from the
                                # cart.
                                print("Removing {} from your cart.".format(cart[remove_choice - 1]))
                                cart.remove(cart[remove_choice - 1])
                            elif remove_choice == 0:
                                # If user choose to go back to the shopping mode.
                                print("Moving to the shopping mode.")
                        else:
                            # If user gave an incorrect option then complete shopping list will be printed again for the
                            # user.
                            print("Incorrect option. Moving to the shopping mode.")
                            remove_choice = 0
            else:
                # If user gave an incorrect option then the user will be moved to the shopping mode.
                print("Moving to the shopping mode.")
    elif choice == len(computer_parts) + 2:
        # If user selects to clear his cart, his/her cart will be emptied.
        if len(cart) == 0:
            # If cart is empty, printing similar message.
            print("Your cart is already empty.\n\tLet`s first add something to the cart.")
        else:
            print("Clearing your cart.")
            cart = []
            print("Your cart is now empty.\n\tLet`s get back to shopping.")
    elif choice == 0:
        # When user choose to end shopping, checking cart and if empty presenting user an option to return to shopping.
        if len(cart) > 0:
            exit_choice = 0
        else:
            print("Your cart looks empty. Want to look at the available option?\nPress any key to return to the "
                  "shopping.\nPress 0 again to exit.")
            exit_choice = input("Your Choice: ")
            click_count += 1
            if exit_choice == "0":
                print("Sorry to see you go empty hand.")
                exit_choice = 0
    elif click_count != 0:
        print("Incorrect option.")
        # Will print only once user has put any incorrect option. Note: Variable run_count initially has been set to
        # num 0. It increments everytime user enter any input. Can also be used to track number of user clicks.

if len(cart) > 0:
    cart.sort()
    print("You cart contains: ", end="")
    if len(cart) == 1:
        print(cart[0], end=".\n")
    else:
        for j in cart:
            if j == cart[-1]:
                print("and", j, end=".\n")
            elif j == cart[-2]:
                print(j, end=" ")
            else:
                print(j, end=", ")
