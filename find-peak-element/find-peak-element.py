import math
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        def get_neighbors(nums,index):
            if not index:
                return [nums[1]]
            if index == len(nums) - 1:
                return [nums[len(nums) - 2]]
            
            return nums[index-1], nums[index+1]
        
        left_pointer = 0
        right_pointer = len(nums) - 1
        while left_pointer <= right_pointer:
            left_neighbors = get_neighbors(nums,left_pointer)
            if len(left_neighbors) == 2:
                
                if nums[left_pointer] > left_neighbors[0] and nums[left_pointer] > left_neighbors[1]:
                    return left_pointer
            else:
                if nums[left_pointer] > left_neighbors[0]:
                    return left_pointer
                
            left_pointer +=1
            right_neighbors = get_neighbors(nums,right_pointer)
            if len(right_neighbors) == 2:
                
                if nums[right_pointer] > right_neighbors[0] and nums[right_pointer] > right_neighbors[1]:
                    return right_pointer
            else:
                if nums[right_pointer] > right_neighbors[0]:
                    return right_pointer
            
            right_pointer -=1
            