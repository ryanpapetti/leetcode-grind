from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        
        

    def next(self, val: int) -> float:
        #popleft and add to the end
        
        #if you are not yet the size, you need to add the number to the queue and return
        if len(self.window) < self.size:
            self.window.append(val)
            return sum(self.window)/len(self.window)
        
        self.window.popleft()

        self.window.append(val)
        return sum(self.window)/len(self.window)
        
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)