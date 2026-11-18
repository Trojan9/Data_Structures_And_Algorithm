# 1197. Minimum Knight Moves (Medium, LeetCode premium)
#  + the Amazon SDE-1 (2026, round 3) follow-on: two knights meeting
#
# =====================================================================================
# QUESTION 1: Minimum Knight Moves
# =====================================================================================
# On an INFINITE chessboard (coordinates from -infinity to +infinity), a knight starts at
# square (0, 0). A knight has 8 possible moves: two squares in one direction (up, down,
# left or right) and then one square at a right angle.
#
#        . X . X .
#        X . . . X          X = the 8 squares a knight at K can jump to
#        . . K . .              (±1, ±2) and (±2, ±1)
#        X . . . X
#        . X . X .
#
# Return the minimum number of moves needed to move the knight to square (x, y).
# It is guaranteed the answer exists.
#
# Example 1: x = 2, y = 1  -> 1   [0,0] -> [2,1]
# Example 2: x = 5, y = 5  -> 4   [0,0] -> [2,1] -> [4,2] -> [3,4] -> [5,5]
# Constraints: -300 <= x, y <= 300, 0 <= |x| + |y| <= 300
#
# =====================================================================================
# QUESTION 2 (Amazon SDE-1 interview, round 3): two knights
# =====================================================================================
# Two knights are placed on an infinite chessboard at given starting squares A and B.
# Both move with normal knight moves, and they take turns. Find the minimum TOTAL number
# of moves (both knights added together) for them to end up on the same square.
#
# -> Solution 3 below. Short answer: it equals the knight distance from A to B.
#
# =====================================================================================
# KEY IDEA
# =====================================================================================
# Every square is a node, every knight jump is an edge, and every edge costs 1 move.
# "Fewest moves" on equal-cost edges = BFS (the first time BFS reaches a square,
# it is with the fewest moves).
#
# The board is INFINITE, so plain BFS could wander off in directions that never
# help. We put a fence around the search:
#   - Solution 1: a box around the origin and the target, plus 2 extra squares per side
#   - Solution 2: fold the target into the top-right quadrant with abs() and only
#                 fence the bottom-left (>= -2)
# =====================================================================================

from collections import deque


# =====================================================================================
# SOLUTION 1: BFS inside a box (no abs)
# =====================================================================================
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        moves = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
        # a margin of 2 around the rectangle spanning origin and target
        x_lo, x_hi = min(0, x) - 2, max(0, x) + 2
        y_lo, y_hi = min(0, y) - 2, max(0, y) + 2
        q = deque([(0, 0, 0)])                 # (x, y, moves so far), start at the origin
        seen = {(0, 0)}                        # squares already put in the queue
        while q:
            cx, cy, d = q.popleft()
            if (cx, cy) == (x, y):             # first time we reach it = fewest moves
                return d
            for dx, dy in moves:               # try all 8 knight jumps
                nx, ny = cx + dx, cy + dy
                if (nx, ny) not in seen and x_lo <= nx <= x_hi and y_lo <= ny <= y_hi:
                    seen.add((nx, ny))         # mark when QUEUED, so it's never queued twice
                    q.append((nx, ny, d + 1))
        return -1                              # never happens: every square is reachable

