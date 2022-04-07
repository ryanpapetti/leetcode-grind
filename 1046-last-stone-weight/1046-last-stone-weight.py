import math
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        if len(stones) == 0:
            return 0
        
        
        
        max1,max2 = stones.pop(self.get_max_ind(stones)), stones.pop(self.get_max_ind(stones))
        
        if max1!=max2:
            stones.append(max1-max2)
        
        return self.lastStoneWeight(stones)
            
    
    
    def get_max_ind(self,arr):
        max_num = -math.inf
        max_ind = -1
        for ind,num in enumerate(arr):
            if num > max_num:
                max_num,max_ind = num,ind
        
        return max_ind
        