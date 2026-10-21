class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # we need to initialise with some max value like inf, 
        # but (amount+1) will be sufficient in this case
        dp = [amount+1] * (amount+1)
        dp[0] = 0 # for amount 0, take 0 coins
        
        for a in range(1, amount+1):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        
        # if there is no changes in dp array,
        # that mean there are no possible coins to give that amount, so return -1
        if dp[amount] != amount + 1:
            return dp[amount]
        else:
            return -1