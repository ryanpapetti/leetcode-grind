class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low_pointer = 0
        high_pointer = len(numbers) -1
        
        while low_pointer < high_pointer:
            relevant_sum = numbers[low_pointer] + numbers[high_pointer]
            if relevant_sum < target:
                low_pointer +=1
            elif relevant_sum > target:
                high_pointer -=1
            else:
                return [low_pointer+1,high_pointer+1]
            
        