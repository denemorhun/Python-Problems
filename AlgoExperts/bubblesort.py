# EASY
'''
Binary search array, target recursively
'''

def binarySearch(array, target):
    return _bs(array, target, left = 0, right = len(array) - 1)

def _bs(array, target, left, right):
	# if we exhaust our indices, number is not in list
	if left > right:
		return -1
	
	midpoint = (left + right) // 2
	print(f"left -> {left}, right -> {right}, midpoint -> {midpoint}")
	
	# target is left of target, eliminate all indices to right
	if target < array[midpoint]:
		right = midpoint - 1
		return _bs(array, target, left, right)
    # target is right of target, eliminate all indices to left
	elif target > array[midpoint]:
		left = midpoint + 1
		return _bs(array, target, left, right)
	else:
		print("final midpoint", midpoint)
		return midpoint

if __name__ == '__main__':
        input = {"array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], "target": 45}

        print(input["array"], input["target"])

        result = binarySearch(input["array"], input["target"])

        print(result)
        
        
