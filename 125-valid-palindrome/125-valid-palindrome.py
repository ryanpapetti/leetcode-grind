class Solution:
    def isPalindrome(self, s: str) -> bool:
        final_str = (''.join([char for char in s if char.isalpha() or char.isnumeric()])).lower()
        
        return final_str == final_str[::-1]
        