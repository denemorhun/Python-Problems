'''
Fibonacci with DP

'''

def fib_dp(n) -> int:

# base case
    if n == 0 == 1:
        return 1

    # declare array

    # insert base case into array

    nums = [None]*(n+1)

    nums[0] = 1
    nums[1] = 1

    for i in range(2, n+1):
        nums[i] = nums[i-2] + nums[i-1]

    return nums



# return dp prev case fib_dp(n-2) + fib_dp(n-1)


if __name__ == '__main__':
    print(fib_dp(5))