# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None: #base cases
            return l2
        elif l2 is None: #base cases
            return l1
        elif l1.val < l2.val: #if l2 is bigger than l1, the l1 good - move down it
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1 #once all the recursion stacks are hit, this completely sorts it... recursion is nice
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2