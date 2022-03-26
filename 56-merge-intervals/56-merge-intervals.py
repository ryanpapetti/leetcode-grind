class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #strategy
        if not intervals:
            return []
        if len(intervals) == 1:
            return intervals
        #i am gonna sort intervals
        intervals.sort()
        output_array = [intervals[0]]
        output_pointer = 0
        #now go through intervals[1:]
        for interval in intervals[1:]:
            relevant_output = output_array[output_pointer]
            if interval[0] > relevant_output[1]:
                output_array.append(interval)
                output_pointer +=1
            elif interval[0] <= relevant_output[1]:
                output_array[output_pointer][1] = max(interval[1], relevant_output[1])
                
        
        return output_array
        # if the interval min is greater than the max of the added interval --> add another one
        # if the interval min not greater than max of added interval --> update added interval max to be max of interval; stay with added interval
        
        
        