class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 4 or len(set(s)) == 1:
            return len(set(s))
        longest_substr = 0
        for starting_ind in range(len(s)-2):
            right_edge = starting_ind + 2
            considered_substr = s[starting_ind:right_edge]
            validate_substr = lambda substr: len(substr) == len(set(substr))
            
            while validate_substr(considered_substr) and right_edge < len(s) + 1:
                longest_substr = max((longest_substr,len(considered_substr)))
                right_edge +=1
                considered_substr = s[starting_ind:right_edge]
        return longest_substr