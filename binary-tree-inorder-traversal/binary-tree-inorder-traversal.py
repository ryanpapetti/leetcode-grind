# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes_traversed = []
        
        def inorder(root):
            if root is None:
                return None
            
            #left
            inorder(root.left)
            
            #root
            nodes_traversed.append(root.val)
            
            #right
            inorder(root.right)
            
        
        inorder(root)
        
        return nodes_traversed
        