'''
Find the number of ways you can partition n objects using parts upto m.

m > 0

'''

def waze(n, m):

    # if our chunk is larger than actual object, limit it to object size
    # if m > n:
    #     m = n
# base case
    if n == 0:
        return 1

    # if n < m case
    elif m == 0 or n < 0:
        return 0

    # if n < m:
        # return 0

    else:
        return waze(n-m, m) + waze(n, m-1)

print('1,1', waze( 1, 1))
print('2,1', waze( 1, 1))
print('2,2', waze(2, 2))
print('3,2', waze(3, 2))
print('3,3', waze(3, 3))
print('2,3', waze(2,3))
print('5,2', waze(5,2))
print('5,3', waze(5,3))
print('7,4', waze(7,4))

