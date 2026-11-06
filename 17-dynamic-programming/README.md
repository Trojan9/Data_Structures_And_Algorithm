# Dynamic Programming

Break into overlapping subproblems, store the answers (memo or table).

| Problem | Key idea | Bloomberg | Amazon 50 |
|---|---|:-:|:-:|
| [climbing-stairs](climbing-stairs.py) | ways(n) = ways(n-1) + ways(n-2) |  | ✅ |
| [maximum-subarray](maximum-subarray.py) | Kadane: drop the running sum when it goes negative |  | |
| [unique-paths](unique-paths.py) | grid[r][c] = top + left | ✅ | |
| [word-break](word-break.py) | dp[i] = some word ends at i and dp[i - len(word)] | ✅ | |
| [coin-change](coin-change.py) | dp[a] = min(1 + dp[a - coin]) | | ✅ |
