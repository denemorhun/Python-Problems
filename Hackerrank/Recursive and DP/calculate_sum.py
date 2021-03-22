'''
Calculate the sigma sum of 1 up to n numbers
'''

def calculate_sum(n):

    if n == 1:
        return 1
    else:
        return n + calculate_sum(n-1)

def calculate_sum_dp(n):
    # base case

    if n == 0:
        return 0

    # init array

    sums = [0]*(n+1)

    # build array bottom up till exclusive n+1

    for i in range(1, n+1):
        sums[i] = i + sums[i-1]
        print(sums[i])
        
    # return the last element in array
    return sums[n]



print(calculate_sum(5))

print(calculate_sum_dp(5))