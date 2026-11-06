# Stack

Last-in, first-out: matching brackets, undoing, nesting, and 'most recent unresolved item' problems.

| Problem | Key idea | Bloomberg | Amazon 50 |
|---|---|:-:|:-:|
| [valid-parentheses](valid-parentheses.py) | Push opens, pop on matching close | ✅ | ✅ |
| [decode-string](decode-string.py) | Push until ']', then pop the string and its repeat count | ✅ | |
| [remove-all-adjacent-duplicates-in-string-ii](remove-all-adjacent-duplicates-in-string-ii.py) | Stack of [char, count] | ✅ | |
| [maximum-nesting-depth-of-the-parentheses](maximum-nesting-depth-of-the-parentheses.py) | Depth counter (an implicit stack) | ✅ | |
| [min-stack](min-stack.py) | Second stack tracks the min at each level | ✅ | ✅ |
| [evaluate-reverse-polish-notation](evaluate-reverse-polish-notation.py) | Push numbers; an operator pops two and pushes the result | | ✅ |
| [daily-temperatures](daily-temperatures.py) | Monotonic decreasing stack of (temp, index) | | ✅ |
