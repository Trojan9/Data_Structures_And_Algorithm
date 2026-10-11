# Design (build a data structure)

Combine the structures above into a class with fast operations. Very common in Bloomberg interviews.

| Problem | Key idea | Bloomberg |
|---|---|:-:|
| [lru-cache](lru-cache.py) | Hash map + doubly linked list (or OrderedDict) | ✅ |
| [insert-delete-getrandom-o1](insert-delete-getrandom-o1.py) | List + value -> index map; swap with last to delete | ✅ |
| [first-unique-number](first-unique-number.py) | Queue + Counter | ✅ |
| [design-browser-history](design-browser-history.py) | List + current index (or two stacks) | ✅ |
| [design-underground-system](design-underground-system.py) | Check-in map + (start, end) -> totals map | ✅ |
| [design-a-leaderboard](design-a-leaderboard.py) | Score map; sort/heap for top K | ✅ |
| [design-an-ordered-stream](design-an-ordered-stream.py) | Array + pointer to the next expected id | ✅ |
