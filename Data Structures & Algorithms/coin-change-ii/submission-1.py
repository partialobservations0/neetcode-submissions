class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        nways = [0] * (amount + 1)
        nways[0] = 1

        coins.sort()

        for n in range(len(coins)-1, -1, -1):
            coin = coins[n]
            for amt in range(coin, amount + 1):
                if amt - coin >= 0:
                    nways[amt] = nways[amt-coin] + nways[amt]
    
        return nways[-1]

        