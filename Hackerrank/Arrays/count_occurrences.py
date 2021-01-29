from collections import Counter 

list_of_nums = [1, 3, 5, 0, 7, 9, 444]
# print(*enumerate(list_of_nums))

count = Counter(list_of_nums)
print(count)

# print(*count.values())

print("3 occurs", count[3])
print("3 occurs" ,list_of_nums.count(3) ) # -> 1

print ("Is cat in the collection? ", 9 in list_of_nums)
# true

isAllUnique = True

for i in count.values():
    if i > 1:
        isAllUnique = False

print("Are all values unique?", isAllUnique)