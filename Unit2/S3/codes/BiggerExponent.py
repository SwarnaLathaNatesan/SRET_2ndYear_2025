import sys
import time

sys.set_int_max_str_digits(50000)  # Set limit above the expected digits count

start_time = time.time()

# Program to calculate 12345^6789
result = 12345 ** 6789

# Calculate number of digits
num_digits = len(str(result))

end_time = time.time()

print("Number of digits:", num_digits)
print("First 100 digits:", str(result)[:100])
print("Last 100 digits:", str(result)[-100:])
print(f"Execution time: {end_time - start_time:.4f} seconds")


print("First 100 digits:", str(result))
