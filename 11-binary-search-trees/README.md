# Binary Search Trees

Left < node < right. In-order traversal visits values in sorted order.

## Binary tree vs binary search tree (read this first)

### Binary tree (general)

A tree where each node has **at most two children** (a left and a right). That is the **only** rule.
The values can be in any order. There is no relationship between a parent's value and its children's.

```
      3
     / \
    5   1
   / \
  6   2
```

Here `5 > 3` (left child bigger than parent) and `1 < 3` (right child smaller). Totally allowed.
The numbers are just labels; their arrangement means nothing.

### Binary search tree (BST)

A binary tree with an **extra ordering rule**. For every node:

- everything in its **left subtree** is **smaller** than it, and
- everything in its **right subtree** is **larger**.

And that holds **all the way down**, not just for direct children.

```
      5
     / \
    3   8
   / \   \
  1   4   9
```

Check it:

- left of 5 is {3, 1, 4}: all < 5
- right of 5 is {8, 9}: all > 5
- left of 3 is 1 (< 3), right of 3 is 4 (> 3)
- right of 8 is 9 (> 8)

Every node obeys the rule. That is a BST.

### The trap: "all the way down" means the whole subtree, not just the child

```
      5
     / \
    3   8
       / \
      4   9
```

Every parent/child pair looks fine (`3 < 5`, `8 > 5`, `4 < 8`, `9 > 8`), but this is **NOT** a BST:
`4` sits in the **right subtree of 5**, so it must be > 5, and it isn't.
That is why [validate-binary-search-tree](validate-binary-search-tree.py) passes `(low, high)` bounds down
instead of only comparing a node with its children.

### Why it matters when solving problems

| | Binary tree | BST |
|---|---|---|
| Rule | at most 2 children | at most 2 children **and** left < node < right everywhere |
| Find a value | must check every node, O(n) | go left if smaller, right if bigger, O(h) (O(log n) when balanced) |
| In-order traversal | values in no particular order | values come out **sorted** |
| How to spot it in a question | "binary tree" | "binary **search** tree" / "BST": use the ordering to skip half the tree |

So when a question says **BST**, ask: "can I use left < node < right to decide which side to go,
or use in-order to get sorted values?" (see [lowest-common-ancestor-of-a-bst](lowest-common-ancestor-of-a-bst.py),
[kth-smallest-element-in-a-bst](kth-smallest-element-in-a-bst.py)).
When it only says **binary tree**, you cannot assume any order; you usually have to visit everything
([09-trees-dfs](../09-trees-dfs/README.md)).

## Problems

| Problem | Key idea | Bloomberg | Amazon 50 |
|---|---|:-:|:-:|
| [validate-binary-search-tree](validate-binary-search-tree.py) | Pass (low, high) bounds down | ✅ | ✅ |
| [add-all-greater-values-to-every-node-in-a-bst](add-all-greater-values-to-every-node-in-a-bst.py) | Reverse in-order with a running sum | ✅ | |
| [lowest-common-ancestor-of-a-bst](lowest-common-ancestor-of-a-bst.py) | Both smaller: go left; both bigger: go right; else here | | ✅ |
| [kth-smallest-element-in-a-bst](kth-smallest-element-in-a-bst.py) | Iterative in-order, stop at the kth pop | | ✅ |

> Recursive BST solutions follow the same [rules of tree recursion](../09-trees-dfs/README.md#rules-of-tree-recursion-read-before-every-tree-problem): handle `if not node:` first and return the answer for an empty tree.
