class Solution(object):
    def findMinArrowShots(self, points):
        if not points:
            return 0
        points.sort()
        start, end = points[0]
        arrow=1
        for s,e in points[1:]:
            if end>= s:
                start = max(s,start)
                end = min(end ,e)
            else:
                arrow+=1
                start, end = s,e
        return arrow
