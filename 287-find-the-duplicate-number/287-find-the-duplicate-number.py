class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #okay things I got before I saw hints
        # the NOT modifying the og array makes me :(
        # the constant extra space hints towards a pointer approach
        # the duplicate idea hints towards a linked list (since no modifying)
        # the linked list will be built like so
        # [1,3,4,2,2] --> 0 -- > 3 --> 2 --> 4 -- (back) 2
        # head(ind, next = nums[ind])
        # but how do i know when to stop making the list?
        slow,fast = 0,0
        
        havent_found_cycle = True
        
        while havent_found_cycle:
            slow = nums[slow]
            fast = nums[nums[fast]] #just do it twice
            
            if slow == fast:
                havent_found_cycle = False
            
        
        #cycle found, move until a new pointer meets the slow one
        
        snail = 0
        while True:
            slow = nums[slow]
            snail = nums[snail]
            if snail == slow:
                return slow
            
                
 

        
        
        
        