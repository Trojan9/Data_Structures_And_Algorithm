class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashMap=defaultdict(int)
        #sort first
        words.sort()
        #add word to map
        for i in words:
            hashMap[i]+=1
        myArr=[]
        #for max needed
        for j in range(k):
            #get max from map
            maxima=max(hashMap,key=hashMap.get)
            #delete max
            del hashMap[maxima]
            #add to array
            myArr.append(maxima)
        
        return myArr
            
#using heap

class Solution:
    def topKFrequent(self, words, k):
        # Step 1: Count frequency
        count = Counter(words)

        # Step 2: Build heap (negative frequency so most frequent comes first)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)

        # Step 3: Get top k words
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        return result


🧠 What's a Heap?
A heap is just a special kind of tree data structure used for quick access to the smallest or largest item.

In Python, we usually work with min-heaps using the heapq module.

🔽 Min-Heap:
The smallest value comes first.

In Python, heapq uses a list under the hood.

👇 Why Use a Heap in This Problem?
You want:

The k most frequent words.

If two words have the same frequency, the one with lower alphabetical order comes first.

To do this with a heap:

You push (-frequency, word) — we use negative frequency to turn Python’s min-heap into a max-heap.

This way, the most frequent words come out first!
