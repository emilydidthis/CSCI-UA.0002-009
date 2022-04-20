# function:    listlen
# INPUT:       a list
# PROCESSING:  determines the size of the list
# OUTPUT:      an integer representing the size of the list

def listlen(l):
    counter = 0
    for i in l:
        counter += 1
    return counter

'''
mylist = [10, 20, 30]
x = listlen(mylist)
print (x)
'''

# function:    listmax
# INPUT:       a list
# PROCESSING:  obtains the largest element in the list
# OUTPUT:      returns the largest element in the list

def listmax(l):
    if listlen(l) == 0:
        return "None"
    else:
        maxi = l[0]

        for i in l:
            if i > maxi:
                maxi = i
        return maxi

'''
mylist = [10, 20, 30, 5, 3]
x = listmax(mylist)
print (x)
print (mylist)
'''

# function:    listcopy
# INPUT:       a list
# PROCESSING:  creates a new list which serves as a copy of the supplied list
# OUTPUT:      returns a new copy of the list

def listcopy(l):
    new_list = [] + l
    return new_list

'''
mylist = [10, 20, 30]
x = listcopy(mylist)
print (x)
'''

# function:    listappend
# INPUT:       a list and an element to add to the list (any data type)
# PROCESSING:  creates a new list which includes the new element appended
#              to the end of the list
# OUTPUT:      returns a new copy of the list

def listappend(l, item):
    return l + [item]

'''
mylist = [10, 20, 30]
x = listappend(mylist, 999)
print (x)
'''

# function:    listinsert
# INPUT:       a list, a location (integer) and a data 
#              element (can be a string, float, Boolean or 
#              int)
# PROCESSING:  inserts the supplied data element into the 
#              list at the desired location
# OUTPUT:      return a new copy of the list that contains
#              the inserted element

def listinsert(l, index, item):
    return l[:index] + [item] + l[index:listlen(l)]

'''
mylist = [10, 20, 30]
x = listinsert(mylist, 1, 999)
print (x)
print (mylist)
'''

# function:    listremove
# INPUT:       a list and a data element (can be a string, 
#              float, Boolean or int)
# PROCESSING:  removes all occurrences of the supplied 
#              data element from the list.  You can assume 
#              that the data element is present in the list 
#              somewhere.
# OUTPUT:      return a new copy of the list with the
#              desired element removed

def listremove(l, item):
    for i in range(listlen(l)):
        if l[i] == item:
            return l[0:i] + l[i+1:listlen(l)]
        
'''
mylist = [10, 20, 30]
x = listremove(mylist, 20)
print (x)
print (mylist)
'''

# function:    listreverse
# INPUT:       a list
# PROCESSING:  creates a copy of the supplied list that
#              contains the same elements as the original
#              list, but in reverse order
# OUTPUT:      return a new copy of the list in reverse order

def listreverse(l):
    return l[::-1]

mylist = [10, 20, 30]
x = listreverse(mylist)
print (x)
print (mylist)



