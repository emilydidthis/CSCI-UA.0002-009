# ask user for inputs
x1 = float(input("Enter Point #1 - x position: "))
y1 = float(input("Enter Point #1 - y position: "))
x2 = float(input("Enter Point #2 - x position: "))
y2 = float(input("Enter Point #2 - y position: "))
x3 = float(input("Enter Point #3 - x position: "))
y3 = float(input("Enter Point #3 - y position: "))

# distances
side1raw = pow(pow(x1-x2, 2) + pow(y1-y2, 2), 0.5)
side1 = round(pow(pow(x1-x2, 2) + pow(y1-y2, 2), 0.5), 2)
side2 = round(pow(pow(x3-x1, 2) + pow(y3-y1, 2), 0.5), 2)
side3 = round(pow(pow(x2-x3, 2) + pow(y2-y3, 2), 0.5), 2)

# ouput
print(format(side1, ".2f"))
print(format(side2, ".2f"))
print(format(side3, ".2f"))

# check valid triangle
if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
    print("This is a valid triangle!")
else:
    print("This is not a valid triangle")


#check equilateral triangle
if side1 == side2 == side3:
    print("This is an equilateral triangle")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("This is an isosceles triangle")
else:
    print("This is a scalene triangle")

# EC: check if right triangle
if side1 > side2 and side1 > side3:
    c = side1
    a = side2
    b = side3
elif side2 > side1 and side2 > side3:
    c = side2
    a = side1
    b = side3
else:
    c = side3
    a = side1
    b = side2

if round(pow(a,2)) + round(pow(b,2)) == round(pow(c,2)):
    print("This is also a right triangle")
