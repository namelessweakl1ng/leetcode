class Solution(object):
    def maxArea(self, height):
        l,r = 0 , len(height)-1 # taking 2 pointers at each end
        res=0
        while l<r:
            area = (r-l) * min(height[l],height[r]) # calculate area every time the l,r is updated
            res = max(res ,area) # and update the max
            if height[l] < height[r]: # if the left is less then move left
                l+=1
            else:# if right is less them move the right
                r-=1
        return res 
        