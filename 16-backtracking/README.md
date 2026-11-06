# Backtracking

Choose, explore, un-choose. Builds every combination/path; prune early.

| Problem | Key idea | Bloomberg | Amazon 50 |
|---|---|:-:|:-:|
| [subsets](subsets.py) | Include / exclude each element | ✅ | ✅ |
| [subsets-ii](subsets-ii.py) | Sort, skip duplicates at the same level | ✅ | |
| [word-search](word-search.py) | DFS on the grid, mark visited, unmark on return | ✅ | ✅ |
| [generate-parentheses](generate-parentheses.py) | Add '(' while open < n, ')' while close < open | | ✅ |
| [permutations](permutations.py) | Pick each remaining number, recurse, un-pick | | ✅ |
