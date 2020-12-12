'''
find the maximum absolute difference between values array

'''


def max_abs_difference(numbers) -> int:
    # sort the array
    numbers = sorted(numbers)

    size = len(numbers)

    max_diff = abs(numbers[size-1] - numbers[0] )
    
    return max_diff

print(max_abs_difference([2, 4, 5, -9, 0, 4]))

