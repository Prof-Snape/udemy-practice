import random

highest_number = 100
answer = random.randint(1, highest_number)
print(answer)

print("Guess a number between 1 and {}: ".format(highest_number))
guess = int(input())
no_of_guess = 1

while guess != answer and guess != 0:
    if guess < answer:
        print("Guess higher: ", end="")
    else:
        print("Guess lower: ", end="")
    no_of_guess += 1
    guess = int(input())

if guess == 0:
    print("You Quit.")
else:
    print("You guessed it right. You took", no_of_guess, "guess.")
