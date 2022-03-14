# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        nodes_traversed = []
        
        def preorder(root):
        
            if root is None:
                return []
            
            
            #do root first
            nodes_traversed.append(root.val)

            #do left
            preorder(root.left)
            

            #do right
            preorder(root.right)
            
        
        preorder(root)
        return nodes_traversed
        
        