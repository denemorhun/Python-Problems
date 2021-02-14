# Remove Dupes from sorted array

'''
given a dictionary, assuming keys and values are unique
get key from value
'''

# function to return key for any value
def get_key(val, my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key


if __name__ == '__main__':

    n = 9

    my_dict = {'raptor': 3, 'cat': 1, 'dog': 9, 'rabbit': 2}

    result = get_key(n, my_dict)

    print (f' {n} {result} ')