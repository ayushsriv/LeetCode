class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amount += 1
        dp = [amount]*(amount)
        for i in range(amount):
            if i%coins[0]==0:
                dp[i] = int(i/coins[0])
        
        for coin in coins[1:]:
            for i in range(amount):
                if i-coin>=0:
                    dp[i] = min(dp[i-coin]+1, dp[i])        

        if dp[-1] == amount:
            return -1
        else:
            return dp[-1]
 