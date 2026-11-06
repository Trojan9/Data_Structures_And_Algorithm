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
