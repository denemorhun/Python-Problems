'''encode input wtring AAAAAABBC as 6A2B1C'''

def runLengthEncoding(string):

	print("input will be", string)
    # count needs to be at least for each char
    count = 1
	new_array = []

	# scroll through array for length
    for i in range(len(string)-1):
		
	# compare i with i+1, if equal, increment count during run
		if string[i] is not string[i+1] or count == 9:
			
			print(f"{string[i]} at {i} compared with {string[i+1]} at {i+1}")
			print('appending count', count)
			new_array.append(count)
			new_array.append(string[i])
			
			print(new_array)
			count = 0
			
		# increment count by 1
		count += 1
	
	#handle the last run
	new_array.append(count)
	new_array.append(string[len(string) - 1])
			
    return ''.join(map(str, new_array)) 


if __name__ == '__main__':

   inputarray = "AAAAAABBCCCDDDDD"