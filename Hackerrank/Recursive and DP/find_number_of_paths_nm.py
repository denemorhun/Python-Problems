'''
Find the number of paths from 0,0 to m,n

hint: 1, 1 has only 1 path. If either m or n is 1. 
'''

def find_no_paths(n, m):
# base case
    if m == 1 or n == 1:
        return 1
    else:
        return find_no_paths(n-1, m) + find_no_paths(n, m-1)

print('1,1',find_no_paths( 1, 1))
print('2,2', find_no_paths(2, 2))
print('3,2', find_no_paths(3, 2))
print('2,3', find_no_paths(2,3))
print('4,3', find_no_paths(4, 3))
print('3,4', find_no_paths( 3, 4))
print('4,5', find_no_paths( 4, 5))
