class Solution:
    
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #the O(logn) hint suggests I use Binary Search, which made sense regardless

        left_pointer = 0
        right_pointer = len(nums)-1
        
        def binary_search(left_pointer, right_pointer ):
        
            print(left_pointer,right_pointer)
            if not nums:
                return [-1,-1]

            left_val = nums[left_pointer] 
            right_val = nums[right_pointer]

            if left_val == right_val == target:
                return [left_pointer,right_pointer]

            if left_val > target or right_val < target:
                return [-1,-1]


            if left_val < target:
                left_pointer += 1

            if right_val > target:
                right_pointer -=1

            if right_val == target:
                return binary_search(left_pointer, right_pointer)
            if left_val == target:
                return binary_search(left_pointer, right_pointer)

            return binary_search(left_pointer, right_pointer)
        
        return binary_search(left_pointer, right_pointer)
            