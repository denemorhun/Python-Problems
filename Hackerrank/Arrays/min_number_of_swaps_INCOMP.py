'''
NEED TO WORK ON THUS
 find the minimum number of 
 swaps required to sort the array 
 in ascending order.

* compare the values against a pre-sorted array to see if a swap is necessary. Count swaps

'''

def find_min_num_swaps(a):
    num_of_swaps = 0

    for i in range(1, len(arr)):
        if a[i-1] > a[i]:
            t=i;
            a[i], a[i-1] = a[i-1], a[i]
            num_of_swaps += 1
        else: 


    return num_of_swaps

    def minimumSwaps(arr):
    swap=0
    for i in range (len(arr)):
        if(arr[i]!=(i+1)):
            t=i;
            while(arr[t]!=(i+1)):
                t+=1
            temp=arr[t]
            arr[t]=arr[i]
            arr[i]=temp
            swap+=1
    return swap


    
  
# Driver Code 

if __name__ == '__main__':

    inputArray = [-6, -5, -1, 0, 5, 8]

    print(rotate_array(inputArray, 2))


