class Solution(object):
    def insert(self, intervals, newInterval):
        res = []
        
        for interval in intervals: # looping through the array
            if interval[1] < newInterval[0]: # the current item is before the given interval so append it
                res.append(interval)
            elif interval[0] > newInterval[1]: # after the given interval
                res.append(newInterval) # add the newInterval and then assign the interval to the newinterval again
                newInterval = interval  # until it reaches the end and the last one is appended after the loop ends 
            else:
                newInterval[0] = min(newInterval[0],interval[0])
                newInterval[1] = max(newInterval[1],interval[1])
        res.append(newInterval)
        return res
