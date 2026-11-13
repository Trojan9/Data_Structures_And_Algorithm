# Amazon SDE-I 50, #44: Course Schedule (Medium)  [Graphs]
#
from typing import List

# Brief: Can all courses be finished given prerequisites? (No cycle.)
#
# In plain words: courses with prerequisites form a network of arrows ("A needs B"). You can
# finish everything unless there's a circular dependency (A needs B needs A). Treat it as a graph
# and look for a cycle with DFS, using a "currently visiting" set: if you reach a course that's
# already on your current path, that's a loop.
#
# Why it works: finishing is possible iff the graph is acyclic. The `visiting` set marks nodes on
# the current path; revisiting one means a cycle. Clearing a course's prereqs once proven safe
# stops you re-exploring it, keeping it linear.
#
# Algorithm
# 1. Build adjacency (course → prereqs). 2. DFS; revisiting a path node → cycle. 3. Clear prereqs
#    when proven safe.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visiting = set()
        def dfs(crs):
            if crs in visiting:          # back on the current path → cycle
                return False
            if preMap[crs] == []:
                return True
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)         # leaving this path
            preMap[crs] = []             # proven acyclic → memoise
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

# Complexity: Time O(V + E), Space O(V + E).
# Gotcha: you must remove a course from `visiting` once finished, it's "on the current path", not
# "ever seen".


# ==================== My solution: two sets, `visiting` and `done` ====================
# (Same idea as above. Above, "done" is hidden as `preMap[crs] = []`; here it is its own set,
#  which makes the two states easy to see.)

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # ---------------------------------------------------------------
        # A cycle exists ONLY when, while exploring, we arrive back at a
        # course we are STILL in the middle of checking, one whose
        # prerequisites we haven't finished verifying yet. That course is
        # "visiting". Arriving at a course we've ALREADY fully checked and
        # proven safe ("done") is NOT a cycle, we just reuse the result.
        #
        # So we need two sets:
        #   visiting = courses on the CURRENT path, still being checked
        #   done     = courses fully checked, proven cycle-free
        #
        # Hitting a "visiting" course  -> cycle -> can't finish (False).
        # Hitting a "done" course      -> safe  -> skip, return True.
        # ---------------------------------------------------------------
        courseMap = defaultdict(list)
        for a, b in prerequisites:          # must take b before a
            courseMap[a].append(b)          # a depends on b

        visiting = set()                    # on the current path, still checking
        done = set()                        # fully checked, cycle-free

        def dfs(course):
            if course in visiting:          # looped back to a course still in progress -> cycle
                return False
            if course in done:              # already proven safe -> reuse, don't re-explore
                return True

            visiting.add(course)            # start checking this course
            for pre in courseMap[course]:
                if not dfs(pre):            # a prerequisite led to a cycle -> fail upward
                    return False
            visiting.remove(course)         # finished checking it -> no longer "in progress"
            done.add(course)                # mark it fully checked and safe
            return True

        for c in range(numCourses):
            if c not in done:               # skip courses already proven safe
                if not dfs(c):
                    return False
        return True

# Every course is in ONE of three states:
#
#   not seen yet  --dfs starts-->  visiting  --all prereqs checked-->  done
#                                     |
#                                     +-- reached AGAIN while still visiting  ->  CYCLE
#
#   `visiting` is exactly the courses on the recursion call stack right now.
#
# =====================================================================================
# DRY RUN 1: numCourses = 2, prerequisites = [[1,0],[0,1]]   -> False (cycle)
# =====================================================================================
#
#   courseMap: 1 -> [0],  0 -> [1]          (1 needs 0, 0 needs 1)
#
#   call      what happens                                visiting   done   returns
#   --------  ------------------------------------------  ---------  -----  -------
#   dfs(0)    not visiting/done -> add to visiting        {0}        {}
#     dfs(1)  not visiting/done -> add to visiting        {0,1}      {}
#       dfs(0) 0 is IN visiting (still on the path)                         False
#     dfs(1)  a prereq failed -> fail upward                                False
#   dfs(0)    a prereq failed -> fail upward                                False
#   outer loop: dfs(0) was False -> return False
#
#   The path 0 -> 1 -> 0 came back to a course still in progress = a loop.
#
# =====================================================================================
# DRY RUN 2: why we need `done` and not one "seen" set   -> True
#   numCourses = 4, prerequisites = [[0,1],[0,2],[1,3],[2,3]]
# =====================================================================================
#
#   courseMap: 0 -> [1,2],  1 -> [3],  2 -> [3]
#
#            0               0 needs 1 and 2,
#           / \              1 and 2 both need 3.
#          1   2             3 is reached TWICE, but there is NO cycle
#           \ /              (a diamond, not a loop).
#            3
#
#   call       what happens                               visiting   done        returns
#   ---------  -----------------------------------------  ---------  ----------  -------
#   dfs(0)     start 0                                    {0}        {}
#     dfs(1)   start 1                                    {0,1}      {}
#       dfs(3) start 3, no prereqs                        {0,1,3}    {}
#              finish 3: visiting -> done                 {0,1}      {3}         True
#     dfs(1)   all prereqs ok: finish 1                   {0}        {3,1}       True
#     dfs(2)   start 2                                    {0,2}      {3,1}
#       dfs(3) 3 is in DONE -> safe, skip                                        True
#     dfs(2)   finish 2                                   {0}        {3,1,2}     True
#   dfs(0)     finish 0                                   {}         {3,1,2,0}   True
#   outer loop: c = 1, 2, 3 are already in done -> skipped -> return True
#
#   With ONE "seen" set, reaching 3 the second time (from 2) would look like a cycle
#   and wrongly return False. 3 is not on the current path (0 -> 2) anymore,
#   it was finished earlier. That is why "visiting" (on the path NOW) and
#   "done" (finished, safe) must be different sets.
#
# =====================================================================================
# DRY RUN 3: longer cycle, numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]] -> False
# =====================================================================================
#
#   courseMap: 0 -> [1],  1 -> [2],  2 -> [0]
#
#   dfs(0)  visiting {0}
#   dfs(1)  visiting {0,1}
#   dfs(2)  visiting {0,1,2}
#   dfs(0)  0 IN visiting -> False, passed up through 2, 1, 0 -> answer False
#
#   call stack at the moment of the cycle:   dfs(0) -> dfs(1) -> dfs(2) -> dfs(0)?!
#                                            (visiting = exactly what's on this stack)
#
# Why `visiting.remove(course)` matters: once a course's prerequisites are all checked,
# it leaves the current path. If we left it in `visiting`, the next path to reach it
# (like 3 in dry run 2) would see a fake cycle.
#
# Complexity: Time O(V + E): each course goes visiting -> done once, each edge is
#             followed once (after that the course is in done and returns straight away).
#             Space O(V + E) for the map, the two sets and the call stack.
