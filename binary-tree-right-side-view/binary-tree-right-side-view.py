# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
#     def has_child(self,node):
#         return node.right or node.left
    
#     def special_traverse(self,root, ignore_root = False):
#         if root is None:
#             return []
#         proper_root_val = [root.val] if not ignore_root else []

#         if root.right is None and root.left:
#             return proper_root_val + self.special_traverse(root.left)
#         if root.right and not self.has_child(root.right) and root.left and self.has_child(root.left):
#             return proper_root_val + [root.right.val] + self.special_traverse(root.left, ignore_root = True)
#         return proper_root_val + self.special_traverse(root.right) + self.special_traverse(root.left)[len(self.special_traverse(root.right)):]
            
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        partial_correct_view = [root.val] + self.rightSideView(root.right) 
        return partial_correct_view + self.rightSideView(root.left)[len(self.rightSideView(root.right)):]
        
        