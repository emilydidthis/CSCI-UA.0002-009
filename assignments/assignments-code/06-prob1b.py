# function: maximum
# input: two integers
# processing: calculates which integer is larger
# output: returns the larger number

def maximum(num1, num2):
    if num1 > num2:
        return num1
    elif num1 == num2:
        return num2
    else:
        return num2

# function: minimum
# input: two integers
# processing: calculates which integer is smaller
# output: returns the smaller number

def minimum(num1, num2):
    if num1 < num2:
        return num1
    elif num1 == num2:
        return num2
    else:
        return num2


a = 5
b = 10
c = 15
d = 20

ans1 = maximum(a,b)
ans2 = maximum(a,c)
ans3 = maximum(a,d)
print (ans1,ans2,ans3) # 10 15 20

ans4 = minimum(d,c)
ans5 = minimum(d,b)
ans6 = minimum(d,a)
print (ans4,ans5,ans6) # 15 10 5

ans7 = maximum( maximum(a,b), maximum(c,d) )
print ("The biggest is:", ans7)
