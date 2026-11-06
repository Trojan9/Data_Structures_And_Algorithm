# Amazon SDE-I 50, #50: Coin Change (Medium)  [Dynamic Programming]
#
from typing import List

# Brief: Fewest coins to make an amount, or -1. `[1,2,5], 11` → `3`.
#
# In plain words: fewest coins to total the amount. Work out the fewest for every amount from 0 up
# to the target. For an amount, try each coin: using it leaves "amount − coin", already solved, so
# that option costs `1 + dp[amount − coin]`. Take the best. Start with "0 coins make 0".
#
# Why it works: the last coin used leaves a smaller amount whose best answer you already computed
# (optimal substructure). Building from small amounts up means every lookup is ready. The sentinel
# `amount + 1` means "unreachable" (no real answer exceeds `amount` coins).
#
# Algorithm
# 1. `dp` size amount+1 filled with sentinel, `dp[0]=0`. 2. For each `a`, for each coin ≤ a,
#    `dp[a] = min(dp[a], 1 + dp[a-coin])`. 3. Return `dp[amount]` or -1.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)      # amount+1 = "infinity" sentinel
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1

# Complexity: Time O(amount · coins), Space O(amount).
