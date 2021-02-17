
# EASY

'''
"rotate" every alphanumeric character by a certain amount. Rotating a 
character means replacing it with another character that is a certain 
number of steps away in normal alphabetic or numerical order.
For example, if the string "Zebra-493?" is rotated 3 places, the 
resulting string is "Cheud-726?". Every alphabetic character is 
replaced with the character 3 letters higher (wrapping around from 
Z to A), and every numeric character replaced with the character 
3 digits higher (wrapping around from 9 to 0). 
Note that the non-alphanumeric characters remain unchanged.
Solution:

if code is not isnumeric()
ASCII code 48 - 57 -> Numbers 

isupper() and and isalpha()
ASCII code 65 - 90 -> UpperCASE

islower() and isalpha()
Ascii code 97 - 122 -> lowercase

# function to get ascii for number
    x = ord(letter) + k
    
    # if we go past z=122

'''

#!/bin/python3

def rotationalCipher(input, rotation_factor):

    ALPHABET = 26
    DIGITS = 10
    k = rotation_factor
    rotated_arr = []

    for l in input:
        if l.isupper():
            rotate_helper(l, k, ALPHABET, 90, 64, rotated_arr)
        elif l.islower():
            rotate_helper(l, k, ALPHABET, 122, 96, rotated_arr)
        elif l.isnumeric():
            rotate_helper(l, k, DIGITS, 57, 47, rotated_arr)
        else:
            rotated_arr.append(l)
        
    return "".join(rotated_arr)

def rotate_helper(l, k, size, upper_limit, lower_limit, arr):
    enc_idx = ord(l) + k % size
    
    if enc_idx > upper_limit:
        enc_idx = enc_idx % upper_limit + lower_limit
        arr.append(chr(enc_idx))
    else:
        arr.append(chr(enc_idx))

 # driver code
if __name__ == '__main__':

    result = rotationalCipher('Zebra-493', 3)
    print(result)

