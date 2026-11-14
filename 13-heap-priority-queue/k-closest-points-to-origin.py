# 973. K Closest Points to Origin (Medium)
#
# QUESTION
# Given an array points where points[i] = [x_i, y_i] is a point on the 2D plane,
# and an integer k, return the k points closest to the origin (0, 0).
# Distance is the Euclidean distance sqrt(x^2 + y^2). Return the answer in any order.
#
# Example 1: points = [[1,3],[-2,2]], k = 1  -> [[-2,2]]
# Example 2: points = [[3,3],[5,-1],[-2,4]], k = 2 -> [[3,3],[-2,4]] (any order)
# Constraints: 1 <= k <= points.length <= 10^4, -10^4 <= x_i, y_i <= 10^4.

import heapq
import math


# =====================================================================================
# SOLUTION 1 (mine): compute every distance, sort, take the first k
# =====================================================================================
class Solution:
    def kClosest(self, points, k):
        res = []                                  # the k closest points we'll return
        sqr_res = []                              # list of (distance, original index)

        # work out the distance from the origin for every point
        for i in range(len(points)):
            # distance = sqrt(x^2 + y^2); points[i][0] is x, points[i][1] is y
            sqrt_res = math.sqrt((points[i][0] ** 2) + (points[i][1] ** 2))
            sqr_res.append((sqrt_res, i))         # store the distance with the point's index

        # sort by distance (smallest first)
        sqr_res.sort(key=lambda x: x[0])

        # take the first k entries, look up their original points by index
        for r in range(k):
            res.append(points[sqr_res[r][1]])     # sqr_res[r][1] is the stored index

        return res


# EXPLANATION
# Idea: the k closest points are just the k with the smallest distance to the
# origin. So compute every point's distance, pair it with the point's index,
# sort by distance, and take the first k.
#
# - Pair distance with index so that after sorting we can still find which
#   original point each distance belonged to (sqr_res[r][1] is that index).
# - Sorting puts the smallest distances first, so the first k are the answer.
# - (Optional) you don't actually need sqrt: x*x + y*y orders points the same
#   way, so you could skip math.sqrt and the floating point entirely.
#   (If a < b then sqrt(a) < sqrt(b), so the ORDER never changes, only the numbers.)
#
# COMPLEXITY
# Time: O(n log n)  -> one pass to build the list is O(n), the sort is O(n log n)
#                      which dominates, taking the first k is O(k) <= O(n).
# Space: O(n)       -> sqr_res stores one (distance, index) tuple per point.
#
# DRY RUN (Example 2): points = [[3,3],[5,-1],[-2,4]], k = 2
#
#   i  point    x^2 + y^2     sqrt     sqr_res after append
#   -  -------  ------------  -------  ------------------------------------
#   0  [3,3]    9 + 9  = 18   4.24     [(4.24, 0)]
#   1  [5,-1]   25 + 1 = 26   5.10     [(4.24, 0), (5.10, 1)]
#   2  [-2,4]   4 + 16 = 20   4.47     [(4.24, 0), (5.10, 1), (4.47, 2)]
#
#   sort by distance  -> [(4.24, 0), (4.47, 2), (5.10, 1)]
#   take first k = 2  -> indexes 0 and 2 -> points[0] = [3,3], points[2] = [-2,4]
#   answer: [[3,3], [-2,4]]
#
#   (Without sqrt: 18, 26, 20 -> sorted 18, 20, 26 -> same indexes 0, 2.)


# =====================================================================================
# BETTER FOLLOW-UP (say this out loud)
# =====================================================================================
# Since only the k smallest are needed, a size-k max-heap does it in
# O(n log k) time, O(k) space, better when k is much smaller than n:
#     import heapq
#     return heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)


class SolutionNSmallest:
    def kClosest(self, points, k):
        return heapq.nsmallest(k, points, key=lambda p: p[0] ** 2 + p[1] ** 2)


# The same size-k max-heap written out by hand (what nsmallest does for you):
#
#   Python's heapq is a MIN-heap, so store the NEGATIVE distance -> the top (heap[0])
#   is the FARTHEST of the k points we are keeping.
#   - Push every point.
#   - If the heap has more than k points, pop the top = throw away the farthest.
#   - At the end the heap holds exactly the k closest.
class SolutionMaxHeap:
    def kClosest(self, points, k):
        heap = []                                     # (-distance, x, y), at most k items
        for x, y in points:
            heapq.heappush(heap, (-(x * x + y * y), x, y))
            if len(heap) > k:                         # one too many
                heapq.heappop(heap)                   # drop the farthest (most negative)
        return [[x, y] for _, x, y in heap]

# DRY RUN (Example 2, max-heap): k = 2, distances [3,3]=18, [5,-1]=26, [-2,4]=20
#
#   point    push              heap (as distances kept)   size > k?   pop
#   -------  ----------------  -------------------------  ----------  ----------
#   [3,3]    -18               {18}                       no
#   [5,-1]   -26               {18, 26}                   no
#   [-2,4]   -20               {18, 26, 20}               yes         26 (farthest)
#   end                        {18, 20} -> [[3,3], [-2,4]]
#
#   Each push/pop costs O(log k) because the heap never has more than k + 1 items,
#   so n points -> O(n log k) time and O(k) space.


if __name__ == "__main__":
    import random
    for _ in range(500):
        pts = [[random.randint(-20, 20), random.randint(-20, 20)] for _ in range(random.randint(1, 15))]
        k = random.randint(1, len(pts))
        want = sorted(p[0] ** 2 + p[1] ** 2 for p in pts)[:k]
        for S in (Solution, SolutionNSmallest, SolutionMaxHeap):
            got = S().kClosest(pts, k)
            assert sorted(p[0] ** 2 + p[1] ** 2 for p in got) == want
    print(Solution().kClosest([[1, 3], [-2, 2]], 1), Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2))
