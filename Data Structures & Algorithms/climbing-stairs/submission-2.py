class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1: return 1
        if n == 2: return 2
        N = [0] * (n+1)
        N[1] = 1
        N[2] = 2
        
        for i in range(3,n+1):
            N[i] = N[i-2] + N[i-1]
        return N[n]



