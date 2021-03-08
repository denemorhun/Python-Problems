''' shift a string by k characters given by int 

    Use chr() and ord() builtin functions

    values must be between 97 and 122 for lower case 
    must wrap around once it passes

    chr(ord('b')+3)

    # we can also use a hashmap to create our own dict

    # we need to use modulus to wrap around

'''

def caesarCipherEncryptor(string, k):
    encrypted = []

    # if shift > alphabet size, reduce by length of alphabet
    if k >= 26:
        k = k % 26
	
    for letter in string:
        # shift each char
        x = ord(letter) + k
        # if we go past z = 122
        if x > 122:
            encrypted.append(chr(96 + x % 122))
        else:
        	encrypted.append(chr(x))   

    return "".join(encrypted)


# encrypted the string by n letters in the alphabet
print(caesarCipherEncryptor('xyz', 28))