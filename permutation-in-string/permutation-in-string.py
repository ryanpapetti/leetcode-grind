class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # my way is this: build windows size of s1.
        # slide across s2 in size of s1
        # if s1 is bigger or None --> False
        # in each window: sort s1 and s2-window. they need to match to be the same
        # if they match --> woo hoo
        # if they don't match --> just keep swimming
        
        if len(s1) > len(s2):
            return False

        s2_window = s2[:len(s1)]
        does_match = True
        for char in set(s1):

            does_match = does_match and (s1.count(char) == s2_window.count(char))
        
        
        if does_match:
            return True

        else:
            return self.checkInclusion(s1,s2[1:])
        
        
        
        
        