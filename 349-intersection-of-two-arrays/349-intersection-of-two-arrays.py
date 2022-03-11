class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
    
    # know you can make it a lot more optimized. For example, you can only iterate via the size of the smallest array to make the runtime O(N) rather than O(N+M) 