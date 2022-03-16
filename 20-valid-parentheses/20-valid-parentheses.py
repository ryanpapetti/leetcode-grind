from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        left_pointer = 0
        stack = deque()
        
        char_mapping = {'{':'}', '(':')', '[':']'}
        
        while left_pointer < len(s):
            val = s[left_pointer]
            if stack:
                top_of_stack = stack.popleft()
                if top_of_stack in char_mapping.keys():
                    if val != char_mapping[top_of_stack]:
                    #add both back in 
                        stack.appendleft(top_of_stack)
                        stack.appendleft(val)
                
                else:
                    stack.appendleft(top_of_stack)
                    stack.appendleft(val)
                
            else:
                stack.appendleft(val)
            left_pointer += 1
            
        return not bool(len(stack))
            