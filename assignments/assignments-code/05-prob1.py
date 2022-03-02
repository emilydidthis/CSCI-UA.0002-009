budget = int(input("Enter budget for your party: "))
cost_per_slice = float(input("Cost per slice of pizza: "))
cost_per_pie = float(input("Cost per whole pie (8 slices): "))
attendees = int(input("How many people will be attending your party? "))
total_slices = 0
for p in range(1, attendees + 1):
    while True:
        slices = int(input("Enter number of slices for person #" + str(p)+": "))
        if slices < 1:
            print("Not a valid entry, try again!")
        else:
            total_slices += slices
            break

pies_result = total_slices // 8
slices_result = total_slices % 8
cost_result = pies_result * cost_per_pie + slices_result * cost_per_slice
change = budget - cost_result

if change < 0:
    print("Your order cannot be completed.")
    print("You would need to purchase", pies_result, "pies and", slices_result, "slices")
    print("This would put you over budget by", format(change*-1, ".2f"))
else:
    print("You should purchase", pies_result, "pies and", slices_result, "slices")
    print("Your total cost will be:", format(cost_result, ".2f"))
    if change == 0:
        print("You will have no money left after your order")
    else:
        print("You will still have", format(change, ".2f"), "left after your order")
        
