''' shift a string by k characters given by int '''
import string as alphabet

def cipher(input, k):
    # get entire alphabet
    all = list(alphabet.ascii_lowercase)

    # enumarate letters starting with 1
    enum = enumerate(all, start=1)
    print(all)


 
    # we should use %26 to wrap around

    for nums, vals in enum:
        print(nums, vals)


cipher('denem', 3)