import heapq, math

a1 = [1, 3, 5, 10, 4, 8]
a2 = [-1, -4, 0]
a3 = [-8, -9, -10, 4, 0, 5, 7, 9]
a4 = []
a5 = [1, 4]
a6 = [-6, -5, -3, -7, -9]

def heap_solution_for_max_triplets(a):

    if len (a) < 3:
        print("Too short")
        return -1

    # get the max three items.
    max_items = heapq.nlargest(3, a)

    # get the min 2 items

    min_items = heapq.nsmallest(2, a)

    output = max((max_items[0] * max_items[1] * max_items[2]), (min_items[0] * min_items[1]) * max_items[0])

    print(output)


# naive solution O(n2) (same array)
def naive_solution(a):

    mp = 0

    for i in range(0, len(a)):
        for j in range(i+1 , len(a)):
            if a[i] * a[j] >= mp:
                mp = a[i] * a[j]

    print(mp)

# heap solution
def heap_solution(a):

    if len(a) < 2:
        return -1
    # get the max 2 items
    max_items = heapq.nlargest(2,a)
    # get the min items
    min_items = heapq.nsmallest(2, a)
    print( max(math.prod(max_items), math.prod(min_items)))


assert 400, heap_solution_for_max_triplets(a1)
assert 0, heap_solution_for_max_triplets(a2)
assert 810, heap_solution_for_max_triplets(a3)
assert 'Too short', heap_solution_for_max_triplets(a4)
assert 'Too short', heap_solution_for_max_triplets(a5)
assert -90, heap_solution_for_max_triplets(a6)
