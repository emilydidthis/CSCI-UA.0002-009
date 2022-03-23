# function:   is_even 
# input:      a positive integer 
# processing: determines if the supplied number is even 
# output:     boolean

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# function:   is_odd
# input:      a positive integer
# processing: determines if the supplied number is odd
# output:     boolean

def is_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False
    
# function:   is_prime
# input:      a positive integer
# processing: determines if the supplied number is prime 
# output:     boolean

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

# function:   is_perfect
# input:      a positive integer
# processing: determines if the supplied number is perfect. a perfect number
#             is a number that is equal to the sum of its factors (i.e. the
#             number 6 is perfect because 6 = 1 + 2 + 3)
# output:     boolean

def is_perfect(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    if total == num:
        return True
    else:
        return False

# function:   is_abundant
# input:      a positive integer
# processing: determines if the supplied number is abundant. an abundant number
#             is a number that is less than the sum of its factors (i.e. the
#             number 12 is abundant because 12 < 1 + 2 + 3 + 4 + 6)
# output:     boolean

def is_abundant(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    if num < total:
        return True
    else:
        return False


# Analyze numbers within a range

# user input, both positive, second must be greater than first
while True:
    num1 = int(input("Enter starting number: "))
    if num1 < 0:
        print("Invalid, number must be positive")
    else:
        break
while True:
    num2 = int(input("Enter ending number: "))
    if num2 <= num1:
        print("Invalid, ending number must be greater than starting number")
    else:
        break

# run through the range of numbers
for i in range(num1, num2 + 1):
    print(i, "is", "...", end=" ")
    if is_even(i):
        print("even", end=" ")
    if is_odd(i):
        print("odd", end=" ")
    if is_prime(i):
        print("prime", end=" ")
    if is_abundant(i):
        print("abundant", end=" ")
    if is_perfect(i):
        print("perfect", end=" ")
    print()
        
'''
a1 = is_even(5)
a2 = is_even(6)
print (a1, a2) # False True

b1 = is_odd(5)
b2 = is_odd(6)
print (b1, b2) # True False

c1 = is_prime(5)
c2 = is_prime(17)
c3 = is_prime(21)
print (c1,c2,c3) # True True False

d1 = is_perfect(6)
d2 = is_perfect(7)
d3 = is_perfect(10)
print (d1,d2,d3) # True False False

e1 = is_abundant(12)
e2 = is_abundant(13)
e3 = is_abundant(14)
print (e1,e2,e3) # True False False
'''
