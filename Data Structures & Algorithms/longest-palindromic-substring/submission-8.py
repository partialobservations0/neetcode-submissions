class Solution:
    def longestPalindrome(self, s: str) -> str:

        
        def dp(s):
            grid = [[0 for _ in range(len(s))] for _ in range(len(s))]
            for i in range(0,len(s)):
                grid[i][i] = 1
            resIdx, resLen = 0, 1
            for i in range(len(s)-1, -1, -1):
                for j in range(i+1, len(s)):
                    if ((grid[i+1][j-1]==1 or j-i==1) and s[i] == s[j]):
                        grid[i][j] = 1
                        if resLen < (j - i + 1):
                            resIdx = i
                            resLen = j - i + 1
            return s[resIdx : resIdx + resLen]

        def bruteforce(s):
            resLen = 0
            for i in range(len(s)):
                for j in range(i,len(s)):
                    l, r = i, j
                    while l < r and s[l] == s[r]:
                        l += 1
                        r -= 1
                    
                    if l >= r and resLen < (j - i + 1):
                        res = s[i:j+1]
                        resLen = j - i + 1
            return res
        return dp(s)