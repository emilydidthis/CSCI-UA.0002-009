def string_length(word):
    length = 0
    for c in word:
        length += 1
    return length

# create list of ords for A-Z [65-90]; a-z[97-122]
ord_info = []
for num in range(65,91):
    ord_info.append(num)
for num in range(97, 123):
    ord_info.append(num)
    
def string_isalpha(word):
    validation = []
    for c in word:
        validation.append(ord(c) in ord_info)

    if validation == [] or False in validation:
        return False
    else:
        return True
'''
print ( string_isalpha("apple")     )	# True
print ( string_isalpha("pear!")     )	# False
print ( string_isalpha("123")       )	# False
print ( string_isalpha("123 AbC")   )	# False
print ( string_isalpha("abc1")      )	# False
print ( string_isalpha("")          )	# False
'''

# EVERYTHING IS CAPITAL
# Happy Birthday

def string_capitalize(word):
    proceed_space = True
    output = ""
    for c in word:
        # check if capitalized already
        if ord(c) in range(65,91):
            if proceed_space:
                # add as is, no conversion necessary
                output += c
                proceed_space = False
            # if there wasn't a space before
            else:
                # convert it to lower
               output += chr(ord(c) + 32)
        # otherwise, it's lowercase
        else:
            #if there was a space before
            if proceed_space:
                #convert lower to upper
                output += chr(ord(c) - 32)
                proceed_space = False
            else:
                # add as is
                output += c
        if c == " ":
            output += c
            proceed_space = True
    return output
        
print( string_capitalize("happy birthday sad kitten") )
# Happy Birthday Sad Kitten

print( string_capitalize("every word in this phrase should start with a capital letter") )
# Every Word In This Phrase Should Start With A Capital Letter

print( string_capitalize("EVERYTHING IS UPPERCASE ALREADY!") )
# Everything Is Uppercase Already!

print( string_capitalize("cRaZy MIxeD cAse") )
# Crazy Mixed Case
            
            
