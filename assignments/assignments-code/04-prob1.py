



num1_valid = False
num2_valid = False

while num1_valid == False:
    num1 = int(input("Number 1: "))
    if num1 <= 0:
        print("Invalid, try again")
    else:
        num1_valid = True
        while num2_valid == False:
            num2 = int(input("Number 2: "))
            if num2 <= 0:
                print("Invalid, try again")
            else:
                num2_valid = True

lower = num1

while num1 <= num2:
    print(num1, "*" * num1)
    num1 += 1

num1 -= 2

while num1 >= lower:
    print(num1, "*" * num1)
    num1 -= 1
