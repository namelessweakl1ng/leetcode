class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        poison = duration
        for i in range(len(timeSeries)-1):
            if timeSeries[i+1] - timeSeries[i] < duration:
                poison +=  timeSeries[i+1] - timeSeries[i]
            else:
                poison += duration
        return poison
        