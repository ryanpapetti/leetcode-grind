class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {2:'abc',3:'def', 4:"ghi", 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        

        final_combos = []
        
        def produceCombos(digit_ind=0,path=[]):
            if len(digits) == len(path): #base case AKA we have a full path and we don't care about smaller than that; let's add
                final_combos.append("".join(path))
                return None 
            relevant_chars = mapping.get(int(digits[digit_ind]))
            for char in relevant_chars:
                #this excerpt below EXACTLY produces the relevant size combinations
                path.append(char)
                
                produceCombos(digit_ind+1,path)
                path.pop()
                        
        produceCombos()
        
        return final_combos
                
                    
                    
                                     
                
                    
            