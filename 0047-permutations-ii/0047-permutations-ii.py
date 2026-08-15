class Solution(object):
    def permuteUnique(self, nums):
        count = {n:0 for n in nums}
        res =[] # total rsult of all the list in a list
        perm =[] # current permutation being built

        for n in nums:
            count[n]+=1

        # make the dict ful
        def dfs():
            if len(nums) == len(perm):
                res.append(perm[:])
                return # if the end of the dfs is reached that is if the count i=0 for all the elementts in the array
                
            for n in count:
                if count[n]>0:
                    perm.append(n)
                    count[n]-=1

                    dfs()

                    count[n]+=1
                    perm.pop()
        dfs()
        return res