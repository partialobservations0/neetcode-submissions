class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        storage = {}
        if not nums:
            return 0
        for i in nums:
            storage[i] = 1
        cnts = []
        for i in nums:
            cnt = 1
            while(i+1 in storage):
                i += 1
                cnt += 1
            cnts.append(cnt)
        return max(cnts)
