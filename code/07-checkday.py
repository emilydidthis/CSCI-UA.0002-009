# ask user for input
num = int(input("Pick a number between 1 and 7: "))

# check to see if number is valid
if num > 0 and num <= 7:
    if num == 1:
        weekday = "Sunday"
    elif num == 2:
        weekday = "Monday"
    elif num == 3:
        weekday = "Tuesday"
    elif num == 4:
        weekday = "Wednesday"
    elif num == 5:
        weekday = "Thursday"
    elif num == 6:
        weekday = "Friday"
    else:
        weekday = "Saturday"
    print("You selected", weekday)
else:
    print("The number you entered was not valid.")
    

    