# -------------------------------------------------------------------------------------
# ILLUSTRATION: the box for target (-3, 2)
# -------------------------------------------------------------------------------------
# (a negative x on purpose, so you can see why min/max are needed)
#
#   x_lo = min(0, -3) - 2 = -3 - 2 = -5
#   x_hi = max(0, -3) + 2 =  0 + 2 =  2
#   y_lo = min(0,  2) - 2 =  0 - 2 = -2
#   y_hi = max(0,  2) + 2 =  2 + 2 =  4
#
#           x:  -5  -4  -3  -2  -1   0   1   2
#             +---------------------------------+
#     y =  4  |  .   .   .   .   .   .   .   .  |  <- y_hi = 4  (+2 above the target)
#     y =  3  |  .   .   .   .   .   .   .   .  |
#     y =  2  |  .   .   T   .   .   .   .   .  |  <- target T = (-3, 2)
#     y =  1  |  .   .   .   .   .   .   .   .  |
#     y =  0  |  .   .   .   .   .   O   .   .  |  <- origin O = (0, 0)
#     y = -1  |  .   .   .   .   .   .   .   .  |
#     y = -2  |  .   .   .   .   .   .   .   .  |  <- y_lo = -2 (-2 below the origin)
#             +---------------------------------+
#                ^                           ^
#             x_lo = -5                   x_hi = 2
#         (-2 left of target)        (+2 right of origin)
#
# The BFS is only allowed to step on squares inside this rectangle.
# Reading the formula onto the picture:
#   - min(0, x) = the leftmost of {origin at 0, target at -3} = -3,
#     then -2 pushes the left wall out to -5.
#   - max(0, x) = the rightmost of {0, -3} = 0, then +2 pushes the right wall to 2.
#   - Same for y: min(0, y) finds the bottom, max(0, y) the top, each padded by 2.
#
# So the box is simply the smallest rectangle that contains BOTH the origin and the
# target, grown by 2 squares on every side.
#
# Why min/max of 0 and the target: they make the box stretch towards wherever the
# target is. Target up-right -> max extends that way; down-left (like here) -> min
# extends that way. Using 0 as the other corner always keeps the origin inside too.
#
# What BFS actually does inside that box: the number of moves to reach each square,
# spreading out from O in rings (1s first, then 2s, then 3s ...):
#
#           x:  -5  -4  -3  -2  -1   0   1   2
#     y =  4  |  3   4   3   2   3   2   3   2
#     y =  3  |  4   3   2   3   2   3   2   3
#     y =  2  |  3   2  [3]  4   1   2   1   4      [3] = target (-3, 2): 3 moves
#     y =  1  |  4   3   2   1   2   3   2   1
#     y =  0  |  3   2   3   2   3   0   3   2      0 = origin
#     y = -1  |  4   3   2   1   2   3   2   1
#     y = -2  |  3   2   3   4   1   2   1   4
#
#   One shortest path: (0,0) -> (-2,-1) -> (-4,0) -> (-3,2)
#   It goes BELOW the origin (y = -1) and LEFT of the target (x = -4), outside the
#   plain origin-to-target rectangle. That is what the margin is for.
#
# Why the +2 / -2 margin: a shortest knight path can step just outside the direct
# origin-to-target rectangle (by a square or two) before curving back. The 2-square
# padding makes sure the fence never cuts off a shortest path, while still keeping
# the search finite.
#
#   Margin 1 is NOT enough. Target (-1, 0) needs 3 moves:
#       (0,0) -> (-2,1) -> (0,2) -> (-1,0)
#   (0, 2) has y = 2. With margin 1, y_hi = max(0, 0) + 1 = 1, so (0, 2) is fenced
#   off and the BFS returns a longer answer. (I checked margin 2 against an unfenced
#   BFS for every target from -12 to 12 in both x and y: always the same answer.
#   Margin 1 fails for (-1,0), (-2,0), (0,-1), (0,-2), ...)
#
# DRY RUN: target (2, 1)   box x: -2..4, y: -2..3
#   queue: (0,0,0)          pop (0,0): not target. push its 8 jumps (all inside the box)
#                           with d = 1: (1,2) (2,1) (-1,2) (-2,1) (1,-2) (2,-1) (-1,-2) (-2,-1)
#   pop (1,2,1): not target, push its unseen in-box jumps with d = 2 ...
#   pop (2,1,1): target -> return 1
#
# Complexity (Solution 1):
#   The BFS can only visit squares inside the box: (|x| + 5) * (|y| + 5) squares.
#   Time:  O(|x| * |y|)   each square is queued at most once, 8 jumps checked each
#          (for a target on an axis, e.g. (300, 0), the box is thin, so it's O(|x| + |y|))
#   Space: O(|x| * |y|)   the seen set and the queue


# =====================================================================================
# SOLUTION 2: fold with abs(), then fence only one side
# =====================================================================================
class SolutionAbs:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)                  # fold the target into the top-right quadrant
        moves = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
        q = deque([(0, 0, 0)])
        seen = {(0, 0)}
        while q:
            cx, cy, d = q.popleft()
            if (cx, cy) == (x, y):
                return d
            for dx, dy in moves:
                nx, ny = cx + dx, cy + dy
                if (nx, ny) not in seen and nx >= -2 and ny >= -2:   # one-sided fence
                    seen.add((nx, ny))
                    q.append((nx, ny, d + 1))
        return -1

# Why abs() is allowed: the board is symmetric. Flip the board left-right and the
# knight moves are still the same 8 moves, so the distance to (x, y), (-x, y),
# (x, -y) and (-x, -y) is identical. Folding into one quadrant loses nothing.
#
#   (-3, 2)  --abs-->  (3, 2)      both need 3 moves
#
# abs() isn't cosmetic: it's what lets the fence be ONE-sided (>= -2). Without the
# fold you must fence the whole origin-to-target box like Solution 1.
#
# Which one searches less? I measured it (squares put into `seen` before finding the
# target):
#
#   target       box (Solution 1)   abs (Solution 2)
#   (5, 5)       90                 112
#   (-3, 2)      52                 75
#   (50, 50)     3,023              4,461
#   (2, 112)     801                11,656
#   (300, 0)     1,519              81,091
#
#   The abs version has NO upper fence, so it spreads in a growing ring until it hits
#   the target. The box fences all 4 sides, so it searches FEWER squares, a lot fewer
#   for long thin targets. abs() buys simpler code, not a smaller search.
#   (You can combine them: fold with abs(), then use the box -2 .. x+2 and -2 .. y+2.)
#
# Complexity (Solution 2):
#   The BFS reaches distance d ~ max(|x|, |y|) / 2 moves, and visits roughly every
#   square in the quadrant within that many moves.
#   Time:  O(max(|x|, |y|)^2)
#   Space: O(max(|x|, |y|)^2)


