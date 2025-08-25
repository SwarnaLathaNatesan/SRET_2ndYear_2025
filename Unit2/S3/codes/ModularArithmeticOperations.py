# Modular Arithmetic Operations

def mod_add(a, b, m):
    return (a % m + b % m) % m

def mod_sub(a, b, m):
    # Add m before mod to handle negative results
    return ((a % m) - (b % m) + m) % m

def mod_mul(a, b, m):
    return (a % m * b % m) % m

# Fast Exponentiation (Binary Exponentiation) with Modular Arithmetic
def mod_pow(base, exponent, mod):
    result = 1
    base = base % mod
    while exponent > 0:
        # If exponent is odd, multiply by base
        if exponent & 1:
            result = (result * base) % mod
        # Square the base
        base = (base * base) % mod
        # Right shift exponent by 1 (divide by 2)
        exponent >>= 1
    return result

# Bitwise Operator Programs

def bitwise_xor(a, b):
    return a ^ b

def bitwise_and(a, b):
    return a & b

def bitwise_or(a, b):
    return a | b

# Power of 2 Using Bitwise Shift
def power_of_two(n):
    # 1 left shifted by n is 2^n
    return 1 << n


# Example Usage

if __name__ == "__main__":

    a = 27
    b = 15
    mod = 4

    print("Modular Arithmetic Examples:")
    print(f"({a} + {b}) % {mod} =", mod_add(a, b, mod))
    print(f"({a} - {b}) % {mod} =", mod_sub(a, b, mod))
    print(f"({a} * {b}) % {mod} =", mod_mul(a, b, mod))

    base = 7
    exponent = 5
    mod = 11

    print("\nFast Exponentiation Example:")
    print(f"{base}^{exponent} % {mod} =", mod_pow(base, exponent, mod))

    x = 12
    y = 25

    print("\nBitwise Operations Examples:")
    print(f"{x} XOR {y} =", bitwise_xor(x, y))
    print(f"{x} AND {y} =", bitwise_and(x, y))
    print(f"{x} OR {y} =", bitwise_or(x, y))

    power = 3
    print(f"\n2 to the power of {power} using bitwise shift:", power_of_two(power))
