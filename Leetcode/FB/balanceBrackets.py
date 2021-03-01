"""
Balance Brackets

EASY

DS: Stack 

Codify the brackets with 0, 1, 2

open_bracket_list = ['(', '{', '[']

closed_bracket_list = [')', '}', ']']
"""

from collections import deque

def balance_brackets(string):
    
    stack = []

    # trick is to codify paranthesis type with 0, 1, 2
    open_bracket_list = ['(', '{', '[']
    closed_bracket_list = [')', '}', ']']

    for p in string:
        if p in open_bracket_list:
            stack.append(p)
        elif p in closed_bracket_list and stack is not None:
            # if the index of closed list == last entry from stacks 
            
            if closed_bracket_list.index(p) == open_bracket_list.index(stack[-1]): 
                stack.pop()

    print(stack)

    if len(stack) == 0:
        return True
    else:
         return False

if __name__ == "__main__":

    # Must operate LIFO
    string = '([{ (((  %% )))} ] )'

    print("Brackets are balanced" if balance_brackets(string) else "Mismatch")