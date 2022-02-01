#Programming Challenge: Coins

# ask user for number of pennies, nickels, dimes, and quarters

pennies = float(input("Number of pennies: "))
nickels = float(input("Number of nickels: "))
dimes = float(input("Number of dimes: "))
quarters = float(input("Number of quarters: "))

# calculate total amout of money
money_total = 0.01 * pennies + 0.05 * nickels + 0.10 * dimes + 0.25 * quarters

print("Total value of money:", format(money_total, '.2f'))

