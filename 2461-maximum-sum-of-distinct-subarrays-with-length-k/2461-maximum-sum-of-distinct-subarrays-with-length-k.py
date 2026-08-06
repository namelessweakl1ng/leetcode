class Solution(object):
    def maximumSubarraySum(self, nums, k):
        res = 0
        count = defaultdict(int)
        curr_sum = 0
        l = 0
        for r in range(len(nums)):
            curr_sum += nums[r] # add this to the curr_sum integer
            count[nums[r]]+=1 # when you see a number increase the count inside the dict in the default dict

            if r-l+1>k: # if the window is too high then increase the left
                count[nums[l]]-=1 # you are not seeing the left item anymore
                curr_sum-=nums[l] # subtract the thing youre deleting 
                if count[nums[l]]==0: # if it goes to 0 then delete from the window so that it dont mess with the len(count)
                    count.pop(nums[l])
                l+=1 # go forward

            if r- l+1 == k == len(count):
                res= max(res,curr_sum)
        return res