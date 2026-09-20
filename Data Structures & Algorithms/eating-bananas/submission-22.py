import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # by design if len(piles) > h, then it is not possible

        # since we want minimum we can iterate from 1 to h and 
        # for each i we can check if that lets koko eat all bananas

        # q: given rate what is the best way to eat 

        def feasible(i, piles):
            time_taken = sum([math.ceil(piles[j]/i) for j in range(len(piles))])
            if time_taken > h:
                return False
            else:
                return True
        
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
            