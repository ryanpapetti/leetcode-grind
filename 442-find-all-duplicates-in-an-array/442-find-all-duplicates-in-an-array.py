class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        for ind, num in enumerate(nums):
            retrieved_val = nums[abs(num) - 1]
            if retrieved_val < 0:
                output.append(abs(num))
            else:
                nums[abs(num) - 1] = -1 * nums[abs(num) - 1]
        return output