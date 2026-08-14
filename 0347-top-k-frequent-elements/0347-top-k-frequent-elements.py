import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        count = collections.defaultdict(int)

        # Count frequencies
        for num in nums:
            count[num] += 1

        # Sort numbers by frequency
        sorted_nums = sorted(count, key=count.get, reverse=True)

        return sorted_nums[:k]