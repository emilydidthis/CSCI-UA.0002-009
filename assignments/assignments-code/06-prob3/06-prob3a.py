import digitalclock
import random

while True:
    count = int(input("How many problems would you like to attempt? "))
    if count < 0:
        print("Invalid number, try again")
    else:
        while True:
            width = int(input("How wide do you want your digits to be? 5-10: "))
            if width < 5 or width > 10:
                print("Invalid number, try again")
            else:
                while True:
                    char = input("What character would you like to use? " )
                    if len(char) > 1:
                        print("String too long, try again")
                    else:
                        break
                break
        break

print("\nHere we go!\n")
i = 0
correct = 0
while i< count:
    print("What is .....")
    print()
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    operator = random.randint(0, 1)
    #print(operator)
    digitalclock.print_number(num1, width, char)

    if operator == 0:
        print(digitalclock.plus(width, char))
        operator = "+"
        #print(operator)
    else:
        print(digitalclock.minus(width, char))
        operator = "-"
        #print(operator)

    digitalclock.print_number(num2, width, char)

    answer = int(input("= "))
    if digitalclock.check_answer(num1, num2, answer, operator):
        print("Correct!")
        correct += 1
    else:
        print("Sorry, that's not correct.")
    print()
    i += 1

    
print("\nYou got", correct, "out of", count, "correct!")
