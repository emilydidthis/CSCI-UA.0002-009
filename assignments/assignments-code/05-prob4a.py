# validate user input 
while True:
    low = int(input("Lowest number: "))
    if low < 0:
        print("Lowest number must be 0 or greater")
    else:
        while True:
            high = int(input("Highest number: "))
            if high <= low:
                print("Highest number must be larger than lowest number!")
            else:
                break
        # character spacing is length of greatest sum plus two
        width = len(str(high+high)) + 2
        break
    
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
        print (format(x + y, ">" + str(width) + "d"), end=ending)

'''
# just print row heading
for y in range(low, high + 1):
    print(y)
'''
