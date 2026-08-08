class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = total =0
        res = float("inf") # take the highes value

        for r in range(len(nums)):# move the right pointer incresing the window
            total +=nums[r]# keep incrementing until the value is either equal to the target or greater
            while total>=target: # move the left till the total is greater than or wqual to the target
                res = min(res,r-l+1)
                total -= nums[l]
                l+=1
        return 0 if res == float("inf") else res