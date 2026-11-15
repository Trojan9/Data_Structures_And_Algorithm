# Amazon SDE-I 50, #50: Coin Change (Medium)  [Dynamic Programming]
#
from typing import List

# Brief: Fewest coins to make an amount, or -1. `[1,2,5], 11` → `3`.
#
# ---------------------------------------------------------------------------------------------
# Intuition (bottom-up DP)
# ---------------------------------------------------------------------------------------------
# Instead of asking "how many coins to make this amount?" recursively, build the answers from
# small amounts up to the big one.
#
# Key idea:
#   - If we already know the fewest coins to make (a - coin),
#   - then we can make a with just ONE more coin (that coin).
#
# So every amount depends only on smaller amounts that are already solved. Try every coin as
# "the last coin used" and keep the best: dp[a] = min over coins of 1 + dp[a - coin].
#
# Why it works: whatever the best way to make a is, it has some last coin c. Remove it and what's
# left is a - c, which must itself be made in the fewest coins (otherwise we could do better).
# That's "optimal substructure". Going from 1 upwards means dp[a - c] is always ready when we need
# it.
#
# The sentinel amount + 1 means "not reachable (yet)". No real answer can be bigger than amount
# (the worst case is all 1-coins), so amount + 1 works as "infinity".
#
# ---------------------------------------------------------------------------------------------
# Algorithm
# ---------------------------------------------------------------------------------------------
# 1. Make a dp array of size amount + 1, where dp[a] = fewest coins to make amount a.
# 2. Initialise:
#      dp[0] = 0              (0 coins make amount 0)
#      everything else = amount + 1   ("infinity" / not reachable yet)
# 3. For every amount a from 1 to amount:
#      for each coin c:
#        if a - c >= 0        (the coin isn't bigger than the amount)
#          dp[a] = min(dp[a], 1 + dp[a - c])
# 4. If dp[amount] is still amount + 1, it can't be made: return -1.
# 5. Otherwise return dp[amount].

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)      # amount+1 = "infinity" sentinel
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1

# Complexity: Time O(amount · coins) (every amount tries every coin), Space O(amount) (dp array).

# ---------------------------------------------------------------------------------------------
# Dry run 1: coins = [1, 2, 5], amount = 6
# ---------------------------------------------------------------------------------------------
# dp[a] = fewest coins to make amount a. Sentinel 7 (= amount + 1) means "not reachable yet".
# The coins are always 1, 2, 5. A coin is SKIPPED for an amount when a - coin < 0 (the coin is
# bigger than the amount), so coin 5 does nothing until a reaches 5.
#
#   setup:  dp = [0, 7, 7, 7, 7, 7, 7]      dp[0] = 0, the rest = infinity
#                 0  1  2  3  4  5  6       <- index = amount
#
#   a = 1:  coin 1 -> 1 + dp[0] = 1   -> dp[1] = 1
#           coin 2 -> skipped (1 - 2 < 0)
#           coin 5 -> skipped (1 - 5 < 0)
#           dp = [0, 1, 7, 7, 7, 7, 7]
#
#   a = 2:  coin 1 -> 1 + dp[1] = 2   -> dp[2] = 2
#           coin 2 -> 1 + dp[0] = 1   -> dp[2] = 1   (better: one 2-coin)
#           coin 5 -> skipped (2 - 5 < 0)
#           dp = [0, 1, 1, 7, 7, 7, 7]
#
#   a = 3:  coin 1 -> 1 + dp[2] = 2   -> dp[3] = 2
#           coin 2 -> 1 + dp[1] = 2   (not better, stays 2)
#           coin 5 -> skipped (3 - 5 < 0)
#           dp = [0, 1, 1, 2, 7, 7, 7]
#
#   a = 4:  coin 1 -> 1 + dp[3] = 3   -> dp[4] = 3
#           coin 2 -> 1 + dp[2] = 2   -> dp[4] = 2   (two 2-coins)
#           coin 5 -> skipped (4 - 5 < 0)
#           dp = [0, 1, 1, 2, 2, 7, 7]
#
#   a = 5:  coin 1 -> 1 + dp[4] = 3   -> dp[5] = 3
#           coin 2 -> 1 + dp[3] = 3   (not better)
#           coin 5 -> 1 + dp[0] = 1   -> dp[5] = 1   (coin 5 finally fits)
#           dp = [0, 1, 1, 2, 2, 1, 7]
#
#   a = 6:  coin 1 -> 1 + dp[5] = 2   -> dp[6] = 2
#           coin 2 -> 1 + dp[4] = 3   (not better)
#           coin 5 -> 1 + dp[1] = 2   (ties, stays 2)
#           dp = [0, 1, 1, 2, 2, 1, 2]
#
#   return dp[6] = 2   (5 + 1)
#
# How to tell a coin was skipped: look at a - coin. If it's negative, that coin can't be used for
# that amount, so `if a - c >= 0` is false and it isn't even tried. Coin 5 is skipped at
# a = 1, 2, 3, 4 and first usable at a = 5.

