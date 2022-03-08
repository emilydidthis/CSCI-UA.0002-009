while True:
    start = int(input("Start number: "))
    end = int(input("End number: "))
    if start < 0 or end < 0:
        print("Start and end must be positive")
    elif end <= start:
        print("End number must be greater than start number")
    else:
        break

if start < 3:
    print(2)
for i in range(start, end + 1):
    counter = 2
    for j in range(2, i):
        if i % j != 0:
            counter += 1
        else:
            break
        if counter == i:
            print(i)
            

    
