# prints main menu options
def main_menu():
    print("Main Menu")

    print("1 - Find all prime numbers within a given range")
    print("2 - Find all perfect numbers within a given range")
    print("3 - Find all abundant numbers within a given range")
    print("4 - Chart all even, odd, prime, perfect and abundant numbers within a given range")
    print("5 - Quit")
    print()
    print()
    
'''
Even/Odd Functions
'''

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def is_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False
'''
Prime Functions
'''
# function: is_prime
def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
                break
        else:
            return True

# function that prints all prime numbers within a range
# takes starting value and ending value
def print_prime(start, end):
    for i in range(start, end+1):
        if is_prime(i):
            print(i)

'''
Perfect Functions
'''
def is_perfect(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    if total == num:
        return True
    else:
        return False
    
def print_perfect(start, end):
    for i in range(start, end+1):
        if is_perfect(i):
            print(i)
'''
Abundant Functions
'''

def is_abundant(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    if num < total:
        return True
    else:
        return False
def print_abundant(start, end):
    for i in range(start, end+1):
        if is_abundant(i):
            print(i)
'''
Print whole chart
'''
# returns an iterable of True or Falses to help me draw xs or blanks
def chart_checker(num):
    even = is_even(num)
    odd = is_odd(num)
    prime = is_prime(num)
    perfect = is_perfect(num)
    abundant = is_abundant(num)
    return even, odd, prime, perfect, abundant

def print_chart(start, end):
    width = 10
    formatting_info = "<" + str(width) + "s"
    print(format("Number", formatting_info), end="")
    print(format("Even", formatting_info), end="")
    print(format("Odd", formatting_info), end="")
    print(format("Prime", formatting_info), end="")
    print(format("Perfect", formatting_info), end="")
    print(format("Abundant", formatting_info), end="")
    print()
    for i in range(start, end+1):
        print(format(str(i), formatting_info), end="")
        for x in chart_checker(i):
            if x == True:
                print(format("x", formatting_info), end="")
            else:
                print(format(" ", formatting_info), end="")
        print()
    print()

'''
Print Range Function: directs to more specific functions
'''
def print_range(num):
    #ask for user inputs
    while True:
        input1 = int(input("Enter starting number (positive only): "))
        if input1 <= 0:
            print("Invalid, try again")
        else:
            break
    while True:
        input2 = int(input("Enter ending number (positive only): "))
        if input2 < input1:
            print("Invalid, try again")
        else:
            break
    # create string called category for customized print
    # call necessary print functions
    if num == 4:
        print_chart(input1, input2)
    else:
        if num == 1:
            category = "prime"
        elif num == 2:
            category = "perfect"
        elif num == 3:
            category = "abundant"
        #output
        print()
        print("All", category, "numbers between", input1, "and", input2)
        print("#" * 14)
        # calls function associated with specific category
        globals()["print_" + category](input1, input2) 
        print("#" * 14)
        print()

# user input validation
while True:
    main_menu()
    selection = input("Your choice: ")
    if selection in ["1", "2", "3", "4"]:
        # call a function 
        print_range(int(selection)) 
    elif selection == "5":
        print("Goodbye!")
        break
    else:
        print("I don't understand that...")
        print()
        print()
