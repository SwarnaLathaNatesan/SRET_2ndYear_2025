def find_divisors(n):
    """Find all divisors of a given number.
    
    Args:
        n (int): The number to find divisors for
        
    Returns:
        list: A list of all divisors of n
    """
    divisors = []
    
    # Only check up to sqrt(n) for efficiency
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            # Add the complementary divisor
            if i != n / i:
                divisors.append(n / i)
    
    # Return sorted divisors
    return sorted(divisors)


def main():
    """Main function to demonstrate the divisor finder."""
    number = 36
    divisors = find_divisors(number)
    print(f"Divisors of {number}: {divisors}")


if __name__ == "__main__":
    main()
