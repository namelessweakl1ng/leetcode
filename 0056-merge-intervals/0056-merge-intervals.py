class Solution(object):
    def merge(self, intervals):
        intervals.sort() # sorting by index 0 that is [0,1]
        # to avoid edge cases we already append one index to the result 
        ans = [intervals[0]]
        for start,end in intervals[1:]: # this loops from 1 since the 0 is already appended
            if start<= ans[-1][1]: # comapring wheather the value of new interval value start already in the result
                ans[-1][1]= max(end,ans[-1][1]) # get max of pick the end that is higher since it alread over laps 
            else:
                ans.append([start,end])
        return ans