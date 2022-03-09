# validate user input 
while True:
    low = int(input("Lowest number: "))
    if low < 0:
        print("Lowest number must be 0 or greater")
    else:
        break
while True:
    high = int(input("Highest number: "))
    if high <= low:
        print("Highest number must be larger than lowest number!")
    else:
        # character spacing is length of greatest sum plus two
        width = len(str(high+high)) + 2
        break
    
    
# *** ask user if they want to identify Prime
while True:
    answer = str(input("Would you like to identify Prime numbers in your table? (y/n): "))
    if answer == "y":
        checkPrime =  True
        break
    elif answer == "n":check
        checkPrime = False
        break
    else:
        print("Invalid command, try again")
    
# print operation symbol centered
print(format("+", "^" + str(width) + "s"), end="")

# print column headings 
for x in range(low, high + 1):
    print(format(x, ">" + str(width) + "d"), end ="")

# print line break
print()
print("-" * width * (high-low+2)) # add two, one for extra number, one for operator


for x in range(low, high + 1):
    # print the row heading
    print(format(x, "<" + str(width-1) + "d"), end="")
    print("|", end="")
    for y in range(low, high + 1):
        # create a new line at the end of the row
        if y == high:
            ending = "\n"
        else:
            ending = ""
            
        # *** check if prime
        sumxy = x + y
        isPrime = False
        for i in range(2, sumxy):
            if sumxy % i == 0:
                break
        else:
            isPrime = True
        if isPrime and sumxy != 0 and sumxy != 1:
            output = str(sumxy) + "p"
        else:
            output = str(sumxy)
        print (format(output, ">" + str(width) + "s"), end=ending)

'''
# just print row heading
for y in range(low, high + 1):
    print(y)
'''
