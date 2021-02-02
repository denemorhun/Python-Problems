''' Rotate array by n index

'''

def rotate_array(a, n):

    return a[n:] + a[:n]


    
  
# Driver Code 

if __name__ == '__main__':

    inputArray = [-6, -5, -1, 0, 5, 8]

    print(rotate_array(inputArray, 2))


