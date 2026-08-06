class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        res = 0
        curr_sum = 0
        l = 0

        for r in range(len(arr)):
            curr_sum +=arr[r]

            if r-l+1>k:
                curr_sum-=arr[l]
                l+=1
            if r-l+1==k and (curr_sum)/k>=threshold:
                res +=1
        return res