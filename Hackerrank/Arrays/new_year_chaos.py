'''
 Each person wears a sticker indicating their initial 
 position in the queue from  to . Any person can bribe 
 the person directly in front of them to swap positions, 
 but they still wear their original sticker. One person can 
 bribe at most two others.

Determine the minimum number of bribes that took place to get
 to a given queue order. Print the number of bribes, or, if 
 anyone has bribed more than two people, print Too chaotic.

  Each person wears a sticker indicating their initial position 
  in the queue from  to . Any person can bribe the person directly 
  in front of them to swap positions, but they still wear their original 
  sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given 
queue order. Print the number of bribes, or, if anyone has bribed more than
 two people, print Too chaotic.

Example

 All you need to do is to count the number of people who overtake a person.

Loop through each person in the queue and check two things: 1. Has this person 
moved more than two positions forward? 2. How many times has this person been bribed?
'''

def minimumBribes(Q):
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


