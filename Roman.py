
# The problem with the code is that it doesnt subtract values if for example :
# IIVM = 995
# II come next to each other and are therefore equal, and are less then the next bigger number
# not subtracting them from V
# So, IIV equals : 5 - 2 = 3 ===> III, thats a duplicate that is invalid in Roman Numerals

def roman_to_integer(rnum):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    
    for char in reversed(rnum):
        current_value = roman_values[char]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value
    
    return total

def check_validity(rnum):
    roman_list = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
    return all(char in roman_list for char in rnum)

rnum = input("Enter Roman Number: ").upper()
if check_validity(rnum):
    print("Integer Value:", roman_to_integer(rnum))
else:
    print("Invalid Roman Numeral")
