# Programming Challenge: Time Calculations

# ask user to input number of seconds as whole number
seconds = int(input("Enter seconds: "))

# output combination of minutes and seconds
minutes = seconds // 60
secs_remain = seconds % 60

print(minutes)
print(secs_remain)
print("That's", minutes, "minutes and", secs_remain, "seconds")

# print("That's " + str(minutes) + " minutes and " + str(secs_remain) + " seconds")


