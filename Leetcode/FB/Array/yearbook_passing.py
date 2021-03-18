'''
 O(N) time/space (Python) solution.

Consider that each student is a member of a single yearbook passing cycle.
For example, for input [3, 2, 4, 1], there are two yearbook passing cycles: {3, 4, 1} and {2}.
Therefore, the number of signatures for each member of a passing cycle is equal to the size of the cycle.
In the example, students {3, 4, 1} each get 3 signatures (1 for his/her self, and 1 for the other 2 students), and student {2} gets 1 signature, his/her own signature.
The yearbook passing cycle for any group of students can be determined starting with a particular student, and traversing through the input until the next student to receive the book is the first student of the cycle. (I thought of the cycle like a circular linked list.)

An O(N) time algo can achieved if it considers a student only one time. That is, as the root of a passing cycle, or as a member of a passing cycle that is visited before the traversal returns to the root member.

Algo

Follow the passing cycle of the first student until it returns back to the first student.
Along the way, mark each student (the root and traversed nodes) as visited.
Save the count of the members in the cycle with the root node.
For each node traversed (nodes other than the root node), save a reference to the root node.
Repeat the above for any students that have yet to be visited.
For each root node, return the size of its cycle.
For each traversed node, return the size of the cycle of its root node.

Complexity

time - O(N)
space - O(N) <- O(max(input, signatures, root_indexes arrays and visited_students set are all size N)


'''

def findSignatureCounts(arr):
    output=[]
  
    for i,x in enumerate(arr,1):
        next = arr[x-1]
        count = 0
        while arr[next-1] != i:
            count += 1
            next = arr[next-1]
            print(i, x, next, count)
        output.append(count + 1)
        
    return output

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
  arr_1 = [2, 1]
  expected_1 = [2, 2]
  output_1 = findSignatureCounts(arr_1)
  check(expected_1, output_1)

  arr_2 = [1, 2]
  expected_2 = [1, 1]
  output_2 = findSignatureCounts(arr_2)
  check(expected_2, output_2)


