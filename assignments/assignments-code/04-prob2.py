import random

snake_eyes = False
sides = 0

# ask user for dice side input

while True:
    sides = int(input("How many sides on your dice (4, 6, 8, 10, 12, or 20)? "))
    if sides != 4 and sides != 6 and sides != 8 and sides != 10 and sides != 12 and sides != 20:
        print("Invalid size, try again.")
    else:
        print("\nThanks, here we go!\n")

        break
                     
# tracking variables
roll_count = 1
doubles = 0
high = 0
high_low = 0
evens = 0
odds = 0
sums = 0
die_1_total = 0
die_2_total = 0

while snake_eyes == False:

    # roll the dice
    die_1 = random.randint(1, sides)
    die_2 = random.randint(1, sides)
    die_1_total += die_1
    die_2_total += die_2
    
    # check for special conditions
    message = ""
    if die_1 == die_2:
        message += "Doubles!" + " "
        doubles += 1
    if die_1 == sides and die_2 == sides:
        message += "High!" + " "
        high += 1
    if (die_1 == 1 and die_2 == sides) or (die_1 == sides and die_2 == 1):
        message += "High/Low!" + " "
        high_low +=1
    if die_1 % 2 == 0 and die_2 % 2 == 0:
        message += "Evens!" + " "
        evens += 1
    if die_1 % 2 == 1 and die_2 % 2 == 1:
        message += "Odds!" + " "
        odds += 1
    if die_1 + die_2 == sides:
        message += "Sum value is size value!" + " "


    roll_count += 1
    
    # exit the loop
    if die_1 == 1 and die_2 == 1:
        message += "Snake Eyes!" 
        snake_eyes = True
        
    # output
    print(str(roll_count) + ".", "die #1 is", "*" + str(die_1) + "*", "and die #2 is", "*" + str(die_2) + "*", message)

along = "Along the way you rolled"
doubles_percent = format(doubles/roll_count, ".2%")
highs_percent = format(high/roll_count, ".2%")
evens_perecent = format(evens/roll_count, ".2%")
odds_perecent = format(odds/roll_count, ".2%")
high_low_percent = format(high_low/roll_count, ".2%")
sums_percent = format(sums/roll_count, ".2%")
average1 = round(die_1_total/roll_count, 2)
average2 = round(die_2_total/roll_count, 2)

print("\nYou finally got snake eyes on roll #" + str(roll_count))
print(along, "DOUBLES", doubles, "times.", "(" + doubles_percent + " of all rolls were doubles)")
print("Average roll for die #1:", average1)
print("Average roll for die #2:", average2)
