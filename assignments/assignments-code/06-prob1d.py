# function: simple_sort_1
# inputs: two values, same data type
# processing: sorts values from smallest to largest
# output: values in order from smallest to largest

def simple_sort_1(input1, input2):
    if input1 <= input2:
        return input1, input2
    else:
        return input2, input1

def simple_sort_2(input1, input2, input3):
    #123, 132, 213, 231, 321, 312    
    if input1 <= input2 and input1 <= input3:
        if input2 <= input3:
            return input1, input2, input3
        else:
            return input1, input3, input2
    
    if input2 <= input3 and input2 <= input1:
        if input1 <= input3:
            return input2, input1, input3
        else:
            return input2, input3, input1
            
    if input3 <= input2 and input3 <= input1:
        if input2 <= input1:
            return input3, input2, input1
        else:
            return input3, input1, input2

a,b = simple_sort_1(10,20)
print (a,b) # 10 20

a,b = simple_sort_1(20,10)
print (a,b) # 10 20

a,b = simple_sort_1(30,30)
print (a,b) # 30 30

a,b,c = simple_sort_2(10,20,30)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_2(10,30,20)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_2(30,20,10)
print (a,b,c) # 10 20 30

a,b,c = simple_sort_2(30,20,20)
print (a,b,c) # 20 20 30
        
