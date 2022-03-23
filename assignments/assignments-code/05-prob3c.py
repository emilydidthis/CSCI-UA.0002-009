while True:
    start = int(input("Start number: "))
    end = int(input("End number: "))
    if start < 0 or end < 0:
        print("Start and end must be positive")
    elif end <= start:
        print("End number must be greater than start number")
    else:
        break

for i in range(start, end + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
    

    
