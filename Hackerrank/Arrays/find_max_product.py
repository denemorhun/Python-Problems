'''Validate Pattern from array 1 to array b

Given a string sequence of words and a string sequence pattern, return true if the sequence of words matches the pattern otherwise false.

Definition of match: A word that is substituted for a variable must always follow that substitution. For example, if "f" is substituted as "monkey" then any time we see another "f" then it must match "monkey" and any time we see "monkey" again it must match "f".

Examples
input: "ant dog cat dog", "a d c d"
output: true
This is true because every variable maps to exactly one word and vice verse.
a -> ant
d -> dog
c -> cat
d -> dog

input: "ant dog cat dog", "a d c e"
output: false
This is false because if we substitute "d" as "dog" then you can not also have "e" be substituted as "dog".
a -> ant
d, e -> dog (Both d and e can't both map to dog so false)
c -> cat

input: "monkey dog eel eel", "e f c c"
output: true
This is true because every variable maps to exactly one word and vice verse.
e -> monkey
f -> dog
c -> eel

1) Sort input array in increasing order. 
2) If all elements are positive, then return the product of the last two numbers. 
3) Else return a maximum of products of the first two and last two numbers. 


'''
def max_products_using_sort(array):

    # matching_values dictionary
    array.sort()

    return max (array[0]*array[1], array[-1]*array[-2])

###################################################################
# A O(n) Python 3 program to find maximum product pair in an array 
####################################################################
  
# Function to find maximum product by finding max and 2nd max
def maxProduct(arr): 
  
    n  = len(arr)
    if (n < 2): 
        print("No pairs exists") 
        return
  
    if (n == 2): 
        print(arr[0] ," " , arr[1]) 
        return
  
    # Iniitialize maximum and  
    # second maximum 
    posa = 0
    posb = 0
  
    # Iniitialize minimum and  
    # second minimum 
    nega = 0
    negb = 0
  
    # Traverse given array 
    for i in range(n): 
      
        # Update maximum and second 
        # maximum if needed 
        if (arr[i] > posa): 
            posb = posa 
            posa = arr[i] 
          
        elif (arr[i] > posb): 
            posb = arr[i] 
  
        # Update minimum and second  
        # minimum if needed 
        if (arr[i] < 0 and abs(arr[i]) > abs(nega)): 
            negb = nega 
            nega = arr[i] 
          
        elif(arr[i] < 0 and abs(arr[i]) > abs(negb)): 
            negb = arr[i] 
  
    if (nega * negb > posa * posb): 
        print("Max product pair is (" ,  
                nega ,", ", negb , ")") 
    else: 
        print( "Max product pair is (" , 
                 posa ,", " ,posb , ")") 
  
# Driver Code 

if __name__ == '__main__':

    inputArray = [-6, -5, -1, 0, 5, 8]

    print(max_products_using_sort(inputArray))
    maxProduct(inputArray)

