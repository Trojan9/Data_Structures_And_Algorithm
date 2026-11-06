# Trees: Breadth-First Search (level order)

Use a deque; process one level at a time with `for _ in range(len(queue))`.

| Problem | Key idea | Bloomberg | Amazon 50 |
|---|---|:-:|:-:|
| [average-of-levels-in-binary-tree](average-of-levels-in-binary-tree.py) | Sum / count per level |  | |
| [find-largest-value-in-each-tree-row](find-largest-value-in-each-tree-row.py) | Max per level | ✅ | |
| [populating-next-right-pointers-in-each-node](populating-next-right-pointers-in-each-node.py) | Link nodes within a level | ✅ | |
| [populating-next-right-pointers-in-each-node-ii](populating-next-right-pointers-in-each-node-ii.py) | Same, for a non-perfect tree | ✅ | |
| [binary-tree-vertical-order-traversal](binary-tree-vertical-order-traversal.py) | BFS carrying a column index; group by column | ✅ | |
| [binary-tree-level-order-traversal](binary-tree-level-order-traversal.py) | Deque; pop len(queue) nodes per level | | ✅ |
| [binary-tree-right-side-view](binary-tree-right-side-view.py) | Level order, keep the last node of each level | | ✅ |
