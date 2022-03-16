class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        # tale of two pointers approach
        # start in the middle and go left and right
        # as you go left and right, they have to be the same
        
        # also, I could just put one pointer at the beginning and end, which seems easier
        
        def is_palindrome(s):
            left_pointer, right_pointer = 0, len(s)-1
            while right_pointer > left_pointer:
                left_val, right_val = s[left_pointer], s[right_pointer]
                if left_val != right_val:
                    return False
                left_pointer +=1
                right_pointer -=1
            return True
        
        left_pointer, right_pointer = 0, len(s)-1
        
        
        if is_palindrome(s):
            return True
        
        
        
        while right_pointer > left_pointer:
            left_val, right_val = s[left_pointer], s[right_pointer]
            if left_val != right_val:
                #get everything but the character
                #check if its a palindrome
                everything_but_left_val = s[:left_pointer] + s[left_pointer+1:]
                if is_palindrome(everything_but_left_val):
                    return True
                everything_but_right_val =  s[:right_pointer] + s[right_pointer+1:]
                if is_palindrome(everything_but_right_val):
                    return True
                
                return False
            
            left_pointer +=1
            right_pointer -=1
        
        return True
        
        