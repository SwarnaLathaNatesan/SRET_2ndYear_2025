# Python program to check for prime number (optimized)
def is_prime_optimized(n):

    if n <= 1: return False, 0
    if n == 2: return True, 0
    if n % 2 == 0: return False, 1
    iterations = 0


    for i in range(3, int(n**0.5) + 1, 2):

		iterations += 1

        if n % i == 0 :
         return False, iterations
    return True, iterations






number = 1001
result, iters = is_prime_optimized(number)
print(f"{number} is prime: {result}")
print(f"Iterations required: {iters}")


totalIter = 0
primeCounter = 0
for i in range (2, 1001):
    result, iters = is_prime_optimized(i)
    totalIter = totalIter + iters
    if result 
	primeCounter = primeCounter+1
	
    print(f"{i} is prime: {result} , {primeCounter}")

print(f" total Iterations required: {totalIter}")
