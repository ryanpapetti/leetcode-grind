class Solution:
    def isPalindrome(self, s: str) -> bool:
#         final_str = (''.join([char for char in s if char.isalpha() or char.isnumeric()])).lower()
        
#         return final_str == final_str[::-1]
        
        
        left_pointer, right_pointer = 0, len(s)-1
        while right_pointer > left_pointer:
            #now we need to check if the character is valid. if it aint, keep moving
            while right_pointer > left_pointer and not s[left_pointer].isalnum():
                left_pointer +=1
                
            while right_pointer > left_pointer and not s[right_pointer].isalnum():
                right_pointer -=1
            
            left_val, right_val = s[left_pointer].lower(), s[right_pointer].lower()
            
            if left_val != right_val:
                return False
            left_pointer +=1
            right_pointer -=1
        return True