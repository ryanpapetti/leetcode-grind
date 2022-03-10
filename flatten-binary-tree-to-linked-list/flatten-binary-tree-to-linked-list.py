# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse_fill(self,root,list_fill):
        if root is None:
            return None
        list_fill.append(root.val)
        self.traverse_fill(root.left,list_fill)
        self.traverse_fill(root.right,list_fill)
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        relevant_vals=[]
        
        self.traverse_fill(root,relevant_vals)
        new_root = root
        for val in relevant_vals[1:]:
            new_root.right = TreeNode(val)
            new_root.left = None
            new_root = new_root.right
            
        