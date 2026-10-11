# Hashing (hash maps & sets)

Trade memory for O(1) lookups: count frequencies, remember what you've seen, group by a key.

| Problem | Key idea | Bloomberg |
|---|---|:-:|
| [two-sum](two-sum.py) | Store value -> index, look up target - n | |
| [two-sum-bloomberg](two-sum-bloomberg.py) | Same problem, Bloomberg-folder version | ✅ |
| [contains-duplicate](contains-duplicate.py) | Set size vs list size |  |
| [group-anagrams](group-anagrams.py) | Key = sorted word / letter count |  |
| [valid-anagram](valid-anagram.py) | Compare letter counts | ✅ |
| [first-unique-character-in-a-string](first-unique-character-in-a-string.py) | Count, then scan for count == 1 | ✅ |
| [majority-element](majority-element.py) | Count and take the max |  |
| [find-the-duplicate-number](find-the-duplicate-number.py) | Seen-before dict |  |
| [find-all-numbers-disappeared-in-an-array](find-all-numbers-disappeared-in-an-array.py) | Set of 1..n minus set of nums |  |
| [missing-number](missing-number.py) | Check 0..n membership |  |
| [rabbits-in-forest](rabbits-in-forest.py) | Counter + group-size math | ✅ |
| [invalid-transactions](invalid-transactions.py) | Group transactions by name, compare times/cities | ✅ |
| [sort-characters-by-frequency](sort-characters-by-frequency.py) | Counter, then sort by count | ✅ |
