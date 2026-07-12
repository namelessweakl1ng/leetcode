class Solution(object):
    def arrayRankTransform(self, arr):
        sorted_arr = sorted(set(arr))
        hash_map = {}
        for i,num in enumerate(sorted_arr):
            hash_map[num] = i+1
        return [hash_map[num] for num in arr]