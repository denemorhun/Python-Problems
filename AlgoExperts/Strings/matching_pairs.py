''' Count number of matching pairs between two strings'''

def matching_pairs(s, t):

  # Write your code here
  counter = 0
  if s == t:
    return len(s) - 2
  else:
    for c in range (len(s)):
      if s[c] == t[c]:
        counter += 1
        continue
    if len(s)-2 <= counter:
      return counter+2
  
  











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  s_3, t_3 = "abcdef", "abcdef"
  expected_3 = 4
  output_3 = matching_pairs(s_3, t_3)
  check(expected_3, output_3)