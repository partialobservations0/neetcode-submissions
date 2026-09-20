class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def getCost(cost):
            n = len(cost)

            C = [0] * (n + 1)
            for i in range(2, n+1):
                C[i] = min( C[i-1] + cost[i-1] , C[i-2] + cost[i-2] )
            return C[n]
        
        return getCost(cost)