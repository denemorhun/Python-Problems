#!/usr/bin/env python3
# Find the intersection of 2 arrays of "distinct" elements


def return_intersection(arr1, arr2):

    arr1 = set(arr1)
    arr2 = set(arr2)

    return list(arr1.intersection(arr2))

def return_difference(arr1, arr2):

    arr1 = set(arr1)
    arr2 = set(arr2)

    return list(arr1.difference(arr2))

def dict_solution(arr1, arr2):
    mydict = dict.fromkeys(arr1)

    for item in arr2:
        if item in mydict.keys():
            mydict[item] = True

    for key, value in mydict.items():
        if value is True:
            print(key)

def main():

    arr1 = [1, 2, 7, 3, -3, 0, 55]
    arr2 = [1, 7, -3, 0, 55, 88]

    print(return_intersection(arr1, arr2))

    print(return_difference(arr1, arr2))

    dict_solution(arr1, arr2)

if __name__ == '__main__': main()
