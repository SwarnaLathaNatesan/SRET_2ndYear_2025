# Python program to check for prime number (optimized)
def is_prime_optimized(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False

    for i in range(3, int(n**0.5) + 1, 2):

        if n % i == 0 :
            return False
    return True

number = 1001
result = is_prime_optimized(number)
print(f"{number} is prime: {result}")



#inefficient method. instead use sieve of eratosthene 
primeCounter = 0
for i in range (2, 1001):
    result = is_prime_optimized(i)
    if result :
	    primeCounter = primeCounter+1
	
    print(f"{i} is prime: {result} ")
print(f"Total prime numbers {primeCounter}")
