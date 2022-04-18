'''
file = open("multiple-choice.txt", "w")

while True:
    question = input("Enter a question: ")
    file.write(question + "\n")
    answer = input("Enter an answer: ")
    file.write(answer + "\n")
    cont = input("Would you like to enter another question? (y/n): ")
    if cont == "n":
        break
    else: continue

file.close()
'''

file = open("multiple-choice.txt", "r")
data = file.read().split("\n")
print(data)

questions = data[:-1:2]
answers = data[1::2]

##print(questions)
##print(answers)

score = 0
for i in range(len(questions)):
    print(questions[i])
    answer = input()
    if answer == answers[i]:
        print("correct")
        score += 1
    else:
        print("wrong")

print("final score:", score)
print("average score:", score/len(questions))
