#!/usr/bin/env python3
# author: Denem Orhun
'''
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.: .
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, .
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the .
If the book is returned after the calendar year in which it was expected, there is a fixed fine of .
Example
 returned date
 due date

The book is returned on time, so no fine is applied.

 returned date
 due date

The book is returned in the following year, so the fine is a fixed 10000.

Input Format

The first line contains  space-separated integers denoting the respective , , and  on which the book was actually returned.
The second line contains  space-separated integers denoting the respective , , and  on which the book was expected to be returned (due date).

Constraints

Output Format

Print a single integer denoting the library fine for the book received as input.

Sample Input

STDIN       Function
-----       --------
9 6 2015    day = 9, month = 6, year = 2015 (date returned)
6 6 2015    day = 6, month = 6, year = 2015 (date due)
Sample Output

45
Explanation

Given the following return dates:
Returned: 
Due: 

Because , it is less than a year late.
Because , it is less than a month late.
Because , it was returned late (but still within the same month and year).

Per the library's fee structure, we know that our fine will be . We then print the result of  as our output.


Simple integer solution:

rd, rm, ry = [int(x) for x in input().split(' ')]
ed, em, ey = [int(x) for x in input().split(' ')]

if (ry, rm, rd) <= (ey, em, ed):
    print(0)
elif (ry, rm) == (ey, em):
    print(15 * (rd - ed))
elif ry == ey:
    print(500 * (rm - em))
else:
    print(10000)

    
'''

import datetime
  
# get the number of entries to be made       
def get_dates():
    returned_date = input()
    due_date = input()

    try:
        returned_date = datetime.datetime.strptime(returned_date, '%d %m %Y').date()
        due_date = datetime.datetime.strptime(due_date, '%d %m %Y').date()
    except (ValueError, TypeError):
        exit

    return (returned_date, due_date)


def calculateFine() -> int:

    dates = get_dates()

    ret_date = dates[0]
    due_date = dates[1]

    fine = 0

    # book is returned on or before the expected return date, no fine will be charged 

    print(ret_date.day)
    print(due_date.day)
   
    if ret_date <= due_date:
        return fine
    elif ret_date > due_date:
        # book is returned after return day but within the same calendar month and year
        if ret_date.day != due_date.day and ret_date.month == due_date.month and ret_date.year == due_date.year:
            fine = 15 * (ret_date.day -  due_date.day)
        # book is returned after return month but within the same calendar year
        if ret_date.month != due_date.month and ret_date.year == due_date.year:
            fine = 500 * (ret_date.month - due_date.month)
        # book is returned after the calendar year in which it was expected
        if ret_date.year > due_date.year:
            fine = 10000

    return fine



if __name__ == '__main__':
        print(calculateFine())