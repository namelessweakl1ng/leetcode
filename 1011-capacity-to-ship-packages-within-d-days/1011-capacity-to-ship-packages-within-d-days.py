class Solution(object):
    def shipWithinDays(self, weights, days):
        def canship(capacity):
            curr=0
            day=1
            for weight in weights:
                if weight+curr>capacity:
                    day+=1
                    curr = weight
                else:
                    curr += weight
            return day<=days

        left = max(weights)
        right = sum(weights)

        while left< right:
            mid = (left+right)//2
            if canship(mid):
                right = mid
            else:
                left = mid+1
        return left

        