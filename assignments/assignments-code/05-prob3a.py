while True:
    num = int(input("Enter a positive number to test: "))
    if num <= 0:
        print("Number must be positive, try again.")
    else:
        break
    
print()
if num == 1:
    print("1 is not a prime number")
elif num == 2:
    print("2 is a prime number!")
elif num == 3:
    print("3 is a prime number!")
else:
    divisor = 2
    while divisor < num:
        if num % divisor != 0:
            print(str(divisor), "is NOT a divisor of", str(num), "... continuing")
            divisor += 1
        else:
            print(str(divisor), "is a divisor of", str(num), "... stopping")
            print()
            print(str(num), "is not a prime number.")
            break
        if divisor == num:
            print()
            print(str(num), "is a prime number!")

'''
else:
    for i in range(2, num):
        if num % i != 0:
            print(str(i), "is NOT a divisor of", str(num), "... continuing")
        else:
            print(str(i), "is a divisor of", str(num), "... stopping")
            print()
            print(str(num), "is not a prime number.")
            break
        if i == num - 1:
            print()
            print(str(num), "is a prime number!")
'''
