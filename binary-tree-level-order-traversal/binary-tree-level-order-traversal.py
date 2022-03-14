# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        
        
        makeshift_queue = deque() #FIFO principle
        nodes_traversed = []
        makeshift_queue.append(root)
        level = 0
        while len(makeshift_queue):

            nodes_traversed.append([])
            level_elems = len(makeshift_queue)
            for _ in range(level_elems):
                
                pointer = makeshift_queue.popleft()
                nodes_traversed[level].append(pointer.val)
            
            
            

                if pointer.left:
                    makeshift_queue.append(pointer.left)
                if pointer.right:
                    makeshift_queue.append(pointer.right)
                
            level +=1
            
            
            
        return nodes_traversed