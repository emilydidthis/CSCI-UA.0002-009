# function: valid date
# inputs: two integers (month and date)
# processing: checks to see if the date is valid
# output: returns True if date is valid and False if not

def valid_date(month, day):
    if month > 12 or month < 0:
        return False
    else:
        if month == 2:
            if day > 0 and day <= 28:
                return True
            else:
                return False
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            if day > 0 and day <= 31:
                return True
            else:
                return False
        else:
            if day > 0 and day <= 30:
                return True
            else:
                return False


print (valid_date(99,1)) # False
print (valid_date(1,99)) # False
print (valid_date(99,99)) # False

print (valid_date(-99,1)) # False
print (valid_date(1,-99)) # False
print (valid_date(-99,-99)) # False

print (valid_date(9,25)) #True
print (valid_date(10,15)) # True
print (valid_date(11,31)) # False
print (valid_date(2,28)) # True
print (valid_date(2,29)) # False
