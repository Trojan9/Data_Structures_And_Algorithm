# Amazon SDE-I 50, #19: Evaluate Reverse Polish Notation (Medium)  [Stack]
#
from typing import List

# Brief: Evaluate RPN (operator after operands). `["2","1","+","3","*"]` → `9`.
#
# In plain words: evaluate an expression where the operator comes after its two numbers. Push
# numbers onto a stack; when you hit an operator, the two numbers it acts on are the top two, pop
# them, apply, push the result back for later operators to use.
#
# Why it works: in RPN an operator always applies to the two most recently produced values, which
# are the stack's top two. Pushing results back lets nested expressions evaluate with no
# precedence parsing. The first value popped was pushed last, so it's the *right* operand (hence
# `b - a`, `b / a`).
#
# Algorithm
# 1. Operator: pop b, a; push `a op b`. 2. Else push int. 3. Return the last value.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)            # first popped (a) is the RIGHT operand
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))       # truncate toward zero
            else:
                stack.append(int(c))
        return stack[0]

# Complexity: Time O(n), Space O(n).
