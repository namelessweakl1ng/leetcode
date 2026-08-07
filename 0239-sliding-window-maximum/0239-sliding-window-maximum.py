class Solution(object):
    def maxSlidingWindow(self, nums, k):
        res =[] # to return at the end
        q = collections.deque() # declate a deque
        l = r = 0 # decalring left and right variable 
        while r <len(nums): # the right pointer will move from left to right 
            while q and nums[q[-1]] < nums[r]: # if the q is not empty and the current item is greater than the old then pop that thing
                q.pop()
            q.append(r)# keep appending the right pointer
            if l > q[0]:# if the left pointer removes left val from the window
                q.popleft()
            if r+1 >= k: # if the window size is high then get the max and then move the left
                res.append(nums[q[0]])
                l+=1
            r+=1
        return res