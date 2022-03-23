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
            if num2 <= num1:
                print("Invalid, try again")
            else:
                num2_valid = True

iterator = num1

while iterator <= num2:
    print(iterator, "*" * iterator)
    iterator += 1

iterator = num2

while iterator >= num1:
    iterator -= 1
    print(iterator, "*" * iterator)
    
