#power of a given number by naive method and its number of iterations
def powerOfNByNaiveMethod(n, p):
    result = 1
    counter = 0
    for i in range(p):
        result = result * n
        counter = counter + 1
    print ("Iterations required are : ", counter)
    print ("Iterations required (inferred from power value) : ", p)
    return result

print(powerOfNByNaiveMethod(2,3))
print(powerOfNByNaiveMethod(7,105))


def printHalf(n):
    while n > 0:
        print(n)
        n = n // 2

print("Odd number halves:")
printHalf(105)


#convert decimal to binary
def decimalToBinary(n):
    print(bin(n))
    return bin(n).replace("0b", "")

decimalToBinary(105)


#print half and convert to binary
def printHalfAndConvertToBinary(n):
    while n > 0:
        print(f"n is {n} and its binary is {bin(n)}")
        n = n // 2


printHalfAndConvertToBinary(105)



def powerOfNByExponentialMethod(base, exponent):
    if exponent == 0:
        return 1
    
    result = 1
    n = exponent  # Work with the exponent

    while n > 0:
        if n % 2 == 1:
            result = result * base  # ✅ Multiply with result
        base = base * base  # ✅ Square the base
        n = n // 2  # ✅ Halve the exponent

    return result

# Test cases
print(powerOfNByExponentialMethod(2, 3))   # Should be 8
print(powerOfNByExponentialMethod(7, 105)) # Should be 7^105
print(powerOfNByExponentialMethod(5, 0))   # Should be 1
print("_"*100)

def powerOfNByExponentialMethodDebugMode(base, exponent):
    if exponent == 0:
        return 1
    
    result = 1
    n = exponent  # Work with the exponent
    counter = 0
    while n > 0:
        if n % 2 == 1:
            result = result * base  # ✅ Multiply with result
        base = base * base  # ✅ Square the base
        n = n // 2  # ✅ Halve the exponent
        counter = counter + 1
    
    print(f"No. of Iterations in power by exponential method: {counter}")
    binarynumber = bin(exponent).replace("0b","")
    print(f"binary number is {binarynumber} No. of binary digits {len(binarynumber)}")
    return result

# Test cases
print(powerOfNByExponentialMethodDebugMode(2, 3))   # Should be 8
print(powerOfNByExponentialMethodDebugMode(7, 105)) # Should be 7^105
print(powerOfNByExponentialMethodDebugMode(5, 0))   # Should be 1





#Performance Comparison
#find time taken to find the result
import time
start_time = time.time()
print(powerOfNByExponentialMethod(7, 105))
end_time = time.time()
print(f"Time taken to find the result thru exponential method: {end_time - start_time} seconds")

#compare time with naive method
start_time = time.time()
print(powerOfNByNaiveMethod(7,105))
end_time = time.time()
print(f"Time taken to find the result thru naive method: {end_time - start_time} seconds")


print("_"*100)
