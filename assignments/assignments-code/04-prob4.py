while True:
    decimal_og = int(input("Enter a number greater than or equal to 0: "))
    if decimal_og < 0:
        print("Invalid, try again")
    else:
        break

binary = ""
decimal = decimal_og

while decimal > 0:
    remainder = decimal % 2
    binary = str(remainder) + binary
    print(decimal, "% 2", "=", remainder, "---", binary)
    print(decimal, "/ 2", "= ", end="")
    decimal = decimal // 2
    print(decimal)

if decimal == 0:
    binary = "0"
print(decimal_og, "in binary is", binary)
