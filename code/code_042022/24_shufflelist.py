# shuffle function

import random

# function: shuffle_list
# input: a list
# processing: create a shuffled copy of the list
# output: return the shuffled list

def shuffle_list(oldList):

    newList = []

    # while there are still items in the old list
    while len(oldList) > 0:

        #pick a new position and add it to the new list
        pos = random.randint(0, len(oldList)-1)
        newList.append( oldList[pos] )

        # remove element by position from old list
        del oldList[pos]


    return newList

"""
# Tester Code
a = [1,2,3,4,5]
answer = shuffle_list(a)
print(answer)
"""














