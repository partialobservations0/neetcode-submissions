class Solution:
    def countSubstrings(self, s: str) -> int:

        def dp(s):
            n = len(s)
            memo = [[False for _ in range(n)] for _ in range(n)]
            total = 0
            for i in range(n-1, -1, -1):
                for j in range(i,n):
                    if (j - i <= 2 or memo[i+1][j-1]) and s[i] == s[j]: 
                        memo[i][j] = True
                        total += 1 
            return total
        
        return dp(s)

        def expand(l, r): 
            count = 0
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
                count += 1
            return count

        total = 0
        for i in range(0,len(s)):
            total += expand(i, i)
            total += expand(i, i+1)
        return total
