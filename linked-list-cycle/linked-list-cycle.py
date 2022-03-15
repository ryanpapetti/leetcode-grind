# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
                
        if head is None:
            return False
        
        #move a small pointer
        slow_pointer = head

        fast_pointer = head.next
        while bool(slow_pointer and fast_pointer):
            if slow_pointer == fast_pointer:
                return True 
            
            slow_pointer = slow_pointer.next
            
            fast_pointer = fast_pointer.next
            if fast_pointer is None:
                return False
            fast_pointer = fast_pointer.next
        
        return False
            
    
        
        
        