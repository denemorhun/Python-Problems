
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

    for l in input:
        print(l)

        if l.isupper():
            print ("Char is upper ", l)
        elif l.islower():
            print("Char is lowercase", l)
        elif l.isnumeric():
            print("Char is numeric")
        else:
            print("Char is special char")
        




 # driver code
if __name__ == '__main__':
    input = ""

    #l1 = ListNode

    result = rotationalCipher('Zebra----0000', 6)