class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        inner_size = len(matrix[0])
        outer_size = len(matrix)
        
        left_row_pointer = 0
        right_row_pointer = outer_size -1
        
        found_right_row = False
        
        while not found_right_row and right_row_pointer >= left_row_pointer:
            left_row_vals = matrix[left_row_pointer][0],matrix[left_row_pointer][inner_size-1]
            right_row_vals = matrix[right_row_pointer][0],matrix[right_row_pointer][inner_size-1]
            if target == left_row_vals[0] or target == left_row_vals[1]:
                return True
            
            if target == right_row_vals[0] or target == right_row_vals[1]:
                return True
            
            if target > left_row_vals[0] and target < left_row_vals[1]:
                found_right_row = matrix[left_row_pointer]
            
            elif target > right_row_vals[0] and target < right_row_vals[1]:
                found_right_row = matrix[right_row_pointer]
            
            
            
            if target > left_row_vals[1]:
                left_row_pointer +=1
            
            if target < right_row_vals[0]:
                right_row_pointer -=1
        
        
        if not found_right_row:
            return False
        
        
        correct_row_pointer_left = 0
        correct_row_pointer_right = inner_size -1
        
        while correct_row_pointer_left <= correct_row_pointer_right:
            left_val, right_val = found_right_row[correct_row_pointer_left], found_right_row[correct_row_pointer_right]
            
            if left_val == target or right_val == target:
                return True
            
            if left_val < target:
                correct_row_pointer_left +=1
            
            if right_val > target:
                correct_row_pointer_right -=1
            
        
                
            
        
        