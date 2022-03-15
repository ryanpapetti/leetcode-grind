# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        final_sum = ListNode()
        final_sum_cursor = final_sum
        
        while l1 is not None or l2 is not None:
            #sum the values
            mini_sum = 0
            
            if l1:
                mini_sum +=l1.val
                l1 = l1.next
                
            
            if l2:
                mini_sum += l2.val
                l2 = l2.next
            
            
            
            #add at end
            while final_sum_cursor.next is not None:
                final_sum_cursor = final_sum_cursor.next
            
            new_val = (final_sum_cursor.val + mini_sum % 10)

            if new_val > 9:
                final_sum_cursor.val = new_val % 10
                final_sum_cursor.next = ListNode(1)
                
            else:
                final_sum_cursor.val = new_val
                if l1 is not None or l2 is not None:
                    final_sum_cursor.next = ListNode(mini_sum // 10)
                else:
                    if mini_sum // 10:
                        final_sum_cursor.next = ListNode(mini_sum // 10)

        return final_sum
        