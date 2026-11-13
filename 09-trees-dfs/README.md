# Trees: Depth-First Search

Recurse down left/right subtrees and combine results on the way back up.

> Binary tree or BST? A plain binary tree has **no ordering** between parent and children; a BST has left < node < right for the whole subtree. See [binary tree vs binary search tree](../11-binary-search-trees/README.md#binary-tree-vs-binary-search-tree-read-this-first).

| Problem | Key idea | Bloomberg | Amazon 50 |
|---|---|:-:|:-:|
| [maximum-depth-of-binary-tree](maximum-depth-of-binary-tree.py) | 1 + max(left, right) |  | ✅ |
| [minimum-depth-of-binary-tree](minimum-depth-of-binary-tree.py) | Track depth, record at leaves only |  | |
| [invert-binary-tree](invert-binary-tree.py) | Swap children, recurse |  | ✅ |
| [same-tree](same-tree.py) | Compare node, then both subtrees |  | ✅ |
| [subtree-of-another-tree](subtree-of-another-tree.py) | same-tree at every node |  | |
| [merge-two-binary-trees](merge-two-binary-trees.py) | Sum overlapping nodes recursively |  | |
| [path-sum](path-sum.py) | Subtract as you go, check at leaf |  | |
| [diameter-of-binary-tree](diameter-of-binary-tree.py) | At each node: left height + right height |  | |
| [check-mirror-in-n-ary-tree](check-mirror-in-n-ary-tree.py) | Children of A in order == children of B reversed | ✅ | |
| [construct-binary-tree-from-preorder-and-inorder](construct-binary-tree-from-preorder-and-inorder.py) | preorder[0] is the root; its inorder index splits the subtrees | | ✅ |
| [lowest-common-ancestor-of-a-binary-tree](lowest-common-ancestor-of-a-binary-tree.py) | Return None up till you see p or q; if left AND right both come back, this node is the LCA | | |

---

## Rules of tree recursion (read before every tree problem)

### Rule 1: recursion goes all the way to the BOTTOM first, then answers come back UP

A recursive call doesn't finish until the calls below it finish. So the code dives down
`left`/`right` until it falls off the tree (`node is None`), and only then do answers start
flowing back up, one level at a time, to the root.

```
maxDepth(3)                          tree:      3
├── maxDepth(9)                                / \
│   ├── maxDepth(None) -> 0   ← bottom        9   20
│   └── maxDepth(None) -> 0   ← bottom           /  \
│   returns 1 + max(0, 0) = 1                   15    7
└── maxDepth(20)
    ├── maxDepth(15)
    │   ├── maxDepth(None) -> 0
    │   └── maxDepth(None) -> 0
    │   returns 1
    ├── maxDepth(7)
    │   ├── maxDepth(None) -> 0
    │   └── maxDepth(None) -> 0
    │   returns 1
    returns 1 + max(1, 1) = 2
returns 1 + max(1, 2) = 3            ← root answers LAST
```

The root is the first call made and the last one to return.

**It goes one step PAST the last level.** A leaf still calls `dfs(leaf.left)` and
`dfs(leaf.right)`. Both are `None`, so every path ends one level below the leaves. That
`None` level is where the early exit runs, and it's where the answers start going back up:

```
            1
           / \
          2   3
         / \  / \
        4  5 N   N        ← 3 is a leaf, but dfs still visits its None children
       /\  /\
      N N  N N            ← the "one step further" level: early exit, return the base value
                            everything after this flows UPWARD
```

**The base value and the combine step must match.** In
[diameter](diameter-of-binary-tree.py), `return 0` (height counts nodes) goes with
`left + right`, but `return -1` (height counts edges) needs `left + right + 2`. Mixing them
gives a wrong answer with no error.

### Rule 2: ALWAYS handle the bottom (out of the tree) FIRST, and return something

Below every leaf there's an empty spot (`None`). Every path reaches it, so the **first line**
of every tree recursion must be the base case:

```python
def dfs(node):
    if not node:          # fell off the tree: the bottom level
        return ...        # MUST return something the parent can use
    left = dfs(node.left)
    right = dfs(node.right)
    return ...            # combine left + right + node
```

Without it, you call `node.left` on `None` and get
`AttributeError: 'NoneType' object has no attribute 'left'`.

### Rule 3: what to return at the bottom = "the answer for an empty tree"

Ask: *"if the tree were empty, what would the answer be?"* Return exactly that. Then the
parent's combine step works without special cases.

| Problem asks for | Return at `if not node:` | Why |
|---|---|---|
| a count / height / depth / sum | `0` | an empty tree has height 0, sum 0 |
| a tree / node ([invert](invert-binary-tree.py), [merge](merge-two-binary-trees.py), [construct](construct-binary-tree-from-preorder-and-inorder.py)) | `None` | an empty subtree is `None` |
| yes / no "does a path exist?" ([path-sum](path-sum.py)) | `False` | nothing to find in an empty tree |
| yes / no "is it valid / balanced?" ([validate BST](../11-binary-search-trees/validate-binary-search-tree.py)) | `True` | an empty tree breaks no rule |
| comparing two trees ([same-tree](same-tree.py)) | `p is None and q is None` → `True`; only one `None` → `False` | two empty trees match; empty vs not-empty don't |
| a list of values (traversals) | `[]` (or just `return`) | nothing to add |
| a minimum / maximum value | `float('inf')` / `float('-inf')` | never wins the `min` / `max` |
| nothing: answer saved in `self.something` (your [path-sum](path-sum.py) uses `self.myBool`) | plain `return` | still MUST stop here, just nothing to hand back |

**Check your base case:** plug it into the combine step for a leaf. For max depth, a leaf
gives `1 + max(0, 0) = 1`. That's correct, so `0` is the right base.

### Rule 4: trust the recursive call, and only think about ONE node

Don't trace the whole tree in your head. Assume `dfs(node.left)` already gives the right answer
for the left subtree, and `dfs(node.right)` for the right. Your only job is:
*"given the left answer and the right answer, what's the answer for this node?"*

### Rule 5: decide WHEN this node does its work

| Where the work goes | Order | Use it for |
|---|---|---|
| before the recursive calls | pre-order (top → down) | passing info DOWN: running sum, depth, min/max bounds |
| after the recursive calls | post-order (bottom → up) | building answers UP: height, diameter, "is balanced" |
| between left and right | in-order | BSTs: visits values in sorted order |

### Checklist
1. `if not node: return <answer for an empty tree>` is the first line
2. recurse left, recurse right
3. combine left + right + node into this node's answer, and **return it**
4. if you also pass something down (bound, running total), it goes in the call: `dfs(node.left, total + node.val)`
