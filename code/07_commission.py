# Calculate Commissions for a Sales Team

# set up loop with assumption / "control variable"
compute_comms = 'yes'

# initialize variables
num_employees = 0
total_sales = 0
avg_sales = 0
total_comm = 0

# start a loop
while compute_comms == 'yes':
    # get sales and commission rate for person
    sales = float(input("Input gross sales: "))
    comm_rate = float(input("Input commission rate: "))

    # calculate commission for person 
    comm = sales * comm_rate

    # output commission earned 
    print("You made", comm, "in commissions.")

    num_employees = num_employees + 1
    total_sales += sales
    avg_sales = total_sales / num_employees
    total_comm += comm

    #output
    print("Number of employees:", num_employees)
    print("Total sales:", total_sales)
    print("Average sales:", avg_sales)
    print("Total commission:", total_comm)

    # ask user if they want to continue
    compute_comms = input("Do you want to continue? Type yes or no: ")

    
print("Thank you for using our program.")

