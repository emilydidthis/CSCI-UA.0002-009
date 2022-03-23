# inputs
width1 = int(input("Enter the width for Rectangle #1: "))
length1 = int(input("Enter the length for Rectangle #1: "))
width2 = int(input("Enter the width for Rectangle #2: "))
length2 = int(input("Enter the length for Rectangle #2: "))

# calculate areas
area1 = width1 * length1
area2 = width2 * length2

# outputs
print()
print("Rectangle #1 has an area of", area1)
print("Rectangle #2 has an area of", area2)

# determine if rectangle is square
if width1 == length1:
    print("Rectangle #1 is a square!")
if width2 == length2:
    print("Rectangle #2 is a square!")

# determine which rect is larger
print()
if area1 > area2:
    print("Rectangle #1 is larger than Rectangle #2")
elif area1 < area2:
    print("Rectangle #2 is larger than Rectangle #1")
else:
    print("The rectangles are equal!")
     
