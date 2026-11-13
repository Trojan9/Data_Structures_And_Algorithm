# LeetCode 621: Task Scheduler (Medium)  [Greedy / Math, or Heap]
#
from typing import List
from collections import Counter, deque
import heapq

# Problem: each task is a letter and takes 1 unit of time. Two copies of the SAME task must have
# at least n units between them (other tasks or "idle" can fill those units). Tasks can be done in
# any order. What is the minimum total time?
#
#   tasks = ["A","A","A","B","B","B"], n = 2  ->  8      A B idle A B idle A B
#
# What "n apart" means: after doing A at time t, the next A can be at time t + n + 1 at the
# earliest. With n = 2:   A _ _ A _ _ A     (2 slots between every pair of A's)
#
# =============================================================================================
# KEY IDEA: THE MOST FREQUENT TASK DECIDES THE SHAPE OF THE SCHEDULE.
# WRITE THE SCHEDULE AS ROWS OF WIDTH (n + 1). PUT ONE COPY OF THE MOST FREQUENT TASK AT THE
# START OF EACH ROW. EACH ROW IS EXACTLY "A + n GAPS", SO THE A's ARE n APART.
#   -> (maxCount - 1) FULL ROWS of width (n + 1)
#   -> PLUS A LAST ROW that only holds the tasks that ALSO appear maxCount times (maxFreq of them)
#   -> slots = (maxCount - 1) * (n + 1) + maxFreq
# ALL OTHER TASKS FIT INTO THE GAPS. IF THERE ARE MORE TASKS THAN GAPS, THERE ARE NO IDLES AT ALL
# AND THE ANSWER IS JUST len(tasks).  ANSWER = max(slots, len(tasks)).
# =============================================================================================


# =============================================================================================
# Build it up from small examples (the way the video explains it). I = idle.
# =============================================================================================
# First: what is an "interval"?
#   Every unit of time is ONE interval. In each interval the CPU either runs one task or sits
#   IDLE. The answer counts ALL intervals, so:
#
#       answer = (number of tasks) + (number of idles we couldn't avoid)
#
#   Each idle is an interval where the CPU had nothing it was ALLOWED to run (everything left was
#   still cooling down). So every "I" adds 1 to the answer, exactly like a task does.
#
# ---- Example 1: A B C A B C, n = 2  -> 6 ----------------------------------------------------
#       A B C A B C
#   Between the two A's there are B and C: 2 other tasks = n. Same for B and C.
#   No idle needed.  output = 6 = len(tasks)
#
# ---- Example 2: A A A, n = 2  -> 7 ----------------------------------------------------------
#       A I I A I I A
#   Only A exists, so the 2 slots after each A (except the last) MUST be idle.
#   output = 3 tasks + 4 idles = 7
#
# ---- Example 3: A A A B, n = 2  -> 7 --------------------------------------------------------
#       A B I A I I A
#   B goes into one of A's idle slots. It replaces an idle, it doesn't add time.
#   output = 4 tasks + 3 idles = 7      (same 7 as before!)
#
# ---- Example 4: A A A B B C C, n = 2  -> 7 --------------------------------------------------
#       A B C A B C A
#   B, B, C, C fill ALL 4 idle slots.
#   output = 7 tasks + 0 idles = 7      (still 7)
#
# What examples 2, 3 and 4 show: A (the most frequent task) sets the length. Other tasks just
# FILL A's idle slots for free. They never make the schedule longer, until the slots run out.
#
# ---------------------------------------------------------------------------------------------
# WHY THE HIGHEST FREQUENCY?
# ---------------------------------------------------------------------------------------------
# The task with the most copies needs the most cooldowns. A appears 3 times, so there are 2 gaps
# between its copies, and each gap must be at least n long:
#
#       A [n slots] A [n slots] A
#
# No matter what else you have, you can't fit 3 A's into fewer than (3-1)*(n+1) + 1 = 7
# intervals. A task with fewer copies needs fewer gaps, and it fits inside A's gaps. So the
# busiest task is the one that decides the minimum length; the others never stretch it.
#
# ---------------------------------------------------------------------------------------------
# The formulas from the video
# ---------------------------------------------------------------------------------------------
#   idle      = (max_occurring_number - 1) * n
#               the idle slots A's gaps create BEFORE anything else fills them
#               (example 2: (3-1)*2 = 4 idles:  A I I A I I A)
#
#   counter   = how many tasks appear max_occurring_number times (tasks tied for most frequent)
#
#   intervals = (max_occurring_number - 1) * (n + 1) + counter
#               (max - 1) blocks of "A + n slots", then one last block holding every tied task
#
#   Check:  AAABBB, n = 2:   (3-1)*(2+1) + 2 = 8      A B I A B I A B
#           AAA,    n = 2:   (3-1)*(2+1) + 1 = 7      A I I A I I A
#
# ---------------------------------------------------------------------------------------------
# WHY max(intervals, len(tasks))?
# ---------------------------------------------------------------------------------------------
# The formula assumes A's gaps are the limit. But if there are MORE other tasks than slots, the
# extras don't fit in the gaps. Then you just make the gaps wider and keep going: nobody ever has
# to wait, there are 0 idles, and the answer is simply the number of tasks.
#
#   tasks = A B C A B C D E F, n = 2      (A, B, C twice; D, E, F once; 9 tasks)
#   intervals = (2-1)*(2+1) + 3 = 6       <- too small! 9 tasks can't fit in 6 intervals
#   len(tasks) = 9
#
#       A B C D A B C E F      -> 9, no idle, every repeat is >= 3 apart
#
#   answer = max(6, 9) = 9
#
# So:  - if there AREN'T enough tasks to fill the gaps -> idles are left -> the formula is bigger
#      - if there ARE enough (or more) tasks           -> no idles       -> len(tasks) is bigger
# max() picks whichever case you're in. You can never go below len(tasks): every task needs its
# own interval.
#
# Same thing, counting idles directly:
#   idle_left = (max - 1) * n  -  (tasks that fill those slots)
#   answer    = len(tasks) + max(0, idle_left)
# When the fillers outnumber the slots, idle_left goes negative, max(0, ...) makes it 0, and the
# answer is just len(tasks). That's the same max() in a different form.


