# Binary Search Trees

Left < node < right. In-order traversal visits values in sorted order.

| Problem | Key idea | Bloomberg | Amazon 50 |
|---|---|:-:|:-:|
| [validate-binary-search-tree](validate-binary-search-tree.py) | Pass (low, high) bounds down | ✅ | ✅ |
| [add-all-greater-values-to-every-node-in-a-bst](add-all-greater-values-to-every-node-in-a-bst.py) | Reverse in-order with a running sum | ✅ | |
| [lowest-common-ancestor-of-a-bst](lowest-common-ancestor-of-a-bst.py) | Both smaller: go left; both bigger: go right; else here | | ✅ |
| [kth-smallest-element-in-a-bst](kth-smallest-element-in-a-bst.py) | Iterative in-order, stop at the kth pop | | ✅ |

> Recursive BST solutions follow the same [rules of tree recursion](../09-trees-dfs/README.md#rules-of-tree-recursion-read-before-every-tree-problem): handle `if not node:` first and return the answer for an empty tree.
