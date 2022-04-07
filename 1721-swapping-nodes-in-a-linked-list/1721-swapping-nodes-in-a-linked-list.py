# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start_cur, end_cur, head_counter, new_head = head, head, head, head
        
        head_count = 1
        while head.next:
            head = head.next
            head_count +=1
            
        
        
        
        for _ in range(k-1):
            start_cur = start_cur.next
        
        
        for _ in range(head_count - k):
            end_cur = end_cur.next
                    
        start_cur.val, end_cur.val = end_cur.val, start_cur.val
        
        return new_head
        