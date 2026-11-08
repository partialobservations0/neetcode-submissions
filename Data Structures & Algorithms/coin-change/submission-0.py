class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
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
        

            
                    