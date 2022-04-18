'''
username = input("Enter a username: ")
password = input("Enter a password: ")

file = open("security.txt", "w")

file.write(username + '\n')
file.write(password + '\n')

file.close()

'''

file = open("security.txt", "r")

data = file.read().split("\n")
#print(data)

username = data[0]
password = data[1]

u_input = input("Enter a username: ")
p_input = input("Enter a password: ")

if u_input == username:
    if p_input == password:
        print("Welcome!")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")
