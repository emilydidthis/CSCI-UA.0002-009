end = 20
for i in range(1, end + 1):
    if i == 1:
        print("1 is technically not a prime number.")
    elif i == 2:
        print("2 is a prime number!")
    else:
        counter = 2
        #For Loop
        for j in range(2, i):
            if i % j != 0:
                counter += 1
            else:
                break
            if counter == i:
                print(str(i), "is a prime number!")
                
'''
    # While Loop
    else:
        divisor = 2
        while divisor < i:
            if i % divisor != 0:
                divisor += 1
            else:
                break
            if divisor == i:
                print(str(i), "is a prime number!")
            
'''
    
