class Solution:
    def __init__(self):
        self.trace = set()
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        #sum digits in n until number // 10 == 0
        
        if n in self.trace:
            return False
        
        self.trace.add(n)
        sum_of_digits_n = sum([int(char)**2 for char in str(n)])
        
        return self.isHappy(sum_of_digits_n)
        
        