# ---------------------------------------------------------------------------------------------
# Step 1: build the skeleton from the most frequent task
# ---------------------------------------------------------------------------------------------
# tasks = A A A B B B, n = 2.  Most frequent: A appears 3 times (maxCount = 3).
# Rows have width n + 1 = 3 (one A + 2 gaps). One A per row:
#
#            col 0  col 1  col 2          width = n + 1 = 3
#   row 1:     A      _      _
#   row 2:     A      _      _
#   row 3:     A                          <- LAST row: nothing has to come after the last A
#
#   full rows = maxCount - 1 = 2   (every A except the last one needs n slots after it)
#   last row  = just the final A
#
# Moving down one row in the same column = n + 1 time steps later, so anything placed in the
# same column on different rows is automatically n apart. That's why the rows trick works.
#
# ---------------------------------------------------------------------------------------------
# Step 2: tasks that TIE with the most frequent also go in the last row
# ---------------------------------------------------------------------------------------------
# B also appears 3 times. Put one B in each row, same column:
#
#   row 1:     A      B      _
#   row 2:     A      B      _
#   row 3:     A      B                   <- B also needs a 3rd copy, so the last row grows
#
#   last row length = maxFreq = how many tasks appear maxCount times = 2 (A and B)
#
# ---------------------------------------------------------------------------------------------
# Step 3: count the slots
# ---------------------------------------------------------------------------------------------
#   slots = (maxCount - 1) * (n + 1) + maxFreq
#         =    (3 - 1)    *  (2 + 1) +    2
#         =       2       *     3    +    2     = 8
#
#   the "_" left over are idle:   A B idle A B idle A B   -> 8
#
# ---------------------------------------------------------------------------------------------
# Step 4: why max(slots, len(tasks))
# ---------------------------------------------------------------------------------------------
# Tasks with fewer than maxCount copies never reach the last row; they just fill "_" gaps (one per
# row, same column, so they stay n apart). If there are MORE such tasks than gaps, we simply make
# the rows wider. Then nobody ever waits, there are no idles, and the time is just the number of
# tasks. The formula would undercount in that case, so take the bigger of the two.
#
#   tasks = A A A B C D E F G, n = 2:   slots = 2 * 3 + 1 = 7, but there are 9 tasks
#
#   row 1:     A  B  C  D        <- rows widened, no "_" left
#   row 2:     A  E  F
#   row 3:     A  G ... (any order works as long as the A's are >= 3 apart)
#
#   schedule: A B C D A E F A G   = 9, no idle        -> max(7, 9) = 9
#   (A at times 0, 4, 7: gaps of 4 and 3, both >= n + 1 = 3 ✓)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)                         # task -> how many times it appears
        maxCount = max(counts.values())                 # copies of the most frequent task (rows)
        maxFreq = sum(1 for c in counts.values()        # how many tasks TIE for most frequent
                      if c == maxCount)                 #   (= length of the last row)
        slots = (maxCount - 1) * (n + 1) + maxFreq      # full rows + last row
        return max(slots, len(tasks))                   # if gaps overflow, no idles: just len(tasks)

# Complexity: Time O(total tasks) (counting), Space O(1) (at most 26 letters in the Counter).


