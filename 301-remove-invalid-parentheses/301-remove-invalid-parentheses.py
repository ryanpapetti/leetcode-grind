from collections import deque

class Solution:
    
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        
        def isValid(str_to_validate):
            iterative_left_count = 0                        
            for char in str_to_validate:
                if char == '(':
                    iterative_left_count +=1
                elif char == ')':
                    iterative_left_count -=1
                
                if iterative_left_count < 0:
                    return False
            
            return not iterative_left_count
    
        
        
        
        if not s:
            return [s]
        
        
        found = False
        already_tested_strs = set()
        valid_strs = set()
        
        working_queue = deque()
        working_queue.append(s)
        
        while working_queue: #while it is not empty
            testable_str = working_queue.popleft() #give me the firstmost element
            
            if isValid(testable_str):
                valid_strs.add(testable_str)
                found = True
            
            if found:
                continue
            
            for ind, char in enumerate(testable_str):
                if char in "()":
                    new_str = testable_str[:ind] + testable_str[ind+1:]
                    if new_str not in already_tested_strs:
                        working_queue.append(new_str)
                        already_tested_strs.add(new_str)
                        
        
        return list(valid_strs) if valid_strs else ['']
                
        
        
        
        
        
        
        
        