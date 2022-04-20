# function: shuffle_list
# input: a list
# processing: create a shuffled copy of the list
# output: return the shuffled list

import random

def shuffle_list(oldList):
    newList = []

    while len(oldList) > 0:
        # pick a random index and add the item to new list
        pos = random.randint(0, len(oldList) - 1)
        newList.append(oldList[pos])

        # remove element by position from old list
        del oldList[pos]

    return newList

"""
# Tester Code
a = [1,2,3,4,5]
answer = shuffle_list(a)
print(answer)
"""
