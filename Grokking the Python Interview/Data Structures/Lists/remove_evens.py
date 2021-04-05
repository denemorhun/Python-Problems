# remove all evens from an input list
# O(n) because entire list must be iterated

def remove_even(arr):
    odds = [num for num in arr if num%2 != 0]
    return odds
    
print(remove_even([1,2,4,5,10,6,3]))