# ---------------------------------------------------------------------------------------------
# Dry run 2: coins = [1, 2, 5], amount = 11   (the classic example, sentinel = 12)
# ---------------------------------------------------------------------------------------------
# Each column is "1 + dp[a - coin]" for that coin ("-" = skipped). dp[a] is the smallest.
#
#    a  | coin 1         | coin 2         | coin 5         | dp[a] | best way
#   ----+----------------+----------------+----------------+-------+-----------
#    0  |                |                |                |   0   | (nothing)
#    1  | 1+dp[0]  = 1   |       -        |       -        |   1   | 1
#    2  | 1+dp[1]  = 2   | 1+dp[0] = 1    |       -        |   1   | 2
#    3  | 1+dp[2]  = 2   | 1+dp[1] = 2    |       -        |   2   | 2+1
#    4  | 1+dp[3]  = 3   | 1+dp[2] = 2    |       -        |   2   | 2+2
#    5  | 1+dp[4]  = 3   | 1+dp[3] = 3    | 1+dp[0] = 1    |   1   | 5
#    6  | 1+dp[5]  = 2   | 1+dp[4] = 3    | 1+dp[1] = 2    |   2   | 5+1
#    7  | 1+dp[6]  = 3   | 1+dp[5] = 2    | 1+dp[2] = 2    |   2   | 5+2
#    8  | 1+dp[7]  = 3   | 1+dp[6] = 3    | 1+dp[3] = 3    |   3   | 5+2+1
#    9  | 1+dp[8]  = 4   | 1+dp[7] = 3    | 1+dp[4] = 3    |   3   | 5+2+2
#   10  | 1+dp[9]  = 4   | 1+dp[8] = 4    | 1+dp[5] = 2    |   2   | 5+5
#   11  | 1+dp[10] = 3   | 1+dp[9] = 4    | 1+dp[6] = 3    |   3   | 5+5+1
#
#   final dp = [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]   -> return dp[11] = 3
#
# Notice a = 11 reuses a = 10 (5+5) and a = 6 (5+1): the big answer is built entirely from
# small answers already in the table. That's the whole point of DP.

# ---------------------------------------------------------------------------------------------
# Dry run 3: impossible case, coins = [2], amount = 3   (sentinel = 4)
# ---------------------------------------------------------------------------------------------
#   setup:  dp = [0, 4, 4, 4]
#   a = 1:  coin 2 -> skipped (1 - 2 < 0)          dp[1] stays 4
#   a = 2:  coin 2 -> 1 + dp[0] = 1                dp[2] = 1
#   a = 3:  coin 2 -> 1 + dp[1] = 1 + 4 = 5        min(4, 5) = 4, dp[3] stays 4
#   dp[3] == 4 == sentinel  -> return -1
#
# Note: "1 + sentinel" is always bigger than the sentinel, so building on an unreachable amount
# can never make dp[a] look reachable. min() just keeps the sentinel.



















from collections import deque

