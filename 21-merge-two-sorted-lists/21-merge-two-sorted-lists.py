# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def add_at_end(node,new_node):
            if node is None:
                node = new_node
                return None
            last = node
            while last.next:
                last = last.next
            
            last.next = new_node
        
        list3 = ListNode()
        
        while list1 is not None or list2 is not None:
            if list1 and list2:
                if list1.val >= list2.val:
                    #add both - one way to do this is just to add one at random and the other one will get caught next turn
                    # i like 2 hehe
                    new_node = ListNode(list2.val)
                    add_at_end(list3,new_node)
                    list2 = list2.next

                else:
                    new_node = ListNode(list1.val)
                    add_at_end(list3,new_node)
                    list1 = list1.next
            elif list1:
                new_node = ListNode(list1.val)
                add_at_end(list3,new_node)
                list1 = list1.next
            elif list2:
                new_node = ListNode(list2.val)
                add_at_end(list3,new_node)
                list2 = list2.next
                
        return list3.next
