# Trees: Depth-First Search

Recurse down left/right subtrees and combine results on the way back up.

| Problem | Key idea | Bloomberg |
|---|---|:-:|
| [maximum-depth-of-binary-tree](maximum-depth-of-binary-tree.py) | 1 + max(left, right) |  |
| [minimum-depth-of-binary-tree](minimum-depth-of-binary-tree.py) | Track depth, record at leaves only |  |
| [invert-binary-tree](invert-binary-tree.py) | Swap children, recurse |  |
| [same-tree](same-tree.py) | Compare node, then both subtrees |  |
| [subtree-of-another-tree](subtree-of-another-tree.py) | same-tree at every node |  |
| [merge-two-binary-trees](merge-two-binary-trees.py) | Sum overlapping nodes recursively |  |
| [path-sum](path-sum.py) | Subtract as you go, check at leaf |  |
| [diameter-of-binary-tree](diameter-of-binary-tree.py) | At each node: left height + right height |  |
| [check-mirror-in-n-ary-tree](check-mirror-in-n-ary-tree.py) | Children of A in order == children of B reversed | ✅ |
