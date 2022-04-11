# Prob 2a


# Input
name = input("Name: ")

# Lowercase first
name = name.lower()

# Create a new string
cleaned_name = ""

# Only add characters that aren't digits, spaces, or special
for c in name:
    if c.isdigit():
        continue
    elif c == " ":
        continue
    elif not c.isalnum():
        continue
    else:
        cleaned_name += c

print("Your 'cleaned up' name is:", cleaned_name)
print("Your 'cleaned up' name reduces to:")

num_total = 0
length = len(cleaned_name)
counter = 0

for c in cleaned_name: 
    number = ord(c) - 96 # a is 97 so subtract 96
    num_total += number
    if counter == length - 1:
        print(number, end = " ")
    else:
        print(number, "+", end= " ")
    counter += 1
print("=", num_total)

# add up numbers places of a number
while num_total > 9:
    num_as_string = str(num_total)
    new_num = 0
    for i in range(0, len(num_as_string)):
        new_num += int(num_as_string[i])

    num_total = new_num
    print("Further reduction:", num_total)

personalities = ["emptiness", "independence", "quiet", "charming", "harmony", "new directions", "love", "spirtuality", "organization", "romantic"]
print("This name means ...", personalities[int(num_total)])
    
