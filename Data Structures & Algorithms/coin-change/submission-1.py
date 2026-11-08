class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    

        def dp_sol(amount,coins):

            memo = {i:float('inf') for i in range(amount+1)}
            memo[0] = 0

            for i in range(1,amount+1):
                for _, c in enumerate(coins):
                    if i - c >= 0: 
                        memo[i] = min(memo[i - c] + 1, memo[i])
            return -1 if memo[amount] == float('inf') else memo[amount]

        return dp_sol(amount,coins)


        dp = {0:0}
        def search(amount, coins):
            if amount < 0:
                return float('inf')
            if amount in dp:
                return dp[amount]
            best = float('inf')

            for coin in coins:
                best = min(best, 1 + search(amount - coin, coins))
            dp[amount] = best
            return best
        
        res = search(amount,coins)
        return -1 if res == float('inf') else res
        



            
                    