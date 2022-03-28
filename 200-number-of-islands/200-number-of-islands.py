class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    #look all around
                    total_islands +=1 
                    self.lookFunc(grid,row,col)
        return total_islands
    
    
    
    def lookFunc(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or grid[row][col] == '0':
            return None #base case
        
        grid[row][col] = '0'
        self.lookFunc(grid, row,col+1)
        self.lookFunc(grid, row+1,col)
        self.lookFunc(grid, row-1,col)
        self.lookFunc(grid, row,col-1)
                    
                    