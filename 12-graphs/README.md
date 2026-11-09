# Graphs (BFS / DFS on grids and adjacency lists)

Build an adjacency list (or treat a grid as a graph), keep a visited set, then BFS or DFS.

| Problem | Key idea | Bloomberg | Amazon 50 |
|---|---|:-:|:-:|
| [number-of-islands](number-of-islands.py) | Flood-fill each unvisited land cell | ✅ | ✅ |
| [island-perimeter](island-perimeter.py) | Count land edges touching water/border | ✅ | |
| [all-paths-from-source-to-target](all-paths-from-source-to-target.py) | DFS with a path list (DAG, no visited needed) | ✅ | |
| [kill-process](kill-process.py) | parent -> children map, BFS from the killed pid | ✅ | |
| [evaluate-division](evaluate-division.py) | Weighted graph; multiply edge weights along a path | ✅ | |
| [clone-graph](clone-graph.py) | old -> new node map; BFS with a queue (or DFS) | | ✅ |
| [course-schedule](course-schedule.py) | Cycle detection with a 'visiting' set on the current path | | ✅ |
| [rotting-oranges](rotting-oranges.py) | Multi-source BFS, one wave per minute | | ✅ |