# =============================================================================================
# Dry runs
# =============================================================================================
#
# ---- Dry run 1: ["A","A","A","B","B","B"], n = 2  -> 8 ---------------------------------------
#   counts   = {A: 3, B: 3}
#   maxCount = 3                 (A and B both 3)
#   maxFreq  = 2                 (A and B tie)
#   slots    = (3-1)*(2+1) + 2 = 8
#   len      = 6
#   answer   = max(8, 6) = 8
#
#     A B _
#     A B _      ->  A B idle A B idle A B
#     A B
#
# ---- Dry run 2: same tasks, n = 0  -> 6 ------------------------------------------------------
#   n = 0 means no waiting needed at all.
#   slots  = (3-1)*(0+1) + 2 = 4      (rows of width 1 are too narrow for A and B together)
#   len    = 6
#   answer = max(4, 6) = 6            <- the max() is what saves this case
#
# ---- Dry run 3: ["A"]*6 + ["B","C","D","E","F","G"], n = 2  -> 16 ----------------------------
#   counts   = {A: 6, B..G: 1 each}
#   maxCount = 6, maxFreq = 1 (only A)
#   slots    = (6-1)*(2+1) + 1 = 16
#   len      = 12
#   answer   = max(16, 12) = 16
#
#     A B C
#     A D E
#     A F G
#     A _ _          <- ran out of other tasks: 4 idles
#     A _ _
#     A
#   ->  A B C A D E A F G A idle idle A idle idle A   = 16
#
# ---- Dry run 4: ["A","A","A","B","C","D","E","F","G"], n = 2  -> 9 ---------------------------
#   maxCount = 3, maxFreq = 1
#   slots    = (3-1)*(2+1) + 1 = 7
#   len      = 9
#   answer   = max(7, 9) = 9      (more tasks than gaps, so no idle at all; see Step 4)


# ---------------------------------------------------------------------------------------------
# The video's code (same formula, written step by step with a dict and a sorted list)
# ---------------------------------------------------------------------------------------------
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for i in tasks:                          # count each task
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        lst = sorted(d.values(), reverse=True)   # counts, biggest first, e.g. [3, 3] for AAABBB
        max_number = lst[0]                      # the highest frequency

        i = 0
        counter = 0
        while i < len(lst) and lst[i] == max_number:   # how many tasks tie for the highest
            counter += 1
            i += 1

        ret = (max_number - 1) * (n + 1) + counter     # skeleton built around the busiest task
        return max(ret, len(tasks))                    # can't be shorter than doing every task

# Note: in the video the first run failed with "'builtin_function_or_method' object is not
# iterable" because it was written d.values without the (). It must be d.values().
#
# Dry run on AAABBB, n = 2:
#   d = {A: 3, B: 3}    lst = [3, 3]    max_number = 3
#   while: lst[0] == 3 -> counter 1, lst[1] == 3 -> counter 2, i = 2 = len -> stop
#   ret = (3 - 1) * 3 + 2 = 8       max(8, 6) = 8


# ---------------------------------------------------------------------------------------------
# Another way: simulate with a max-heap + cooldown queue (no formula to remember)
# ---------------------------------------------------------------------------------------------
# Each unit of time: run the task with the MOST copies left that isn't cooling down. After running
# it, it can't run again until time + n, so park it in a queue with that time.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-c for c in Counter(tasks).values()]    # max-heap of remaining counts (negated)
        heapq.heapify(heap)
        cooldown = deque()                              # (remaining count, time it's ready again)
        time = 0
        while heap or cooldown:
            time += 1
            if heap:
                c = heapq.heappop(heap) + 1             # run the busiest task once (-3 -> -2)
                if c != 0:                              # copies left -> cool down for n units
                    cooldown.append((c, time + n))
            # (if the heap is empty, this unit is idle)
            if cooldown and cooldown[0][1] == time:     # a task finished cooling down
                heapq.heappush(heap, cooldown.popleft()[0])
        return time

# Complexity: Time O(total time * log 26) = O(total time), Space O(1) (at most 26 tasks).
#
# Dry run on ["A","A","A","B","B","B"], n = 2   (counts shown positive for readability)
#   time | heap before | run  | cooldown after           | back to heap
#   -----+-------------+------+--------------------------+-------------
#     1  | A3 B3       | A    | (A2 ready@3)             |
#     2  | B3          | B    | (A2@3) (B2@4)            |
#     3  | -           | idle | (A2@3) (B2@4)            | A2 (ready at 3)
#     4  | A2          | A    | (B2@4) (A1@6)            | B2
#     5  | B2          | B    | (A1@6) (B1@7)            |
#     6  | -           | idle | (A1@6) (B1@7)            | A1
#     7  | A1          | A    | (B1@7)    (A done)       | B1
#     8  | B1          | B    |           (B done)       |
#   heap and cooldown empty -> return 8
#
# Same 8 as the formula. The formula is O(n) and shorter; the heap version is easier to come up
# with in an interview if you forget the formula, and it shows the actual schedule.
