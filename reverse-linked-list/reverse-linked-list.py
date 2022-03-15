# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        # one solution is to iterate the nodes in original order and move them to the head of the list one by one
        cursor = head
        next_nodes = cursor.next
        
        #now call recursion
        reversed_list = self.reverseList(next_nodes)
        
        head.next.next = head
        head.next = None
        
        return reversed_list

        
            
        
        

 
        