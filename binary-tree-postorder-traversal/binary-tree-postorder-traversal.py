# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes_traversed = []
        def postorder(root):
            
            if root is None:
                return None
            
            #do left
            postorder(root.left)
            
            #do right
            postorder(root.right)
            
            #do root
            nodes_traversed.append(root.val)
            
        postorder(root)
        return nodes_traversed
            
            