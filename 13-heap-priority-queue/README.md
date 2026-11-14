# Heap / Priority Queue

Get the smallest (or largest, by negating) item in O(log n). Go-to for 'top K' problems.

| Problem | Key idea | Bloomberg | Amazon 50 |
|---|---|:-:|:-:|
| [top-k-frequent-words](top-k-frequent-words.py) | Counter + heap of (-freq, word) | ✅ | |
| [top-k-frequent-elements](top-k-frequent-elements.py) | Bucket sort by frequency (heap also works) | | ✅ |
| [k-closest-points-to-origin](k-closest-points-to-origin.py) | Sort by x²+y² and take k, or keep a size-k max-heap (O(n log k)) | | |
