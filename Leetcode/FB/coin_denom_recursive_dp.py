#!/bin/python3

''' Medium:

Calculate the number of ways using DP whether or not target money can be 
obtained using a denomitor. 

ETC: 10$ -> denoms{1, 2, 5}

'''

def canGetExactChange(n, denoms):
    print(denoms, "target ->", n)
    # init array with 0, to return 0 if no denoms are found
    waze = [0]*(n+1)
	
	  #base case, if target is 0, only 1 way of combining denoms
    waze[0] = 1
	
	  #scroll through each coin
    for denom in denoms:
		# calculate waze[1], waze[2]... till we reach waze[n]
    # print("Current denom, ", denom)
		  # for a given denom, increment if there is a solution
      for i in range(1, n+1):
			# if the denom is > target we have 0 solution
        if denom <= i:	
          print(f'i={i}, waze[i]={waze[i]}')
          print(f'waze[{i} - {denom}] = {waze[i - denom]}')
          waze[i] += waze[i - denom]
          print(f'Updated, now waze[{i}] = ', waze[i])
				
	  # return the sum of ways at the last index
    print(f'Sum at last index waze({n})', waze[n])
    return waze[n] != 0



# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  # target_1 = 94
  # arr_1 = [5, 10, 25, 100, 200]
  # expected_1 = False
  # output_1 = canGetExactChange(target_1, arr_1)
  # check(expected_1, output_1)

  # target_2 = 75
  arr_2 = [4, 17, 29]
  # expected_2 = True
  # output_2 = canGetExactChange(target_2, arr_2)
  # check(expected_2, output_2)

  print(calculate_change(75, arr_2))

  # Add your own test cases here
  