def coinChange(coins, amount):
    # q holds states to explore, each a tuple (total_so_far, coins_used).
    # Start at total 0 having used 0 coins.
    q = deque([(0, 0)])

    # visited = totals we've already queued, so we never explore the same
    # total twice. Seed it with 0 (our start), already queued.
    visited = {0}

    # BFS loop: keep going while there are states left to explore.
    while q:
        # Take the oldest state (FIFO). BFS explores in order of coins_used,
        # so the first time we reach 'amount' it's with the fewest coins.
        total, count = q.popleft()

        # If this total is exactly the target, 'count' is the minimum number
        # of coins needed (because of BFS order) -> return it.
        if total == amount:
            return count

        # Otherwise, try adding each coin to the current total.
        for coin in coins:
            new_total = total + coin

            # Only queue new_total if it doesn't overshoot the target AND we
            # haven't already queued it (that would be wasted, repeat work).
            if new_total <= amount and new_total not in visited:
                visited.add(new_total)            # mark as queued (on enqueue!)
                q.append((new_total, count + 1))  # one more coin used

    # Queue emptied without ever hitting 'amount' -> it can't be made.
    return -1


# =============================================================================
# EXPLANATION
# -----------------------------------------------------------------------------
# The "graph" is invisible. Each total (0,1,2,...,amount) is a node. Adding a
# coin is an edge from total -> total + coin, and every edge costs the same:
# one coin. So "fewest coins to reach amount" = "shortest path from 0 to amount
# in an unweighted graph" = exactly what BFS solves.
#
# Why BFS gives the minimum: BFS explores all totals reachable with 1 coin,
# then all with 2 coins, then 3, level by level. So the FIRST time 'amount'
# comes out of the queue, it was reached with the fewest coins -> return count.
#
# Why 'visited' matters: many coin sequences land on the same total (1+2 and
# 2+1 both reach 3). Without visited you'd re-explore the same total over and
# over. Marking it the moment you enqueue guarantees each total is queued once.
#
# Why new_total <= amount: coins are positive, so once you pass the target you
# can never come back to it -> those states are dead ends, skip them.
#
# Why return -1: if the queue drains and 'amount' was never dequeued, no
# combination of coins can make it.
#
# Complexity: Time O(amount * len(coins)), Space O(amount).
# =============================================================================


# =============================================================================
# DRY RUN: coins = [1,2,5], amount = 6   (state = (total, count))
# -----------------------------------------------------------------------------
# Start:        q = [(0,0)]            visited = {0}
#
# Pop (0,0): 0 != 6. Add coins to 0:
#   0+1=1 -> queue (1,1)   visited {0,1}
#   0+2=2 -> queue (2,1)   visited {0,1,2}
#   0+5=5 -> queue (5,1)   visited {0,1,2,5}
#   q = [(1,1),(2,1),(5,1)]
#
# Pop (1,1): 1 != 6. From 1:
#   1+1=2 -> in visited, skip
#   1+2=3 -> queue (3,2)   visited +3
#   1+5=6 -> queue (6,2)   visited +6
#   q = [(2,1),(5,1),(3,2),(6,2)]
#
# Pop (2,1): 2 != 6. From 2:
#   2+1=3 -> visited, skip
#   2+2=4 -> queue (4,2)   visited +4
#   2+5=7 -> 7 > 6, skip
#   q = [(5,1),(3,2),(6,2),(4,2)]
#
# Pop (5,1): 5 != 6. From 5:
#   5+1=6 -> visited, skip
#   5+2=7 -> >6 skip ; 5+5=10 -> >6 skip
#   q = [(3,2),(6,2),(4,2)]
#
# Pop (3,2): 3 != 6. From 3: 4 visited, 5 visited, 8>6 -> nothing new.
#   q = [(6,2),(4,2)]
#
# Pop (6,2): total 6 == amount -> RETURN 2  ✅
#
# Answer: 2 coins (that path was 1 + 5, found at count 2). BFS returned it the
# moment it surfaced. Note visited kept totals like 2, 3, 6 queued only once.
# =============================================================================
