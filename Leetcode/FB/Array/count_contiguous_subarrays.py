def count_subarrays(arr): #O(N^2)
    # Starts from each index,
    # expand towards both directions looking for a larger element.
    n = len(arr)
    result = [1] * n
    st = []
    for i, x in enumerate(arr):
        for di in [1, -1]:
            step = 1
            while 0 <= i + di*step < n and  arr[i+ di*step] < x:
                result[i] += 1
                step += 1

    return result

def stack_solution(arr): #O(N)
    # this solution uses Stacks. Every index starts with n possibilities.
    # Using stack, going from left to right, we remove the subarrays that
    # doesn't satisify the problem condition at this line:
    # 'result[st.pop()] -= n-i'
    # Then we do it again from right to left.
    n = len(arr)
    result = [n] * n
    st = []
    for i, x in enumerate(arr):
        while st and x >= arr[st[-1]]:
            result[st.pop()] -= n-i
        st.append(i)
    st.clear()
    for i, x in reversed(list(enumerate(arr))):
        while st and x >= arr[st[-1]]:
            result[st.pop()] -= i+1
        st.append(i)
    return result

# import random
# arr = [random.randint(1, 100) for _ in range(10)]
# print(arr)
# print(count_subarrays(arr))
# print(bruteforce_solution(arr))
# assert(stack_solution(arr) == bruteforce_solution(arr))


def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  test_1 = [3, 4, 1, 6, 2]
  expected_1 = [1, 3, 1, 5, 1]
  output_1 = count_subarrays(test_1)
  check(expected_1, output_1)
  
  test_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [1, 2, 6, 1, 3, 1]
  output_2 = count_subarrays(test_2)
  check(expected_2, output_2)

  print(count_subarrays(test_1))
  print(count_subarrays(test_2))

  # Add your own test cases here