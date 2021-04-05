def right_rotate(a, k):
    r = len(a) - k 
    return a[r:] + a[:r]

print(right_rotate[10,20,30,40,50], 2)