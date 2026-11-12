There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

 

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

####### SOLUTION ##########################

Greedy Approach (Optimal)
Idea:
-Traverse stations from left to right

-Keep track of tank += gas[i] - cost[i]

-If tank drops below 0, you can’t start from that range, so:

- reset tank to 0

- move start to i + 1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #get total gas also..if total is greater than or equal 0 , then the trip can be made
        total_gas = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            #get gain
            gain = gas[i] - cost[i]
          
            #add them all to get total gas used
            total_gas += gain
          
            #keep track of the tank
            tank += gain

            #if the present tank is less than 0, means we cannot start at the present start point..move it forward
            if tank < 0:
                start = i + 1
                tank = 0  # reset tank and try from the next station
              
        #if total gas left at the end is >= 0 , then the trip can be made i.e no matter where we start, the total gas left will be same
        return start if total_gas >= 0 else -1


# =============================================================================================
# Dry runs
# =============================================================================================
# gain = gas[i] - cost[i] = what you're left with after filling up at i and driving to i + 1.
#   tank       = gas in the car since the CURRENT start (reset when it goes negative)
#   total_gas  = sum of ALL gains, never reset (is there enough gas in the whole circle?)
#
# ---------------------------------------------------------------------------------------------
# Dry run 1: gas = [1,2,3,4,5], cost = [3,4,5,1,2]   -> expected 3
# ---------------------------------------------------------------------------------------------
#   gain = [1-3, 2-4, 3-5, 4-1, 5-2] = [-2, -2, -2, 3, 3]
#
#   i | gain | total_gas | tank (after +gain) | tank < 0?  | start | tank after
#   --+------+-----------+--------------------+------------+-------+-----------
#   0 |  -2  |    -2     |  0 + -2 = -2       | yes, reset |   1   |    0
#   1 |  -2  |    -4     |  0 + -2 = -2       | yes, reset |   2   |    0
#   2 |  -2  |    -6     |  0 + -2 = -2       | yes, reset |   3   |    0
#   3 |   3  |    -3     |  0 +  3 =  3       | no         |   3   |    3
#   4 |   3  |     0     |  3 +  3 =  6       | no         |   3   |    6
#
#   total_gas = 0 >= 0  -> return start = 3
#
#   Check: start at 3: tank 4-1 = 3, +5-2 = 6, +1-3 = 4, +2-4 = 2, +3-5 = 0. Never negative. ✓
#
# ---------------------------------------------------------------------------------------------
# Dry run 2: gas = [2,3,4], cost = [3,4,3]   -> expected -1
# ---------------------------------------------------------------------------------------------
#   gain = [-1, -1, 1]
#
#   i | gain | total_gas | tank      | tank < 0?  | start
#   --+------+-----------+-----------+------------+------
#   0 |  -1  |    -1     | -1        | yes, reset |   1
#   1 |  -1  |    -2     | -1        | yes, reset |   2
#   2 |   1  |    -1     |  1        | no         |   2
#
#   total_gas = -1 < 0  -> return -1
#   (start ended at 2, but it doesn't matter: the whole circle uses more gas than it gives,
#    so NO start can work)
#
# ---------------------------------------------------------------------------------------------
# Dry run 3 (tank goes up, then fails later): gas = [5,1,2,3,4], cost = [4,4,1,5,1] -> expected 4
# ---------------------------------------------------------------------------------------------
#   gain = [1, -3, 1, -2, 3]
#
#   i | gain | total_gas | tank          | tank < 0?  | start
#   --+------+-----------+---------------+------------+------
#   0 |   1  |     1     | 0 + 1 = 1     | no         |   0
#   1 |  -3  |    -2     | 1 - 3 = -2    | yes, reset |   2    <- jump PAST 1, not to 1
#   2 |   1  |    -1     | 0 + 1 = 1     | no         |   2
#   3 |  -2  |    -3     | 1 - 2 = -1    | yes, reset |   4    <- jump PAST 3
#   4 |   3  |     0     | 0 + 3 = 3     | no         |   4
#
#   total_gas = 0 >= 0  -> return 4
#
#   Check: start at 4: tank 4-1 = 3, +5-4 = 4, +1-4 = 1, +2-1 = 2, +3-5 = 0. Never negative. ✓
#
# =============================================================================================
# The two questions this dry run answers
# =============================================================================================
# 1. Why jump start to i + 1, skipping every station between the old start and i?
#    At i = 1 above we started at 0 and failed. Could starting at 1 work instead? No:
#    we ARRIVED at station 1 with tank = 1 (>= 0) and still failed. Starting fresh at 1 means
#    arriving with tank = 0, which is even less gas, so it fails too. The same holds for every
#    station between start and i: we always reached them with tank >= 0, so starting there
#    (with 0) can only be worse. Hence: skip them all, try i + 1.
#
# 2. Why only check total_gas at the end, not go around the circle again?
#    If total_gas >= 0, the whole circle gives at least as much gas as it costs. The stretch
#    from `start` to the end never went negative, and the stretch before `start` (0..start-1)
#    is exactly the part with the deficits we reset on; the surplus from start..end covers them
#    because the grand total is >= 0. So one pass is enough. If total_gas < 0, no start works.
#
# Complexity: Time O(n) (one pass), Space O(1).
