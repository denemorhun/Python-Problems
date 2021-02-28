# Python3 code to Check for balanced parentheses in an expression 
# EASY

'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

Solution:
# position 0 -> []
# position 1 -> []
# position 2 -> ()

Use a stack to push all left paranthesis to open list. 
If the item equals the value in both open and closed lists, pop it. 
If we finish with an empty stack, paranthesis are balanced. 

'''

def isValid(input) -> bool:

    # convert string into a list
    input = list(input)

    # code: 0, 1, 2
    open_list = ["[","{","("] 
    close_list = ["]","}",")"] 

    # No paranthesis means matching case
    if list is None:
        return True

    stack = []

    # scroll through each char and add open paranthesis to the stack.
    for i in input: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            # get the paranthesis code: 0, 1, 2
            code = close_list.index(i)

            if len(stack) > 0 and open_list[code] == stack[len(stack)-1]: 
                stack.pop() 

    # If all left paranthesis have been removed from stack we've found all the matches
    if len(stack) == 0: 
        return True
    else: 
        return False

if __name__ == '__main__':

    input = ["khkjhkjhj", "#@#$@#$@", "()", "((([[[{}]]])))", ")(", "((]]", ""]

    for i in input:
        result = isValid(i)
        print("All paranthesis are matching.", i if result else "Mismatch", i)