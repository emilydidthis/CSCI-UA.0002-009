# function:   horizontal_line
# input:      a width value (integer) and a single character (string)
# processing: generates a single horizontal line of the desired size
# output:     returns the generated pattern (string)

def horizontal_line(width,char):
    return width*char + "\n"

# function:   vertical_line
# input:      a shift value and a height value (both integers)  and a single character (string)
# processing: generates a single vertical line of the desired height.  the line is
#             offset from the left side of the screen using the shift value
# output:     returns the generated pattern (string)

def vertical_line(shift,height,char):
    pattern = ""
    for i in range(height):
        pattern += shift*" " + char + "\n"
    return pattern

# function:   two_vertical_lines
# input:      a width value and a height value (both integers)  and a single character (string)
# processing: generates two vertical lines.  the first line is along the left side of
#             the screen. the second line is offset using the "width" value supplied
# output:     returns the generated pattern (string)

def two_vertical_lines(width,height,char):
    pattern = ""
    for i in range(height):
        pattern += char + " "*(width-2) + char + "\n"
    return pattern


def number_0(width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += two_vertical_lines(width, 3, character)
    pattern += horizontal_line(width, character)
    return pattern

# function:   number_1
# input:      a width value (integer) and a single character (string)
# processing: generates the number 1 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_1(width, character):
    pattern = vertical_line(width-1, 5, character)
    return pattern

def number_2(width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 1, character)
    pattern += horizontal_line(width, character)
    pattern += vertical_line(0, 1, character)
    pattern += horizontal_line(width, character)
    return pattern

def number_3(width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 1, character)
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 1, character)
    pattern += horizontal_line(width, character)
    return pattern

def number_4(width, character):
    pattern = ""
    pattern += two_vertical_lines(width, 2, character)
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 2, character)
    return pattern

def number_5(width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += vertical_line(0, 1, character)
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 1, character)
    pattern += horizontal_line(width, character)
    return pattern

def number_6(width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += vertical_line(0, 1, character)
    pattern += horizontal_line(width, character)
    pattern += two_vertical_lines(width, 1, character)
    pattern += horizontal_line(width, character)
    return pattern

def number_7(width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 4, character)
    return pattern

def number_8(width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += two_vertical_lines(width, 1, character)
    pattern += horizontal_line(width, character)
    pattern += two_vertical_lines(width, 1, character)
    pattern += horizontal_line(width, character)
    return pattern

def number_9(width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += two_vertical_lines(width, 1, character)
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 2, character)
    return pattern

# function:   print_number
# input:      a number to print (integer), a width value (integer) and a single character (string)
# processing: prints the desired number to the screen using the supplied width value
# output:     does not return anything

def print_number(number, width, character):
    for i in range(0, 10):
        if i == number:
            output = globals()["number_" + str(i)](width, character)
            print(output)

# plus function
def plus(width, character):
    if width % 2 == 0:
        pattern = vertical_line(width//2-1, 2, character*2)
        pattern += horizontal_line(width, character)
        pattern += vertical_line(width//2-1, 2, character*2)
    else:
        pattern = vertical_line(width//2, 2, character)
        pattern += horizontal_line(width, character)
        pattern += vertical_line(width//2, 2, character)
    return pattern

# minus function
def minus(width, character):
    return "\n" * 2 + (character * width) + "\n" * 2
    
# function:   check_answer
# input:      two numbers (number1 & number2, both integers); an answer (an integer)
#             and an operator (+ or -, expressed as a String)
# processing: determines if the supplied expression is correct.  for example, if the operator
#             is "+", number1 = 1, number2 = 2 and answer = 3 then the expression is correct
#             (1 + 2 = 3).
# output:     returns True if the expression is correct, False if it is not correct

def check_answer(num1, num2, answer, operator):
    if operator == "+":
        if num1 + num2 == answer:
            return True
        else:
            return False
    else:
        if num1 - num2 == answer:
            return True
        else:
            return False
