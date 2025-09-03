import sys

list_1d = [10, 20, 30, 40, 50]
list_2d = [[1, 2, 3], [4, 5, 6]]

def format_address(addr):
    return str(addr)

print("1D list element addresses and sizes:")
for item in list_1d:
    addr = format_address(id(item))
    size = sys.getsizeof(item)
    print(f"Address: {addr}, Size: {size} bytes")

print("\n2D list inner list addresses and sizes:")
for inner_list in list_2d:
    addr = format_address(id(inner_list))
    size = sys.getsizeof(inner_list)
    print(f"Inner list address: {addr}, Size: {size} bytes")

print("\n2D list element addresses and sizes inside inner lists:")
for inner_list in list_2d:
    for item in inner_list:
        addr = format_address(id(item))
        size = sys.getsizeof(item)
        print(f"Address: {addr}, Size: {size} bytes")
    print("--- End of inner list ---")

