class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        return '-' not in num_str and num_str == num_str[::-1]