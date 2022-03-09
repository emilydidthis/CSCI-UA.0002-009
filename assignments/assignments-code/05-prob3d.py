# validate user inputs
while True:
    start = int(input("Start number: "))
    end = int(input("End number: "))
    if start < 0 or end < 0:
        print("Start and end must be positive")
    elif end <= start:
        print("End number must be greater than start number")
    else:
        width = len(str(end)) + 2
        break

row_counter = 1
for i in range(start, end + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        if i == 1:
            continue
        format_string = ">" + str(width) + "d"
        output = format(i, format_string)
        if row_counter % 10 == 0:
            print(output)
        else:
            print(output, end="")
        row_counter += 1
    

    
