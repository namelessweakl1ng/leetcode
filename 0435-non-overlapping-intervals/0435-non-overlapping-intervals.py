class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort() # sort using the python 
        ans = 0 # set ans to 0 since we have not found any to remove yet
        prevEnd = intervals[0][1] # initialze the end so that you can use this 
        for s,e in intervals[1:]: # iterate the whole array
            if s>=prevEnd: # if the start of the current interval is greater then or equal to the prev end it does not overlap
                prevEnd =e # update the prevEnd to the current interval for next iteration 
            else:
                ans+=1 # overlaps so increment by 1 
                prevEnd = min(prevEnd,e) # so you remove the interval which ends at the last
        return ans