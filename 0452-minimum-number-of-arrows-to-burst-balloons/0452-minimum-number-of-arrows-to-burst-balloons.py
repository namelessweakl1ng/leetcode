class Solution(object):
    def findMinArrowShots(self, points):
        if not points: # nothin exist then return 0
            return 0
        points.sort() # sorts the array by the index[0]
        start, end = points[0] # initialize the start and the end so that the points can be used to compare
        arrow=1 # if there is a value in points then obviously we will need one arrow
        for s,e in points[1:]: # take the loop from index 1 till the end
            if end>= s: # this says it overlaps
                start = max(s,start) # finding the intersection of the two intervals to throw a arraow at
                end = min(end ,e)
            else:
                arrow+=1 # if the range is not a intersection then you will need another arraow
                start, end = s,e # reinitialize the start and the end so that you can keep the loop going 
        return arrow
