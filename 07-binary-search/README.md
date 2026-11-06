# Binary Search

Halve a sorted search space each step: O(log n). Watch the loop condition and mid +/- 1.

| Problem | Key idea | Bloomberg | Amazon 50 |
|---|---|:-:|:-:|
| [binary-search](binary-search.py) | Classic l <= r loop |  | ✅ |
| [find-smallest-letter-greater-than-target](find-smallest-letter-greater-than-target.py) | Upper bound with wrap-around |  | |
| [heaters](heaters.py) | Sort heaters, bisect for nearest one per house |  | |
| [search-a-2d-matrix](search-a-2d-matrix.py) | Treat the grid as one sorted list: m // cols, m % cols | | ✅ |
| [find-minimum-in-rotated-sorted-array](find-minimum-in-rotated-sorted-array.py) | Go toward the half that contains the drop | | ✅ |
| [search-in-rotated-sorted-array](search-in-rotated-sorted-array.py) | One half is always sorted; check if target is in it | | ✅ |
| [koko-eating-bananas](koko-eating-bananas.py) | Binary search on the answer (speed 1..max pile) | | ✅ |
