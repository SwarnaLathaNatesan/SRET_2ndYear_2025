
"""
Recursion — Answers for Small Programs (no binary tree)
Each function includes 2-line core logic comments before it.
Run this file to see example outputs for multiple inputs.
"""
def sum(n):
  if n == 0 :
      return 0
  return n+sum(n-1)

print(sum(5))
   


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))



# Sum of list
# Core logic: 1) base case empty list -> 0  2) reduction: arr[0] + sum_list(arr[1:])
def sum_list(arr):
    if not arr:
        return 0
    return arr[0] + sum_list(arr[1:])

# Reverse string
# Core logic: 1) base case empty/one char -> same  2) reduction: last char + reverse(prefix)
def reverse_str(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_str(s[:-1])

# Fibonacci (naive and memoized)
# Core logic: 1) base cases n==0 or n==1  2) return fib(n-1)+fib(n-2); use cache for memoized
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

def fib_memo(n, cache=None):
    if cache is None: cache = {}
    if n in cache: return cache[n]
    if n <= 1:
        cache[n] = n
    else:
        cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
    return cache[n]

# Subsets (power set)
# Core logic: 1) base when index == len -> emit  2) branch include/exclude
def subsets(nums):
    res = []
    def helper(i, path):
        if i == len(nums):
            res.append(path.copy()); return
        helper(i+1, path)
        path.append(nums[i])
        helper(i+1, path)
        path.pop()
    helper(0, [])
    return res

# Permutations (distinct)
# Core logic: 1) backtrack swapping  2) collect when index==len
def permutations(nums):
    res = []
    def helper(i):
        if i == len(nums):
            res.append(nums.copy()); return
        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            helper(i+1)
            nums[i], nums[j] = nums[j], nums[i]
    helper(0)
    return res

# Letter case permutation (784)
# Core logic: 1) branch for alpha char: lower/upper  2) for digit, just continue
def letter_case_permutation(s):
    res = []
    def dfs(i, path):
        if i == len(s):
            res.append(''.join(path)); return
        ch = s[i]
        if ch.isalpha():
            path.append(ch.lower()); dfs(i+1, path); path.pop()
            path.append(ch.upper()); dfs(i+1, path); path.pop()
        else:
            path.append(ch); dfs(i+1, path); path.pop()
    dfs(0, [])
    return res

# Merge Two Sorted Lists (21) - recursive using python lists
# Core logic: 1) base when one list empty return other  2) pick smaller head and recurse
def merge_sorted_lists(a, b):
    if not a: return b
    if not b: return a
    if a[0] <= b[0]:
        return [a[0]] + merge_sorted_lists(a[1:], b)
    else:
        return [b[0]] + merge_sorted_lists(a, b[1:])

if __name__ == "__main__":
    print("factorial(5) =", factorial(5))
    print("sum_list([1,2,3,4]) =", sum_list([1,2,3,4]))
    print("reverse_str('abcde') =", reverse_str('abcde'))
    print("fib_naive(6) =", fib_naive(6))
    print("fib_memo(30) =", fib_memo(30))
    print("subsets([1,2,3]) =", subsets([1,2,3]))
    print("permutations([1,2,3]) =", permutations([1,2,3]))
    print("letter_case_permutation('a1b') =", letter_case_permutation('a1b'))
    print("merge_sorted_lists([1,3,5],[2,4]) =", merge_sorted_lists([1,3,5],[2,4]))
