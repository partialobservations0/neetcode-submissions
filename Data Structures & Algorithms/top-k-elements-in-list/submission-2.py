from collections import defaultdict
import operator
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) <= k:
            return list(set(nums))
        counts = defaultdict(int)
        for i,n in enumerate(nums):
            counts[n] = counts[n] + 1
        counts = sorted(counts.items(), key=lambda x: x[1])
        print(counts)
        keys = [counts[-k+i][0] for i in range(k)]
        return keys