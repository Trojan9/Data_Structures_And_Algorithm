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
