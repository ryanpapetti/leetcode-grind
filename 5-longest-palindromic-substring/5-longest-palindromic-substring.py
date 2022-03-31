class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        #go to middle of string
        # check if its a palindrome
        # if not, check the same thing but just the left size and the right side
        
        if not s:
            return ''
        
        end = len(s) - 1
        
        longest_str = ''
        
        for i,char in enumerate(s):
            #iterate until a palindrome is found
            #if the len is longer replace it
            odd_size_str = self.expandFromMiddle(s,i,i)
            even_size_str = self.expandFromMiddle(s,i,i+1)
            if len(odd_size_str) > len(even_size_str):
                longer_str = odd_size_str
            else:
                longer_str = even_size_str
        
        
            if len(longest_str) < len(longer_str):
                longest_str = longer_str
        
        return longest_str
            
            

            
        
        
    
    def expandFromMiddle(self,s,left,right):
        if not s or left > right:
            return ''
        
        if right > len(s) -1:
            return s[left]
        
        if len(s) == 1:
            return s
        
        if not left:
            if s[left] == s[right]:
                return s[left:right+1]
            return s[left]
        
        
        if s[left] != s[right]:
            return s[left]
        
        
        
        #the idea is to expand outward until the chars dont match anymore
        
        
        while left > 0 and right < len(s) - 1 and s[left] == s[right] :
            if s[left-1] == s[right+1]:
                left -=1
                right +=1
            else:
                return s[left:right+1]
        return s[left:right+1]
            