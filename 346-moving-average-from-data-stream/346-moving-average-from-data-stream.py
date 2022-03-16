from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        self.total = 0 #for a more optimized approach, let's keep a running total
        
        

    def next(self, val: int) -> float:
        
        #add the val to the total
        self.total += val
        self.window.append(val)
        
        
        
        if len(self.window) > self.size:
       
            self.total -= self.window.popleft() #update the total to reflect
            

        
        return self.total/len(self.window)
        
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)