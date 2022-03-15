# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = [0]
        def traverse_tree(root):
            if root is None:
                return None
            
            if root.val >= low and root.val <= high:
                total[0] += root.val
            
            traverse_tree(root.left)
            traverse_tree(root.right)
        
        traverse_tree(root)
        return total[0]