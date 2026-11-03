class Solution:
    def numDecodings(self, s: str) -> int:

        def dp(s):

            memo = [False]*len(s)+1
            memo[-1] = True
            for i in range(len(s)-1, -1, -1):
                if int(s[i]) < 10 and int(s[i]) > 0 and memo[i+1]:
                    memo[i] = True



        dp = {len(s): 1}
        def dfs(i):
            
            if i in dp:
                return dp[i]
            if i == len(s):
                return 1
            
            if int(s[i]) < 10 and int(s[i]) > 0:
                res = dfs(i+1)
            else:
                return 0 
            
            if i < len(s) - 1:
                if int(s[i:i+2]) < 27 and int(s[i:i+2]) > 9:
                    res += dfs(i+2)
            dp[i] = res
            return res
        return dfs(0)