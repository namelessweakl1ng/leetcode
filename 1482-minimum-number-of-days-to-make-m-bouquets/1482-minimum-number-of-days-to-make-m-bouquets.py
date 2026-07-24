class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m*k>len(bloomDay):
            return -1
        def canmake(days):
            flowers =0
            bouquets = 0
            for bloom in bloomDay:
                if bloom<=days:
                    flowers+=1
                    if flowers==k:
                        bouquets +=1
                        flowers = 0
                else:
                    flowers=0
            return bouquets>=m

        left = min(bloomDay)
        right = max(bloomDay)
        while left<=right:
            mid = (left+right) //2
            if canmake(mid):
                right = mid -1
            else:
                left = mid+1
        return left