''' Given two strings, find whether a ransom note is possible

input long_str, short_str
 '''

from collections import Counter

def find_ransom(long_str, short_str):

    big_dict = Counter(long_str)
    small_dict = Counter(short_str)
    print(big_dict)
    print(small_dict)

    for key in small_dict.keys():
        print(key)
        if key not in big_dict.keys():
            print("key not in big dict")
            return False
        elif small_dict[key] > big_dict[key]:
                print('Not sufficient characters available for ransom note')
                return False

    return True

def main():
    long_str = "abcdabcdggghhhekkladkfa"
    short_str = "abcggg"

    print(find_ransom(long_str, short_str))

if __name__ == '__main__': main()
