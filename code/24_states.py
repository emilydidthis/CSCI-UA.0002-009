import urllib.request

try:
    # define url
    url = "http://002-009-text-files.glitch.me/states.txt"

    # initial request to URL
    response = urllib.request.urlopen(url)

    # read data from URL as string
    data = response.read().decode("utf-8")
except:
    print("Couldn't get data")
else:
    print("Data found")
    print(data)


data = data.split("\n")

states = {}

for s in data:
    pair = s.split(", ")
    states[pair[1]] = pair[0]

# print(states)

import random

# start game
print("How good is your knowledge of state capitals?")
lives = 3

# make a list of states
states_list = []
for key in states:
    states_list.append(key)
#print(states_list)
  
while lives > 0:
    state = random.choice(states_list)
    guess = input("What is the capital of " + state + "? ")
    if guess == states[state]:
        print("Correct!")
    else:
        print("Sorry, the capital of", state, "is", states[state])
        lives -= 1
        if lives == 0:
            print("You lost")
        else:
            print("You have", lives, "lives left")
 
        
