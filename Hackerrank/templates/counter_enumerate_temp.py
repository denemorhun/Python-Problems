from collections import Counter 

list_of_animals = ['cat', 'dog', 'rabbit', 'raptor', 'raptor', 'raptor']
print(*enumerate(list_of_animals))

seen = Counter(list_of_animals)
print(seen, *seen.values())
#cat dog rabbit raptor 1 1 1 3

print(seen['cat'])
print(list_of_animals.count('raptor') )
# 1

print ("Is cat in the collection? ", 'cat' in x)
# true