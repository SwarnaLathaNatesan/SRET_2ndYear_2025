# Recursion Cheat Sheet

## General Template
```python
def recurse(params):
    # Base Case
    if condition:
        return result
    # Recursive Case
    return recurse(smaller_problem of params)
```

## Key Concepts
- Base case prevents infinite recursion.
- Recursive case reduces problem size.
- Common in trees, divide & conquer, backtracking.

## Common Patterns
1. Factorial, Fibonacci → Numerical recursion.
2. Reverse string/array → Divide problem into head & tail.
3. Tree Traversals → Left + Root + Right pattern.
4. Backtracking → Try → Recurse → Undo.
