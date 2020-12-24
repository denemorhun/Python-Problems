'''
A prime is a natural number greater than  that has no 
positive divisors other than  and itself. Given a number
determine and print whether it is prime or not prime. 

Input Format

The first line contains an integer, , the number of test cases.
Each of the  subsequent lines contains an integer, , to be tested for primality.

Sample Input

3
12
5
7
Sample Output

Not prime
Prime
Prime
Explanation

Test Case 0: .
 is divisible by numbers other than  and itself (i.e.: , , , ), so we print  on a new line.

Test Case 1: .
 is only divisible  and itself, so we print  on a new line.

Test Case 2: .
 is only divisible  and itself, so we print  on a new line.

SOLUTION

To eliminate the input pool, follow the 3 following premises:

1) Eliminate all even numbers 
2) no factor can be greater than sqrt of the number.
3) Keep track of prime numbers and only use these as factors. 

'''

import math


# get the number of entries to be made       
def get_entries():
        # number of lines to be entered (t)
        print("Enter number of entries to be made")
        t = int(input())

        entries = []

        # read t lines from STDIN
        for i in range(0, t):
            entries.append(int(input().strip()))
          #  print(entries[i])
        
        return entries
    
def sqrt(num):
    #50 -> 7
    return int(math.sqrt(num))


# generate factors up until the square root of largest num
def generate_factors(entries):

    global factors

    max_num = max(entries)
    #50

    factor = sqrt(max_num)
    # 7

    factors = list(range(2, factor+1))
    #3, 4, 5, 6, 7
    return factors


# Verify if number is a prime number
def check_if_prime(n):

    # 0 and 1 are not prime numbers
    if n == 0 or n == 1:
        print( f"{n} Not prime")
        return
   
    # eliminate all even numbers at O(1) time
    if n % 2 == 0 and n != 2:
        print(n, "Not Prime")
        return

    isPrime = True

    for p in factors:
        #3, 4, 5, 6, 7
        if p > n:
            break
        if n % p == 0:
            isPrime = False
            break

    print("Prime" if isPrime else "Not Prime")

def main():
    # read input 
    entries = get_entries()

    # generate factors from entries
   
    generate_factors(entries)
     #2, 3, 4, 5, 6, 7

    for num in entries:
        check_if_prime(num)
    
if __name__ == '__main__': main()