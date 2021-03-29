''' 2 dimensional array tricks'''

arr = [(1750, 1800), (1990, 2000) , (1840, 1880), (1850, 1890), (1900, 1970), (1905, 1985)]
running_sum = 0

arr = sorted(arr)

years = {}

# print birth and death in tuples
# for i in arr:
#     print(i)

#print only the birth years
for i in arr:
    print("birth occurred", i[0])
    running_sum+=1
    years[(i[0])] = running_sum


# print only death years
for i in arr:
    print(i[1])
    running_sum-=1
    years[(i[1])+1] = running_sum

print(years)




