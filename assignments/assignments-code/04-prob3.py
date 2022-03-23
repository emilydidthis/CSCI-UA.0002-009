
while True:
    sticks = int(input("How many sticks (10-100)? "))
    if sticks < 10:
        print("Sorry, that's too few sticks. Try again.")
    elif sticks > 100:
        print("Sorry, that's too many sticks. Try again.")
    else:
        print("Great, let's play.\n")
        break

turn = 1
while sticks > 0:
    if (turn % 2 == 0):
        print("Turn: Player 2")
    else:
        print("Turn: Player 1")
    print("There are", sticks, "on the table.")
    while True:
        num = int(input("How many sticks do you want to take? (1, 2, or 3)? "))
        if (num != 1 and num != 2 and num != 3) or num > sticks:
            print("Sorry, that's not a valid number.")
        else:
            break
    sticks -= num
    turn += 1
    print()

print("There are no sticks left on the table! Game over.")
if (turn % 2 == 0):
    print("Player 2 wins!")
else:
    print("Player 1 wins!")
