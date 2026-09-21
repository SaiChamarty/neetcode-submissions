class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # let the stack be a list. But we follow LIFO
        parenthesis_map = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        for n, char in enumerate(s):
            if char in parenthesis_map: 
                # if it is a closing bracket, look for opening
                if len(stack) != 0 and stack[-1] == parenthesis_map[char]:
                    # if the top of the stack is the opening, pop and continue
                    stack.pop()
                    continue
                else:
                    # if it is not at the top of the stack, then return false
                    return False
            else:
                # this is an opening bracket, add that to stack.
                stack.append(char)
                
        if len(stack) != 0:
            return False
        
        return True
            