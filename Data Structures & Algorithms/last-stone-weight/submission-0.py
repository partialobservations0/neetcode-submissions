class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # brute force solution
        # scan entire array find the two max, and then apply the logic to get the 
        # new array

        while(len(stones) > 1):

            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur: 
                stones.append(cur)
        return stones[0] if stones else 0
