''' Script to check whether string is a palindrome '''

def check_palindrome(input):

    arr = list(input)

    left_idx = 0
    right_idx = len(input) - 1

    # if left idx surpasses right idx we've passed the middle
    while(left_idx < right_idx):

        if arr[left_idx] != arr[right_idx]:
            return False

        left_idx += 1
        right_idx -= 1

    return True

if __name__ == '__main__': 

    errorMsg = 'not a palindrome'

    #assert check_palindrome('abba'), errorMsg
    #assert check_palindrome('abbas'), errorMsg
    #assert check_palindrome(''), errorMsg
    assert check_palindrome('1221'), errorMsg
    #assert check_palindrome('adafafad'), errorMsg
    assert check_palindrome('ttttttttt'), errorMsg
