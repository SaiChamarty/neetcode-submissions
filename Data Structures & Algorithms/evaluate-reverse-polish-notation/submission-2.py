import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # my idea is that we have a stack. 
        # we go through the list from 0 to n-1, and if it is a number, we push to stack. If we see an operator, we use that operator on whatever is in the stack. 
        stack = []
        operators = {"+", "-", "*", "/"}
        for item in tokens:
            if item in operators:
                second = stack.pop()
                first = stack.pop()
                if item == "+":
                    stack.append(first + second)
                elif item == "-":
                    stack.append(first - second)
                elif item == "*":
                    stack.append(first * second)
                elif item == "/":
                    try:
                        result = math.trunc(first / second)
                        stack.append(result)
                    except ZeroDivisionError:
                        stack.append(0)
            else:
                stack.append(int(item))
        return stack.pop()
