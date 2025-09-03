
def find_divisors(n):
    divisors = []

    sqrtN = int( n ** .5)
    for i in range(1, sqrtN + 1):
        if n % i == 0:
            divisors.append(i)
            complementaryDivisor = int(n/i)
            if (i != complementaryDivisor)	:	
                divisors.append(complementaryDivisor)
    return divisors





number = 36
print(f"Divisors of {number}: {find_divisors(number)}")
