
# get user input YYYYMMDD format
date = int(input('Enter a date in YYYYMMDD format (i.e. 20220101 for January 1st, 2022): '))
day = date % 100
month = (date//100) % 100
valid = True

# check month validity
if month > 12 or month < 0:
    print("That's not a valid date!")
else:
# check day validity 
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        if day > 31:
            print("That's not a valid date!")
            valid = False
    elif month==4 or month==6 or month==9 or month==11:
        if day > 30:
            print("That's not a valid date!")
            valid = False
    else:
        if day > 28:
            print("That's not a valid date!")
            valid = False

#Checks that the date is within the semester
if valid:
    if date < 20220124:
        print('This date is before the semester begins.')
        valid = False
    elif date > 20220509:
        print('This date is after the semester ends.')
        valid = False


#Checks if the date is a class day or not
# Classes on Jan 24 26 31, Feb 2 7 9 14 16 21 28, Mar 2 7 9 21 23 28 30, Apr 4 6 11 13 18 20 25, May 2 4 9

if valid:
    if month == 1:
        if day==24 or day==26 or day==31:
            print('You have class today.')
        else:
            print('You do not have class today.')
    if month == 2:
        if day==2 or day==7 or day==9 or day==14 or day==16 or day==21 or day==28:
            print('You have class today.')
        else:
            print('You do not have class today.')
    if month == 3:
        if day==2 or day==7 or day==9 or day==21 or day==23 or day==28 or day==30:
            print('You have class today.')
        else:
            print('You do not have class today.')
    if month == 4:
        if day==4 or day==6 or day==11 or day==13 or day==18 or day==20 or day==25:
            print('You have class today.')
        else:
            print('You do not have class today.')
    if month == 5:
        if day == 2 or day == 4 or day == 9:
            print("You have class today.")
        else:
            print("You do not have class today.")








    
