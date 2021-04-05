"""
revenues = [10,20,30,40,50,70,80,90,100]
milestones = [100,200,300]

Check the days when milestones are reached

output (4, 6, 10)
"""

# Two loop solution

from collections import deque

def findRevenues(revenues, milestones):
    results = []
    runningSum = 0

    for day in range(len(revenues)):

        runningSum += revenues[day]
        print(runningSum)

        for milestone in milestones:
            if runningSum >= milestone:
                results.append(day+1)
                milestones.pop(0)

    print(results)

if __name__ == "__main__":

    revenues_1 = [100, 200, 300, 400, 500]
    milestones_1 = [300, 800, 1400]
    expected_1 = [2, 4, 5]

    findRevenues(revenues_1, milestones_1)


