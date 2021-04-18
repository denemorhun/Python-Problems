

from typing import Type


def evaluate_post_fix(string):

    stack = []
    try:

        for i in string:
            # if number append to stack
            if i.isdigit():
                stack.append(i)
            # skip spaces
            elif i == ' ':
                continue
            # if operator is encountered pop twice and run op
            else:
                num_to_right = stack.pop()
                num_to_left = stack.pop()
                stack.append(operate(num_to_left, num_to_right, i))
                # push the result back into the stack and run op
     
    except TypeError:
        return "Invalid sequence"

    return int(float(stack.pop()))

def operate(num1, num2, op):
    return eval(f"{num1} {op} {num2}")

print(evaluate_post_fix('638*+4-')) #26
print(evaluate_post_fix('921 * - 8 - 4 +')) #3
print(evaluate_post_fix('98 - 4 +')) #5
print(evaluate_post_fix('92 *')) #18