# =====================================================================================
# SOLUTION 3: two knights at A and B, fewest TOTAL moves to land on the same square
# =====================================================================================
def knightDistance(ax, ay, bx, by):
    moves = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
    # bounding box around BOTH points, padded by 2 on every side
    x_lo, x_hi = min(ax, bx) - 2, max(ax, bx) + 2
    y_lo, y_hi = min(ay, by) - 2, max(ay, by) + 2
    q = deque([(ax, ay, 0)])          # start at A, distance 0
    seen = {(ax, ay)}
    while q:
        cx, cy, d = q.popleft()
        if (cx, cy) == (bx, by):      # reached B
            return d
        for dx, dy in moves:
            nx, ny = cx + dx, cy + dy
            if (nx, ny) not in seen and x_lo <= nx <= x_hi and y_lo <= ny <= y_hi:
                seen.add((nx, ny))
                q.append((nx, ny, d + 1))
    return -1

# What changed from Solution 1:
#   - Start the queue at A, not (0, 0).
#   - The target is B as given.
#   - The box is min/max of A and B (not of 0 and the target), padded by 2.
#
# WHY is "two knights meet" the same as "one knight goes from A to B"?
#
#   Take a shortest path from A to B, length d:
#
#       A = p0 -> p1 -> p2 -> ... -> p(d-1) -> pd = B
#
#   Knight A walks it forwards from the start, knight B walks it backwards from the
#   end. Every knight move can be undone by the opposite knight move, so walking it
#   backwards is fine. They take turns (A, B, A, B, ...), so after d moves in total:
#       A has made ceil(d / 2) moves  -> stands on p(ceil(d/2))
#       B has made floor(d / 2) moves -> stands on p(d - floor(d/2)) = p(ceil(d/2))
#   Same square. So they can always meet in d total moves.
#
#   And they can't do it in fewer: if they met after t total moves, then A's moves
#   followed by B's moves played backwards is a path from A to B of length t, so
#   t >= d.
#
#   => answer = knight distance between A and B = one BFS from A to B.
#
#   (Shift-to-origin version of the same idea: the distance from A to B equals
#    Solution 1/2 called with the difference: minKnightMoves(bx - ax, by - ay).
#    Moving both knights by the same amount doesn't change anything.)
#
# DRY RUN 1: A = (3,3), B = (5,4)
#   Box: x_lo = 1, x_hi = 7, y_lo = 1, y_hi = 6.
#   BFS from (3,3): try all 8 moves; (3,3) -> (5,4) is a (+2,+1) knight move
#   -> queued with d = 1, popped -> reached B at d = 1. ✓
#   Meaning: knight A makes one move onto B's square. Total moves = 1.
#
# DRY RUN 2: A = (0,0), B = (1,1)
#   (1,1) is next to (0,0) diagonally, which no single knight move reaches.
#   BFS: d = 1 ring from (0,0): (1,2) (2,1) (-1,2) (-2,1) (1,-2) (2,-1) (-1,-2) (-2,-1)
#        none is (1,1). d = 2: from (2,-1), the move (-1,+2) lands on (1,1). -> 2
#   Path: (0,0) -> (2,-1) -> (1,1)
#   Meeting: A moves (0,0) -> (2,-1); then B moves (1,1) -> (2,-1). Same square,
#   total 2 moves (1 each). ✓
#
# Complexity (Solution 3): same as Solution 1 with the box around A and B:
#   Time:  O(|bx - ax| * |by - ay|)   (O(|bx-ax| + |by-ay|) when the box is thin)
#   Space: O(|bx - ax| * |by - ay|)
#
# All three are valid: abs() fold (simplest fence), shift-to-origin, or this direct
# box BFS. The direct box BFS is the easiest to explain in an interview: no
# reflection trick, just BFS inside a box around the two squares.


if __name__ == "__main__":
    import random

    def unfenced(ax, ay, bx, by):
        moves = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
        q = deque([(ax, ay, 0)]); seen = {(ax, ay)}
        while q:
            cx, cy, d = q.popleft()
            if (cx, cy) == (bx, by):
                return d
            for dx, dy in moves:
                n = (cx + dx, cy + dy)
                if n not in seen:
                    seen.add(n); q.append((*n, d + 1))

    for x in range(-10, 11):
        for y in range(-10, 11):
            want = unfenced(0, 0, x, y)
            assert Solution().minKnightMoves(x, y) == want
            assert SolutionAbs().minKnightMoves(x, y) == want
    for _ in range(1000):
        a = [random.randint(-8, 8) for _ in range(4)]
        assert knightDistance(*a) == unfenced(*a)
    print(Solution().minKnightMoves(2, 1), Solution().minKnightMoves(5, 5),
          Solution().minKnightMoves(-3, 2), knightDistance(3, 3, 5, 4), knightDistance(0, 0, 1, 1))
