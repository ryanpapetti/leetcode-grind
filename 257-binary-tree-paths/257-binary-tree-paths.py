# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def is_leaf(node):
            return not (node.left or node.right)
        
        valid_paths = []
        def build_path(node, path):
            
            if node:
                if is_leaf(node):
                    path.append(str(node.val))
                    valid_paths.append('->'.join(path))
                else:
                    build_path(node.left,path + [str(node.val)])
                    build_path(node.right,path + [str(node.val)])
                    
                    

        build_path(root,[])
        return valid_paths