students = 0
tests = 0
total_average = 0

while True:
    students = int(input("How many students are in your class? "))
    if students <= 0:
        print("Invalid # of students, try again.")
    else:
        break
    
while True:
    tests = int(input("How many tests are in your class? "))
    if tests <= 0:
        print("Invalid # of tests, try again.")
    else:
        break

print("\nHere we go!")

for s in range (1, students + 1):
    print("\n****", "****", sep=" Student #" + str(s) + " ")
    test_total = 0
    for t in range(1, tests + 1):
        while True:
            score = int(input("Enter score for test #" + str(t) + ": "))
            if score < 0:
                print("Invalid score, try again")
            else:
                test_total += score
                break
    s_average = test_total/2.0
    print("Average score for student #" + str(s), "is", format(s_average, ".2f"))
    total_average += s_average

print()
print("Average score for all students is:", format(total_average/students, ".2f"))
    
            
