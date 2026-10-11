# Prefix Sum

Precompute running totals so any range sum is prefix[r+1] - prefix[l] in O(1).

| Problem | Key idea | Bloomberg |
|---|---|:-:|
| [range-sum-query-immutable](range-sum-query-immutable.py) | 1D prefix array |  |
| [range-sum-query-2d](range-sum-query-2d.py) | 2D summed-area table: bottomRight - top - left + topLeft | ✅ |
| [product-of-array-except-self](product-of-array-except-self.py) | Prefix products times suffix products |  |
