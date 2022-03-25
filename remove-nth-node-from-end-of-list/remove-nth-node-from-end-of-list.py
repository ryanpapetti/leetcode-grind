# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #make a cursor
        cursor = head
        #we can do this in one pass if we check if the next * n is None
        previous = None
        fast_cursor = head
        
        for _ in range(n-1):
            fast_cursor = fast_cursor.next
        
        #so fast cursor is N ahead
        
        while fast_cursor.next:
            previous = cursor
            cursor = cursor.next
            fast_cursor = fast_cursor.next
        
        #now remove the cursor
        if cursor == head:
            return head.next
        if previous:
            previous.next = cursor.next
            
            return head
        return previous