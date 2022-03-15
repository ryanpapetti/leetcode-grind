# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #find the length of the shorter one
        headA_len = 0
        headB_len = 0
        cursor_a = headA
        cursor_b = headB
        while cursor_a or cursor_b:
            if cursor_a:
                headA_len +=1
                cursor_a = cursor_a.next
            if cursor_b:
                headB_len +=1
                cursor_b = cursor_b.next
        
        larger_skip = abs(headA_len - headB_len)
        
        #reassign
        cursor_a = headA
        cursor_b = headB
        
        if headA_len >= headB_len:
            #make A skip
            for _ in range(larger_skip):
                cursor_a = cursor_a.next
        else:
            for _ in range(larger_skip):
                cursor_b = cursor_b.next
        
        #now traverse both at same pace
        while cursor_a and cursor_b:
            if cursor_a == cursor_b:
                return cursor_a
            cursor_a = cursor_a.next
            cursor_b = cursor_b.next
                
            
        
            