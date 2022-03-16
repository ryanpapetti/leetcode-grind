from collections import deque
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        #strategy: go from right to left
        # the rightmost thing will most definitely be in the output
        # what I want to do is use a stack: LIFO 
        # at each iteration: add the val to the stack ONLY IF val > top of stack
        # at each iteration: call this recursively
        
        stack = deque()
        right_pointer = len(heights) -1
        stack.appendleft(right_pointer) #always visible hehe
        right_pointer -=1
        while right_pointer >= 0:
            #pop the last thing 
            last_top_index = stack.popleft()
            last_top_height = heights[last_top_index]
            stack.appendleft(last_top_index)
            if last_top_height < heights[right_pointer]:
                stack.appendleft(right_pointer)
            
            right_pointer -=1
        
        final_answer = []
        while stack:
            final_answer.append(stack.popleft())
        
        return final_answer
            