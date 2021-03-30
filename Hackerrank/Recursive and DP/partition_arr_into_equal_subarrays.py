'''Partition into two arrays of equal sum'''

''' Depth first search

DFS - O(2**n) complexity

Need to use DP

'''


def canPartition(nums) -> bool:
    def dfs(nums, n, subset_sum) -> bool:
        # Base cases
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            result = (dfs(nums, n - 1, subset_sum - nums[n - 1])
                    or dfs(nums, n - 1, subset_sum))
            return result

    # find sum of array elements
    total_sum = sum(nums)

    # if total_sum is odd, it cannot be partitioned into equal sum subsets
    if total_sum % 2 != 0:
        return False

    subset_sum = total_sum // 2
    n = len(nums)
    return dfs(nums, n - 1, subset_sum)


print(canPartition([1, 5, 5, 11]))

''' Efficient solution using bottom up DP

time complexity O(m*n) '''

def canPartition(nums) -> bool:
        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)

        # construct a dp table of size (n+1) x (subset_sum + 1)
        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            curr = nums[i - 1]
            for j in range(subset_sum + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
        return dp[n][subset_sum]