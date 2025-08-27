def gcd_euclidean(a, b):
    iterations = 0
    while b:
        iterations += 1
        a, b = b, a % b
    return a, iterations

num1, num2 = 56, 98
result, iters = gcd_euclidean(num1, num2)
print(f"GCD of {num1} and {num2} is {result}")
print(f"Iterations required: {iters}")


result, iters = gcd_euclidean(24, 36)
print(f"GCD of {num1} and {num2} is {result}")
print(f"Iterations required: {iters}")




result, iters = gcd_euclidean(36, 24)
print(f"GCD of {num1} and {num2} is {result}")
print(f"Iterations required: {iters}")



result, iters = gcd_euclidean(36, 0)
print(f"GCD of {num1} and {num2} is {result}")
print(f"Iterations required: {iters}")



result, iters = gcd_euclidean(0, 36)
print(f"GCD of {num1} and {num2} is {result}")
print(f"Iterations required: {iters}")

'''
10, 100
100, 10%100
100, 10
10, 100%10
'''
result, iters = gcd_euclidean(10**9, 10**18)
print(f"GCD of {num1} and {num2} is {result}")
print(f"Iterations required: {iters}")

num1 = 36
num2 = 24
gcd, iters = gcd_euclidean(num1, num2)
lcm = (num1 * num2 )/gcd

