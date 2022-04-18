# product lists
product_names = ["soft drink", "onion rings", "small fries"]
product_units = [10, 5, 20]
product_costs = [0.99, 1.29, 1.49]

while True:
    command = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port, or (q)uit: ")
    if command == "q":
        print("See you soon!")
        break
    elif command == "l":
        prod_name_lens = []
        for p in product_names:
            prod_name_lens.append(len(p))
        prod_len = str(max(prod_name_lens) + 5)
        print(format("Product", "<" + prod_len + "s"), end ="")
        print(format("Price", "<8s"), end ="")
        print(format("Quantity", "<10s"), end ="")
        print()
        for i in range(len(product_names)):
            print(format(product_names[i], "<" + prod_len + "s"), end = "")
            print(format(product_costs[i], "<8.2f"), end = "") 
            print(format(product_units[i], "<10d"), end = "")
            print()
        print()
    elif command == "a":
        while True:
            name = input("Enter a new product name: ")
            if name in product_names:
                print("Sorry, we already sell that product. Try again.")
            else:
                product_names.append(name)
                while True:
                    cost = float(input("Enter a product cost: "))
                    if cost <= 0:
                        print("Invalid cost. Try again")
                        
                    else:
                        product_costs.append(cost)
                        while True:
                            quant = int(input("How many of these products do we have? "))
                            if quant <= 0:
                                print("Invalid quantity. Try again.")
                            else:
                                product_units.append(quant)
                                print("Product added!")
                                print()
                                break
                        break
                break
    elif command == "r":
        name = input("Enter a product name: ")
        if name in product_names:
            index = product_names.index(name)
            del product_names[index]
            del product_units[index]
            del product_costs[index]
            print("Product removed!")
            print()
        else:
            print("Product doesn't exist. Can't remove.")
            print()
    elif command == "s":
        product = input("Enter a product name: ")
        if product in product_names:
            price = product_costs[product_names.index(product)]
            quantity = product_units[product_names.index(product)]
            print('We sell "' + product + '" at', price, "per unit")
            print("We currently have", quantity, "in stock")
            print()
        else:
            print("Sorry, we don't sell \"" + product + '"')
            print()
    elif command == "u":
        name = input("Enter a product name: ")
        if name in product_names:
            print("What would you like to update?")
            index = product_names.index(name)
            command = input("(n)ame, (c)ost or (q)uantity: ")
            if command == "n":
                while True:
                    new_name = input("Enter a new name: ")
                    if new_name in product_names:
                        print("Duplicate name!")
                    else:
                        print("Product name has been updated \n")
                        product_names[index] = new_name
                        break
            elif command == "c":
                 while True:
                    new_cost = float(input("Enter a new cost: "))
                    if new_cost <= 0:
                        print("Invalid cost!")
                    else:
                        print("Product cost has been updated \n")
                        product_costs[index] = new_cost
                        break
            elif command == "q":
                while True:
                    new_quant = int(input("Enter a new cost: "))
                    if new_quant <= 0:
                        print("Invalid quantity!")
                    else:
                        print("Product quantity has been updated \n")
                        product_units[index] = new_quant
                        break
            else:
                print("Invalid option \n")
                
                        
        else:
            print("Product doesn't exist. Can't update.")
            print()
    elif command == "e":
        most = max(product_costs)
        most_index = product_costs.index(most)
        most_name = "(" + product_names[most_index] + ")"
        least = min(product_costs)
        least_index = product_costs.index(least)
        least_name = "(" + product_names[least_index] + ")"
        total = round(sum(product_costs), 2)
        print("Most expensive product: \t", most, most_name)
        print("Least expensive product: \t", least, least_name)
        print("Total value of all products: \t", total)
        print()
    else:
        print("Invalid option, try again.")
        print()
