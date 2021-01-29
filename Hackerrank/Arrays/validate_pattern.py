'''Validate Pattern from array 1 to array b

Given a string sequence of words and a string sequence pattern, return true if the sequence of words matches the pattern otherwise false.

Definition of match: A word that is substituted for a variable must always follow that substitution. For example, if "f" is substituted as "monkey" then any time we see another "f" then it must match "monkey" and any time we see "monkey" again it must match "f".

Examples
input: "ant dog cat dog", "a d c d"
output: true
This is true because every variable maps to exactly one word and vice verse.
a -> ant
d -> dog
c -> cat
d -> dog

input: "ant dog cat dog", "a d c e"
output: false
This is false because if we substitute "d" as "dog" then you can not also have "e" be substituted as "dog".
a -> ant
d, e -> dog (Both d and e can't both map to dog so false)
c -> cat

input: "monkey dog eel eel", "e f c c"
output: true
This is true because every variable maps to exactly one word and vice verse.
e -> monkey
f -> dog
c -> eel
'''

def is_it_a_pattern(arr, patt):

    # matching_values dictionary
    mv = {}

    #isPattern = True 

    if len(arr) != len(patt):
        return False

    for i in range(len(arr)):
        if arr[i] not in mv.keys():
            mv[arr[i]] = patt[i]
        else:
            if mv[arr[i]] != patt[i]:
                return False

    return True


if __name__ == '__main__':

    color1 = ["red", "green", "green"] 
    patterns1 = ["a", "b", "b", "d"]

    print( "True" if is_it_a_pattern(color1, patterns1) else "False")

    color2 = ["blue", "green", "blue", "blue"] 
    patterns2 = ["blue", "b", "c", "c"]

    print( "True" if is_it_a_pattern(color2, patterns2) else "False")