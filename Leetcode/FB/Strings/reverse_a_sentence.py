''' Reverse a sentence

Reverse the string.
Traverse the string and reverse each word in place.

denem is an orhun -> orhun is an denem

'''

def reverse_string(string):
    return string[::-1]

def parse_string(string):
    array_of_words = string.split(" ")
    return array_of_words

def return_reversed_sentence(string):
    # take the reversed string
    reversed = reverse_string(string)

    # break it down into separate words separated by space
    parsed_array = parse_string(reversed)

    for i in range(len(parsed_array)):
        word = parsed_array[i]
        word = reverse_string(word)
        parsed_array[i] = word

    print(" ".join(parsed_array))

return_reversed_sentence("denem is an orhun")