'''
Climbing stairs, how many ways can we climb some stairs given number of steps

Recursive solution, we do not need to keep the entire array. This is a space optimization.

'''

def num_ways_recursive(n, denoms) -> int:

    # base case
    if n == 0:
        return 1

    total_ways = 0

    # only if total steps - current denom > 0 should we consider climbing.
    # ie, if steps are 4, using 5 steps is out of bounds. 
    for i in denoms:
        if n-i >= 0:
            total_ways += num_ways_recursive(n-i, denoms)

    return total_ways


def num_ways_dp(n, denoms) -> int:

    # base case
    if n == 0:
        return 1

    # declare array
    nums = [0]*(n+1)

    # populate the base case
    nums[0] = 1

    

    # Build array for other cases by starting with base case
    for steps in range(1, n+1): #i = 1

        total_ways = 0

        # with each iteration, build the total number of steps the size of n will take
        for denom in denoms:
        # if jump is greater than max steps, we skip
            if steps >= denom:
              #  print(f's= {steps}, denominator ={denom}')

              #  print(f' ')
                total_ways += nums[steps - denom] 
                print('tw', total_ways)  # i = 1
                    
        nums[steps] = total_ways
       # print('total num of steps for step',steps,  nums[steps])

    print(nums)
    return nums[n]

if __name__ == '__main__':

    # print('recursive')
    # print(num_ways_recursive(4, [1, 3, 5]))
    # print(num_ways_recursive(3, [1, 2]))

    print("hello burcu")
    print(num_ways_dp(4, [1, 3, 5]))
    print(num_ways_dp(3, [1, 2]))