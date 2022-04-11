# Part 1a + 1b

# username validation program
while True:
    true_count = 0
    username = input("Enter a username: ")

    # check length
    length = len(username)
    if length > 7 and length < 16:
        true_count += 1
    print("* Length of username:", length)
    
    #check alpha-numeric
    if username.isalnum():
        true_count += 1
    print("* All characters are alpha-numberic:", username.isalnum())

    #check first and last
    first = username[0]
    last = username[length-1]
    if first.isdigit() or last.isdigit():
        first_last = False
    else:
        first_last = True
        true_count += 1
    print("* First & last characters are not digits:", first_last)    

    # uppercase, lowercase, # of digits
    upper = 0
    lower = 0
    digits = 0
    for c in username:
        if c.isupper():
            upper += 1
        if c.islower():
            lower += 1
        if c.isdigit():
            digits += 1
    if upper > 0:
        true_count += 1
    if lower > 0:
        true_count += 1
    if digits > 0:
        true_count += 1
        
    print("* # of uppercase characters in username:", upper)
    print("* # of lowercase characters in username:", lower)
    print("* # of digits characters in username:", digits)
    
    # break out of the loop
    if true_count == 6:
        print("Username is valid!")
        print()
        break
    else:
        print("Username is invalid, please try again")
        print()
        
# password validation program

while True:
    true_count = 0
    password = input("Enter a password: ")

    #at least 8 chars long
    length = len(password)
    if length > 7:
        true_count += 1
    print("* Length of password:", length)

    #cannot contain username
    if username not in password:
        true_count += 1
        userInPass = False
    else:
        userInPass = True
    print("* Username is part of password", userInPass)
    
    #must contain at least (1) upper, lower, digits, and special
    upper = 0
    lower = 0
    digits = 0
    special = 0
    for c in password:
        if c.isupper():
            upper += 1
        if c.islower():
            lower += 1
        if c.isdigit():
            digits += 1
        if not c.isalnum():
            special += 1
    if upper > 0:
        true_count += 1
    if lower > 0:
        true_count += 1
    if digits > 0:
        true_count += 1
    if special > 0:
        true_count += 1
    print("* # of uppercase characters in password:", upper)
    print("* # of lowercase characters in password:", lower)
    print("* # of digits characters in password:", digits)
    print("* # of special characters in password:", special)

     # break out of the loop
    if true_count == 6:
        print("Password is valid!")
        break
    else:
        print("Password is invalid, please try again")
        print()
