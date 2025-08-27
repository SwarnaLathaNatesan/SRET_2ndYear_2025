def sieve_of_eratosthenes(n):
    """Return a list of prime numbers up to n."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False # 0 and 1 are not primes
    
    for current_num in range(2, int(n**0.5) + 1):
        if is_prime[current_num]:
            # Mark multiples of current_num as composite
            for multiple in range(current_num * current_num, n + 1, current_num):
                is_prime[multiple] = False
    
    # Collect prime numbers
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes

sieve_of_eratosthenes(1001)
