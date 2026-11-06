# Two Pointers

Two indices moving toward each other (or at different speeds) over sorted or sequential data to avoid nested loops.

| Problem | Key idea | Bloomberg | Amazon 50 |
|---|---|:-:|:-:|
| [squares-of-a-sorted-array](squares-of-a-sorted-array.py) | Largest square sits at one of the two ends |  | |
| [backspace-string-compare](backspace-string-compare.py) | Build with a stack, or walk both strings from the back |  | |
| [move-all-zeroes-to-end](move-all-zeroes-to-end.py) | Write pointer for the next non-zero slot | ✅ | |
| [merge-strings-alternately](merge-strings-alternately.py) | One pointer per string | ✅ | |
| [valid-triangle-number](valid-triangle-number.py) | Sort, fix the largest side, squeeze the other two | ✅ | |
| [valid-palindrome](valid-palindrome.py) | Pointers at both ends, skip non-alphanumerics | | ✅ |
| [two-sum-ii-input-array-is-sorted](two-sum-ii-input-array-is-sorted.py) | Sum too small: move left; too big: move right | | ✅ |
| [3sum](3sum.py) | Sort, fix one number, two-pointer the rest, skip duplicates | | ✅ |
| [container-with-most-water](container-with-most-water.py) | Always move the pointer at the shorter wall | | ✅ |
| [trapping-rain-water](trapping-rain-water.py) | Track leftMax/rightMax, advance the smaller side | | ✅ |
