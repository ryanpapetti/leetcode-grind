class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = {ind:val for ind,val in enumerate(nums) if val}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        common_keys = set(self.vector.keys()) & set(vec.vector.keys())
        total_sum = 0
        for key in common_keys:
            total_sum += self.vector.get(key) * vec.vector.get(key)
        return total_sum
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)