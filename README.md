# Data Structures & Algorithms

Solutions grouped by **the principle that solves them**, not by company. Work through the folders in order. Each one builds on the ones before it.
Each folder has its own README with a one-line key idea per problem, and ✅ marks problems tagged as Bloomberg questions or as part of the Amazon SDE-I 50 list.

## Principles (123 problems)

| Principle | When to reach for it | # |
|---|---|:-:|
| [Arrays & Matrices](01-arrays-and-matrices/) | Index arithmetic, in-place swaps and grid simulation. Learn these before anything else. | 6 |
| [Hashing (hash maps & sets)](02-hashing/) | Trade memory for O(1) lookups: count frequencies, remember what you've seen, group by a key. | 13 |
| [Two Pointers](03-two-pointers/) | Two indices moving toward each other (or at different speeds) over sorted or sequential data to avoid nested loops. | 10 |
| [Sliding Window](04-sliding-window/) | Grow the right edge, shrink the left edge while the window is invalid. Turns O(n^2) substring problems into O(n). | 3 |
| [Prefix Sum](05-prefix-sum/) | Precompute running totals so any range sum is prefix[r+1] - prefix[l] in O(1). | 4 |
| [Stack](06-stack/) | Last-in, first-out: matching brackets, undoing, nesting, and 'most recent unresolved item' problems. | 7 |
| [Binary Search](07-binary-search/) | Halve a sorted search space each step: O(log n). Watch the loop condition and mid +/- 1. | 7 |
| [Linked Lists](08-linked-lists/) | Dummy head nodes, fast/slow pointers, and careful pointer rewiring. | 14 |
| [Trees: Depth-First Search](09-trees-dfs/) | Recurse down left/right subtrees and combine results on the way back up. Always start with `if not node: return ...` ([rules](09-trees-dfs/README.md#rules-of-tree-recursion-read-before-every-tree-problem)). | 10 |
| [Trees: Breadth-First Search (level order)](10-trees-bfs/) | Use a deque; process one level at a time with `for _ in range(len(queue))`. | 7 |
| [Binary Search Trees](11-binary-search-trees/) | Left < node < right. In-order traversal visits values in sorted order. | 4 |
| [Graphs (BFS / DFS on grids and adjacency lists)](12-graphs/) | Build an adjacency list (or treat a grid as a graph), keep a visited set, then BFS or DFS. | 9 |
| [Heap / Priority Queue](13-heap-priority-queue/) | Get the smallest (or largest, by negating) item in O(log n). Go-to for 'top K' problems. | 2 |
| [Intervals](14-intervals/) | Sort by start time first, then sweep and compare neighbours. | 3 |
| [Greedy](15-greedy/) | Make the locally best choice each step, when you can prove it never hurts later. | 3 |
| [Backtracking](16-backtracking/) | Choose, explore, un-choose. Builds every combination/path; prune early. | 5 |
| [Dynamic Programming](17-dynamic-programming/) | Break into overlapping subproblems, store the answers (memo or table). | 5 |
| [Math & Bit Manipulation](18-math-and-bit-manipulation/) | Digit tricks (% 10, // 10), XOR cancelling, and bit-count recurrences. | 5 |
| [Design (build a data structure)](19-design/) | Combine the structures above into a class with fast operations. Very common in Bloomberg interviews. | 7 |

## Amazon SDE-I 50

Each of these files carries a full explanation (brief, plain-words idea, why it works, algorithm, complexity) as comments. Where a problem was already solved here, the explanation and reference solution were added at the bottom of the existing file.

| # | Problem | Folder |
|:-:|---|---|
| 1 | [Two Sum (Easy)](02-hashing/two-sum.py) | 02-hashing |
| 2 | [Contains Duplicate (Easy)](02-hashing/contains-duplicate.py) | 02-hashing |
| 3 | [Valid Anagram (Easy)](02-hashing/valid-anagram.py) | 02-hashing |
| 4 | [Group Anagrams (Medium)](02-hashing/group-anagrams.py) | 02-hashing |
| 5 | [Top K Frequent Elements (Medium)](13-heap-priority-queue/top-k-frequent-elements.py) | 13-heap-priority-queue |
| 6 | [Product of Array Except Self (Medium)](05-prefix-sum/product-of-array-except-self.py) | 05-prefix-sum |
| 7 | [Valid Sudoku (Medium)](02-hashing/valid-sudoku.py) | 02-hashing |
| 8 | [Longest Consecutive Sequence (Medium)](01-arrays-and-matrices/Longest-Consecutive-Sequence.py) | 01-arrays-and-matrices |
| 9 | [Valid Palindrome (Easy)](03-two-pointers/valid-palindrome.py) | 03-two-pointers |
| 10 | [Two Sum II, Sorted (Medium)](03-two-pointers/two-sum-ii-input-array-is-sorted.py) | 03-two-pointers |
| 11 | [3Sum (Medium)](03-two-pointers/3sum.py) | 03-two-pointers |
| 12 | [Container With Most Water (Medium)](03-two-pointers/container-with-most-water.py) | 03-two-pointers |
| 13 | [Trapping Rain Water (Hard)](03-two-pointers/trapping-rain-water.py) | 03-two-pointers |
| 14 | [Longest Substring Without Repeating Characters (Medium)](04-sliding-window/longest-substring-without-repeating-characters.py) | 04-sliding-window |
| 15 | [Longest Repeating Character Replacement (Medium)](04-sliding-window/longest-repeating-character-replacement.py) | 04-sliding-window |
| 16 | [Minimum Window Substring (Hard)](04-sliding-window/minimum-window-substring.py) | 04-sliding-window |
| 17 | [Valid Parentheses (Easy)](06-stack/valid-parentheses.py) | 06-stack |
| 18 | [Min Stack (Medium)](06-stack/min-stack.py) | 06-stack |
| 19 | [Evaluate Reverse Polish Notation (Medium)](06-stack/evaluate-reverse-polish-notation.py) | 06-stack |
| 20 | [Daily Temperatures (Medium)](06-stack/daily-temperatures.py) | 06-stack |
| 21 | [Generate Parentheses (Medium)](16-backtracking/generate-parentheses.py) | 16-backtracking |
| 22 | [Binary Search (Easy)](07-binary-search/binary-search.py) | 07-binary-search |
| 23 | [Search a 2D Matrix (Medium)](07-binary-search/search-a-2d-matrix.py) | 07-binary-search |
| 24 | [Find Minimum in Rotated Sorted Array (Medium)](07-binary-search/find-minimum-in-rotated-sorted-array.py) | 07-binary-search |
| 25 | [Search in Rotated Sorted Array (Medium)](07-binary-search/search-in-rotated-sorted-array.py) | 07-binary-search |
| 26 | [Koko Eating Bananas (Medium)](07-binary-search/koko-eating-bananas.py) | 07-binary-search |
| 27 | [Reverse Linked List (Easy)](08-linked-lists/reverse-linked-list.py) | 08-linked-lists |
| 28 | [Merge Two Sorted Lists (Easy)](08-linked-lists/merge-two-sorted-lists.py) | 08-linked-lists |
| 29 | [Linked List Cycle (Easy)](08-linked-lists/linked-list-cycle.py) | 08-linked-lists |
| 30 | [Remove Nth Node From End (Medium)](08-linked-lists/remove-nth-node-from-end-of-list.py) | 08-linked-lists |
| 31 | [Reorder List (Medium)](08-linked-lists/reorder-list.py) | 08-linked-lists |
| 32 | [LRU Cache (Medium)](19-design/lru-cache.py) | 19-design |
| 33 | [Invert Binary Tree (Easy)](09-trees-dfs/invert-binary-tree.py) | 09-trees-dfs |
| 34 | [Maximum Depth (Easy)](09-trees-dfs/maximum-depth-of-binary-tree.py) | 09-trees-dfs |
| 35 | [Same Tree (Easy)](09-trees-dfs/same-tree.py) | 09-trees-dfs |
| 36 | [Binary Tree Level Order Traversal (Medium)](10-trees-bfs/binary-tree-level-order-traversal.py) | 10-trees-bfs |
| 37 | [Validate Binary Search Tree (Medium)](11-binary-search-trees/validate-binary-search-tree.py) | 11-binary-search-trees |
| 38 | [Lowest Common Ancestor of a BST (Medium)](11-binary-search-trees/lowest-common-ancestor-of-a-bst.py) | 11-binary-search-trees |
| 39 | [Kth Smallest Element in a BST (Medium)](11-binary-search-trees/kth-smallest-element-in-a-bst.py) | 11-binary-search-trees |
| 40 | [Construct Tree from Preorder and Inorder (Medium)](09-trees-dfs/construct-binary-tree-from-preorder-and-inorder.py) | 09-trees-dfs |
| 41 | [Binary Tree Right Side View (Medium)](10-trees-bfs/binary-tree-right-side-view.py) | 10-trees-bfs |
| 42 | [Number of Islands (Medium)](12-graphs/number-of-islands.py) | 12-graphs |
| 43 | [Clone Graph (Medium)](12-graphs/clone-graph.py) | 12-graphs |
| 44 | [Course Schedule (Medium)](12-graphs/course-schedule.py) | 12-graphs |
| 45 | [Rotting Oranges (Medium)](12-graphs/rotting-oranges.py) | 12-graphs |
| 46 | [Word Search (Medium)](16-backtracking/word-search.py) | 16-backtracking |
| 47 | [Subsets (Medium)](16-backtracking/subsets.py) | 16-backtracking |
| 48 | [Permutations (Medium)](16-backtracking/permutations.py) | 16-backtracking |
| 49 | [Climbing Stairs (Easy)](17-dynamic-programming/climbing-stairs.py) | 17-dynamic-programming |
| 50 | [Coin Change (Medium)](17-dynamic-programming/coin-change.py) | 17-dynamic-programming |

## Notes

- [BFS vs DFS walkthrough](notes/bfs-vs-dfs.txt)

## Pattern recognition cheat sheet

| If the problem says... | Try |
|---|---|
| "find a pair / have I seen this before / count occurrences" | Hashing |
| sorted array, or "pair that sums to X" in place | Two Pointers / Binary Search |
| "longest / shortest substring or subarray that..." | Sliding Window |
| "sum of range i..j", asked many times | Prefix Sum |
| brackets, nesting, "undo", "most recent" | Stack |
| "kth largest", "top K", "smallest so far, repeatedly" | Heap |
| list of [start, end] | Intervals (sort by start) |
| tree, "per level" | Trees BFS |
| tree, "height / path / compare subtrees" | Trees DFS |
| grid of cells, "connected", "islands", dependencies | Graphs |
| "all combinations / subsets / permutations" | Backtracking |
| "number of ways", "min/max cost", choices that overlap | Dynamic Programming |
| "design a class that supports X in O(1)" | Design |

## Computer science principles (cheat code)

Here you go:

 - Hashing to get quick lookups.
 - Sorting to get quick searches.
 - Append only to get fast and high throughput writes.
 - In-memory to get ultra fast writes/reads.
 - Probabilistic data structures to get fast lookups with chances of false positives.
 - B-trees to get quick lookups with disk-friendly access patterns.
 - Bloom filters to get space-efficient membership testing with acceptable false positives.
 - Write-ahead logging to get durability without sacrificing write performance.
 - Caching to get fast reads by storing frequently accessed data in faster storage.
 - Indexing to get quick searches without scanning entire datasets.
 - Compression to get reduced storage costs at the expense of CPU overhead.
 - Sharding to get horizontal scalability by distributing data across multiple nodes.
 - Replication to get high availability and read performance through data redundancy.
 - Columnar storage to get fast analytical queries by storing related data together.
 - LSM trees to get high write throughput by batching writes and periodic merging.
 - Skip lists to get balanced tree performance with simpler lock-free implementations.
 - Consistent hashing to get even data distribution with minimal reshuffling during scaling.
 - Trie structures to get fast prefix matching and autocomplete functionality.
 - Ring buffers to get bounded memory usage with efficient circular data access.
 - Copy-on-write to get memory efficiency by sharing data until modifications occur.
 - Merkle trees to get tamper detection and efficient synchronization through cryptographic hashing.
 - Segment trees to get fast range queries with logarithmic update complexity.
 - Fenwick trees to get efficient prefix sum calculations with minimal memory overhead.
 - Union-find to get fast connectivity queries through path compression and union by rank.
 - Suffix arrays to get efficient string matching with reduced memory compared to suffix trees.
 - Inverted indexes to get fast full-text search by mapping terms to document locations.
 - Spatial indexing to get quick geographic queries through multi-dimensional partitioning.
 - Time-series databases to get optimized storage for chronological data with compression.
 - Event sourcing to get complete audit trails by storing state changes instead of current state.
 - CRDT (Conflict-free Replicated Data Types) to get eventual consistency without coordination overhead.
 - Lockless data structures to get high concurrency through atomic operations and memory ordering.
 - Partitioning to get improved performance by dividing data based on access patterns.
 - Materialized views to get fast complex queries by pre-computing and storing results.
 - Delta compression to get reduced storage by storing only differences between versions.
 - Heap data structures to get efficient priority queue operations with constant-time peek.
 - Rope data structures to get efficient string concatenation and manipulation for large texts.
 - Radix trees to get memory-efficient prefix storage through path compression.
 - Adaptive data structures to get self-optimizing performance based on access patterns.
 - Batching to get improved throughput by amortizing overhead across multiple operations.
