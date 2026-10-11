# Stack

Last-in, first-out: matching brackets, undoing, nesting, and 'most recent unresolved item' problems.

| Problem | Key idea | Bloomberg |
|---|---|:-:|
| [valid-parentheses](valid-parentheses.py) | Push opens, pop on matching close | ✅ |
| [decode-string](decode-string.py) | Push until ']', then pop the string and its repeat count | ✅ |
| [remove-all-adjacent-duplicates-in-string-ii](remove-all-adjacent-duplicates-in-string-ii.py) | Stack of [char, count] | ✅ |
| [maximum-nesting-depth-of-the-parentheses](maximum-nesting-depth-of-the-parentheses.py) | Depth counter (an implicit stack) | ✅ |
| [min-stack](min-stack.py) | Second stack tracks the min at each level | ✅ |
