''' 3 SUM array solved at O(N2) using 2 pointer solution
'''

def threeNumberSum(array, targetSum):
	
	sums = []
	
    #Sorting the array at O(nlog(n))  is dwarfed by O(n2)
	a = sorted(array)

	print(a)
	s = len(a)
	
	# iterate through a
	L = R = 0
	
	for i in range(s):
		print('For it', i, 'Values are a[i]', a[i], 'L', L, 'R', R)
		R = s - 1
		L = 1 + i
		while L < R :
			
			if a[i] + a[L] + a[R] == targetSum:
				u = [a[i], a[L], a[R]]
				print ('Sum is equal to TS', u)
				sums.append(u)
				L += 1
				R -= 1
			elif a[i] + a[L] + a[R] < targetSum: 
				L += 1
				print('sum < Target, inc L to', L)
				
			elif a[i] + a[L] + a[R] > targetSum:
				R -= 1
				print('sum > Target, dec R to ', R)

	return sums		

if __name__ == '__main__':
    input ={"array": [12, 3, 1, 2, -6, 5, -8, 6], "targetSum": 0}

    result = threeNumberSum(input["array"], input["targetSum"])

    print('The sums are,' ,result)
        
        
