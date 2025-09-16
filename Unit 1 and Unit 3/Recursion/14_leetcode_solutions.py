# 509. Fibonacci Number (Easy)
# Core logic: Base case for n == 0 or 1. Otherwise return recursive sum of previous two.
# This directly follows the recursive definition of Fibonacci.
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print("Fibonacci(5):", fib(5))
print("Fibonacci(7):", fib(7))


# 344. Reverse String (Easy)
# Core logic: Swap first and last elements, then recursively reverse the inner substring.
# Stop recursion when left >= right.
def reverseString(s):
    def helper(left, right):
        if left >= right:
            return
        s[left], s[right] = s[right], s[left]
        helper(left+1, right-1)
    helper(0, len(s)-1)
    return s

print("Reverse String [h,e,l,l,o]:", reverseString(list("hello")))
print("Reverse String [r,a,c,e]:", reverseString(list("race")))


# 21. Merge Two Sorted Lists (Easy, Recursive)
# Core logic: Pick the smaller node and recursively merge the rest.
# Base case when one list is empty, return the other.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2

# Helper function to build and print lists
def build_list(arr):
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def print_list(node):
    vals = []
    while node:
        vals.append(node.val)
        node = node.next
    return vals

list1 = build_list([1,2,4])
list2 = build_list([1,3,4])
merged = mergeTwoLists(list1, list2)
print("Merged List:", print_list(merged))


# 784. Letter Case Permutation (Medium)
# Core logic: For each character, branch into lowercase and uppercase if it's a letter.
# Use recursion to explore all possibilities until the end of the string.
def letterCasePermutation(s):
    res = []

    def backtrack(i, combination):
        if i == len(s):
            res.append(combination)
            return
        if s[i].isalpha():
            backtrack(i+1, combination + s[i].lower())
            backtrack(i+1, combination + s[i].upper())
        else:
            backtrack(i+1, combination + s[i])

    backtrack(0, "")
    return res

print("Letter Case Permutations of 'a1b2':", letterCasePermutation("a1b2"))
print("Letter Case Permutations of '3z4':", letterCasePermutation("3z4"))



'''
def letterCasePermutation(s):
    res = []
    stack = [(0, "")]   # (index, current_combination)
    
    while stack:
        i, combination = stack.pop()
        if i == len(s):
            res.append(combination)
        else:
            if s[i].isalpha():
                stack.append((i+1, combination + s[i].lower()))
                stack.append((i+1, combination + s[i].upper()))
            else:
                stack.append((i+1, combination + s[i]))
    return res

'''