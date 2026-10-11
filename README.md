# Data Structures & Algorithms

Solutions grouped by **the principle that solves them**, not by company. Work through the folders in order. Each one builds on the ones before it.
Each folder has its own README with a one-line key idea per problem, and a ✅ marks problems tagged as Bloomberg questions.

## Principles (93 problems)

| Principle | When to reach for it | # |
|---|---|:-:|
| [Arrays & Matrices](01-arrays-and-matrices/) | Index arithmetic, in-place swaps and grid simulation. Learn these before anything else. | 5 |
| [Hashing (hash maps & sets)](02-hashing/) | Trade memory for O(1) lookups: count frequencies, remember what you've seen, group by a key. | 12 |
| [Two Pointers](03-two-pointers/) | Two indices moving toward each other (or at different speeds) over sorted or sequential data to avoid nested loops. | 5 |
| [Sliding Window](04-sliding-window/) | Grow the right edge, shrink the left edge while the window is invalid. Turns O(n^2) substring problems into O(n). | 1 |
| [Prefix Sum](05-prefix-sum/) | Precompute running totals so any range sum is prefix[r+1] - prefix[l] in O(1). | 3 |
| [Stack](06-stack/) | Last-in, first-out: matching brackets, undoing, nesting, and 'most recent unresolved item' problems. | 5 |
| [Binary Search](07-binary-search/) | Halve a sorted search space each step: O(log n). Watch the loop condition and mid +/- 1. | 3 |
| [Linked Lists](08-linked-lists/) | Dummy head nodes, fast/slow pointers, and careful pointer rewiring. | 12 |
| [Trees: Depth-First Search](09-trees-dfs/) | Recurse down left/right subtrees and combine results on the way back up. | 9 |
| [Trees: Breadth-First Search (level order)](10-trees-bfs/) | Use a deque; process one level at a time with `for _ in range(len(queue))`. | 5 |
| [Binary Search Trees](11-binary-search-trees/) | Left < node < right. In-order traversal visits values in sorted order. | 2 |
| [Graphs (BFS / DFS on grids and adjacency lists)](12-graphs/) | Build an adjacency list (or treat a grid as a graph), keep a visited set, then BFS or DFS. | 5 |
| [Heap / Priority Queue](13-heap-priority-queue/) | Get the smallest (or largest, by negating) item in O(log n). Go-to for 'top K' problems. | 1 |
| [Intervals](14-intervals/) | Sort by start time first, then sweep and compare neighbours. | 3 |
| [Greedy](15-greedy/) | Make the locally best choice each step, when you can prove it never hurts later. | 3 |
| [Backtracking](16-backtracking/) | Choose, explore, un-choose. Builds every combination/path; prune early. | 3 |
| [Dynamic Programming](17-dynamic-programming/) | Break into overlapping subproblems, store the answers (memo or table). | 4 |
| [Math & Bit Manipulation](18-math-and-bit-manipulation/) | Digit tricks (% 10, // 10), XOR cancelling, and bit-count recurrences. | 5 |
| [Design (build a data structure)](19-design/) | Combine the structures above into a class with fast operations. Very common in Bloomberg interviews. | 7 |

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
