You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]


### solution explanation ###


✅ Problem Recap
You're given equations like:

equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
This means:

a / b = 2.0

b / c = 3.0

You're also given queries like:

queries = [["a", "c"], ["b", "a"]]
And your job is to compute:

a / c = ? (Should be 6.0 because a/b * b/c)

b / a = ? (Should be 0.5 because inverse of 2.0)

✅ Step-by-Step BFS Approach
🔧 Step 1: Build a graph
Treat each variable (a, b, c) as a node.
Treat a / b = 2.0 as a directed edge from a → b with weight 2.0
Also add reverse edge: b → a = 1/2.0

This gives us a weighted bidirectional graph.

graph = {
  'a': {'b': 2.0},
  'b': {'a': 0.5, 'c': 3.0},
  'c': {'b': 1/3.0}
}
🚶 Step 2: Use BFS to answer a query
To answer "a" / "c":

Start at "a", do a BFS search for "c"

As you go from node to node, multiply the path weights

So:

a → b = 2.0  
b → c = 3.0  
⇒ a / c = 2.0 × 3.0 = 6.0 ✅


from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        #firstly create the graph
        for i in range(len(equations)):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = 1 / values[i]

        
        def bfs(start,end):
            #if any of start or end not in graph...noting of it was given then then..no way we culd get something
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            queue = deque()
            visited = set()
            #for every node, we will multiply by our present value
            queue.append([start, 1.0])

            while queue:
                node, value = queue.popleft()
                if node == end:
                    return value
                visited.add(node)
                for neighbors in graph[node]:
                    if neighbors not in visited:
                        queue.append([neighbors,value * graph[node][neighbors]])
                        
            return -1.0

        return [bfs(a,b) for a,b in queries]


# Complexity of the BFS solution above
#   E = number of equations, V = number of variables (nodes), Q = number of queries
#   Build the graph: O(E)   (2 edges per equation)
#   One query:       O(V + E)   BFS may visit every node and look at every edge once
#   All queries:     O(E + Q * (V + E))
#   Space:           O(V + E) for the graph, + O(V) for the queue and visited set


# ==================== Solution 2: DFS ====================
# Same graph as the BFS one. Instead of a queue, we go DEEP along one path:
# "can I get from src to dst through this neighbour?"
#   - if yes, the answer = (rate src -> neighbour) * (answer neighbour -> dst)
#   - if no (dead end, returns -1.0), try the next neighbour
# The rates are MULTIPLIED on the way back UP the recursion.
#
# (This is the "currency conversion" question from the Amazon SDE-1 round 2:
#  C = 10B, D = 9B, B = 110Z, A = 2Z -> find A to B. Currencies are the nodes,
#  rates are the edge weights, exactly like a/b = 2.0 here.)

from collections import defaultdict

def calcEquation(equations, values, queries):
    graph = defaultdict(dict)
    for (a, b), r in zip(equations, values):
        graph[a][b] = r
        graph[b][a] = 1 / r          # reverse edge is the inverse rate

    def dfs(src, dst, visited):
        if src not in graph or dst not in graph:
            return -1.0              # unknown currency
        if src == dst:
            return 1.0               # same currency → rate 1
        visited.add(src)
        for nei, rate in graph[src].items():
            if nei not in visited:
                sub = dfs(nei, dst, visited)
                if sub != -1.0:
                    return rate * sub   # multiply along the path
        return -1.0

    return [dfs(a, b, set()) for a, b in queries]

# Line by line
#   graph[a][b] = r, graph[b][a] = 1 / r
#       a / b = r means b / a = 1 / r, so every equation gives an edge both ways.
#   if src not in graph or dst not in graph: return -1.0
#       a variable that never appeared in any equation -> cannot be worked out.
#       This check comes BEFORE src == dst on purpose: "x" / "x" must be -1.0
#       (x is undefined), not 1.0.
#   if src == dst: return 1.0
#       reached the target. Anything divided by itself is 1, and 1 is the
#       neutral value for multiplying (like 0 for adding), so the rates above
#       stay unchanged when they multiply by it.
#   visited.add(src)
#       don't come back to this node on the same search (the graph has
#       reverse edges, so without this a -> b -> a -> b ... loops forever).
#   sub = dfs(nei, dst, visited); if sub != -1.0: return rate * sub
#       the neighbour found a path: src -> nei costs `rate`, nei -> dst costs `sub`,
#       so src -> dst = rate * sub.
#   return -1.0
#       every neighbour was a dead end -> no path from here.
#   dfs(a, b, set())
#       a NEW visited set for every query; each query is its own search.
#
# DRY RUN 1: Example 1, equations a/b = 2, b/c = 3
#
#   graph = { a: {b: 2},  b: {a: 0.5, c: 3},  c: {b: 1/3} }
#
#   Query a / c:
#     dfs(a, c)  visited {a}       neighbour b (rate 2)
#       dfs(b, c)  visited {a, b}  neighbour a: visited, skip
#                                  neighbour c (rate 3)
#         dfs(c, c)  src == dst                    -> 1.0
#       dfs(b, c)  sub = 1.0                       -> 3 * 1.0 = 3.0
#     dfs(a, c)  sub = 3.0                         -> 2 * 3.0 = 6.0   ✅
#
#   Query b / a:  dfs(b): neighbour a (rate 0.5) -> dfs(a, a) = 1.0 -> 0.5   ✅
#   Query a / e:  e not in graph                                    -> -1.0 ✅
#   Query a / a:  both in graph, src == dst                         -> 1.0  ✅
#   Query x / x:  x not in graph (checked first)                    -> -1.0 ✅
#
# DRY RUN 2: a dead end, so DFS has to back up and try the next neighbour
#   equations a/d = 4, a/b = 2, b/c = 3      query a / c
#
#   graph = { a: {d: 4, b: 2},  d: {a: 0.25},  b: {a: 0.5, c: 3},  c: {b: 1/3} }
#
#           d --4-- a --2-- b --3-- c
#
#   dfs(a, c)  visited {a}         first neighbour d (rate 4)
#     dfs(d, c)  visited {a, d}    only neighbour a is visited -> dead end -> -1.0
#   dfs(a, c)  sub = -1.0, so try the next neighbour b (rate 2)
#     dfs(b, c)  visited {a, d, b} neighbour a visited, neighbour c (rate 3)
#       dfs(c, c)                                  -> 1.0
#     dfs(b, c)                                    -> 3 * 1.0 = 3.0
#   dfs(a, c)                                      -> 2 * 3.0 = 6.0   ✅
#
# BFS vs DFS here: both find A path, and any path gives the same answer (the
# problem says there is no contradiction), so either works.
#   BFS: carries the running product in the queue: (node, value so far).
#   DFS: multiplies the rates on the way back up the recursion.
#
# Complexity (DFS)
#   E = number of equations, V = number of variables (nodes), Q = number of queries
#   Build the graph: O(E)
#   One query:       O(V + E)   each node is visited at most once (visited set),
#                               each edge looked at at most once from each side
#   All queries:     O(E + Q * (V + E))
#   Space:           O(V + E) for the graph, + O(V) for visited and the recursion stack
#
# Follow-up (asked in the Amazon interview): "now there are Q queries"
#   Re-searching for every query costs O(V + E) each. Weighted Union Find stores, for
#   every variable, its rate to the root of its group; then each query is
#   rate(a -> root) / rate(b -> root) in almost O(1) (if a and b have the same root,
#   otherwise -1.0). Total about O((E + Q) * α(V)), where α grows so slowly it is
#   basically a constant.
