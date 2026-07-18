class Solution(object):
    def numberOfSubarrays(self, nums, k):
        def algo(k):
            left = odd = ans =0
            for right in range(len(nums)):
                if nums[right] % 2 ==1:
                    odd +=1
                while odd > k:
                    if nums[left]%2==1:
                        odd-=1
                    left+=1
                ans +=right -left +1
            return ans
        return algo(k) - algo(k-1)        