import sys

def analyze_dict_behavior():
    print("=== PYTHON DICTIONARY HASHING DEMONSTRATION ===\n")
    
    # Create an empty dictionary
    my_dict = {}
    print(f"1. Empty dictionary created")
    print(f"   Size: {sys.getsizeof(my_dict)} bytes")
    print(f"   Length: {len(my_dict)}")
    print()
    
    # Insert unique keys
    print("2. Inserting unique keys:")
    keys_to_insert = [10, 20, 30, 40, 50]
    for key in keys_to_insert:
        my_dict[key] = f"value_{key}"
        print(f"   Added key {key}: hash({key}) = {hash(key)}")
        print(f"   Current dict: {list(my_dict.keys())}")
    print()
    
    # Demonstrate duplicate key handling
    print("3. Demonstrating duplicate key handling:")
    print(f"   Before duplicate: my_dict[20] = '{my_dict[20]}'")
    my_dict[20] = "NEW_VALUE_20"  # This overwrites the previous value
    print(f"   After duplicate: my_dict[20] = '{my_dict[20]}'")
    print(f"   All keys remain unique: {list(my_dict.keys())}")
    print()
    
    # Show hash values and internal workings
    print("4. Hash values and internal analysis:")
    for key in my_dict.keys():
        print(f"   Key: {key:2d} -> Hash: {hash(key):10d} -> Hash % 8: {hash(key) % 8}")
    print()
    
    # Demonstrate various data types as keys - CORRECTED SYNTAX
    print("5. Different data types as keys:")
    mixed_dict = {}
    mixed_dict[1] = "integer key"
    mixed_dict["hello"] = "string key"
    mixed_dict[3.14] = "float key"        # Corrected syntax
    mixed_dict[(1, 2)] = "tuple key"      # Corrected syntax
    mixed_dict[True] = "boolean key"
    mixed_dict[None] = "None key"
    mixed_dict[frozenset([1, 2, 3])] = "frozenset key"
    
    for key, value in mixed_dict.items():
        print(f"   {type(key).__name__:10} {repr(key):15} -> hash: {hash(key):12d} -> value: '{value}'")
    print()
    
    # Show dictionary resizing behavior
    print("6. Dictionary resizing demonstration:")
    growth_dict = {}
    print("   Initial empty dict size:", sys.getsizeof(growth_dict), "bytes")
    
    for i in range(20):
        growth_dict[i] = f"item_{i}"
        if i in [0, 5, 10, 15, 19]:
            print(f"   After {i+1:2d} items: {sys.getsizeof(growth_dict):4d} bytes, {len(growth_dict)} items")
    print()
    
    # Collision demonstration
    print("7. Hash collision demonstration:")
    # Create objects with same hash but different values
    class TestKey:
        def __init__(self, value, hash_value):
            self.value = value
            self.hash_value = hash_value
        
        def __hash__(self):
            return self.hash_value
        
        def __eq__(self, other):
            if isinstance(other, TestKey):
                return self.value == other.value
            return False
        
        def __repr__(self):
            return f"TestKey({self.value})"
    
    # Create keys with same hash but different values
    key1 = TestKey("first", 123)
    key2 = TestKey("second", 123)  # Same hash, different value
    key3 = TestKey("first", 123)   # Same hash, same value (equal to key1)
    
    collision_dict = {}
    collision_dict[key1] = "value1"
    print(f"   Added {key1} -> '{collision_dict[key1]}'")
    
    collision_dict[key2] = "value2"  # Different key, same hash -> collision resolved
    print(f"   Added {key2} -> '{collision_dict[key2]}'")
    
    # This will overwrite because key3 equals key1
    collision_dict[key3] = "value3"
    print(f"   Added {key3} -> '{collision_dict[key3]}' (overwrote key1)")
    print(f"   Final collision dict keys: {list(collision_dict.keys())}")
    print()
    
    # Dictionary operations
    print("8. Common dictionary operations:")
    
    # get() method
    print(f"   my_dict.get(20): '{my_dict.get(20)}'")
    print(f"   my_dict.get(999, 'DEFAULT'): '{my_dict.get(999, 'DEFAULT')}'")
    
    # setdefault()
    result = my_dict.setdefault(60, "default_value")
    print(f"   setdefault(60): '{result}' -> dict now has key 60")
    
    # update()
    my_dict.update({70: "value_70", 80: "value_80"})
    print(f"   update() added keys: {[k for k in my_dict.keys() if k in [70, 80]]}")
    
    # pop()
    removed = my_dict.pop(20)
    print(f"   pop(20) removed: '{removed}'")
    
    # keys(), values(), items()
    print(f"   Keys: {list(my_dict.keys())[:5]}...")
    print(f"   Values: {list(my_dict.values())[:5]}...")
    print(f"   Items: {list(my_dict.items())[:5]}...")
    print()
    
    # Memory efficiency
    print("9. Memory efficiency comparison:")
    list_size = sys.getsizeof(list(range(100)))
    dict_size = sys.getsizeof(dict.fromkeys(range(100)))
    print(f"   List of 100 integers: {list_size} bytes")
    print(f"   Dict with 100 keys: {dict_size} bytes")
    print(f"   Memory overhead: {dict_size - list_size} bytes extra for dict")

def demonstrate_hash_uniqueness():
    print("\n" + "="*60)
    print("HASH UNIQUENESS AND COLLISION ANALYSIS")
    print("="*60)
    
    # Show that equal objects have equal hashes
    print("1. Equal objects have equal hashes:")
    a = "hello"
    b = "hello"
    print(f"   a = '{a}', b = '{b}'")
    print(f"   hash(a) = {hash(a)}, hash(b) = {hash(b)}")
    print(f"   a == b: {a == b}, hash(a) == hash(b): {hash(a) == hash(b)}")
    print()
    
    # Show that different objects can have same hash (collision)
    print("2. Hash collisions (different objects, same hash):")
    # Find some collisions
    found_collisions = []
    test_values = []
    
    for i in range(1000):
        h = hash(str(i))
        if len(test_values) > 0 and h == test_values[-1][1]:
            found_collisions.append((test_values[-1][0], i, h))
        test_values.append((i, h))
        
        if len(found_collisions) >= 3:
            break
    
    for val1, val2, hash_val in found_collisions:
        print(f"   Collision: hash('{val1}') = {hash_val} == hash('{val2}')")
    print()
    
    # Immutable requirement for keys
    print("3. Immutability requirement for keys:")
    try:
        mutable_key = [1, 2, 3]
        bad_dict = {mutable_key: "will fail"}  # This will raise TypeError
    except TypeError as e:
        print(f"   Error using list as key: {e}")
    
    # But tuples (immutable) work fine
    tuple_key = (1, 2, 3)
    good_dict = {tuple_key: "works fine"}
    print(f"   Tuple key works: {tuple_key} -> '{good_dict[tuple_key]}'")
    
    # frozenset also works (immutable)
    frozen_key = frozenset([1, 2, 3])
    good_dict[frozen_key] = "frozenset works"
    print(f"   Frozenset key works: {frozen_key} -> '{good_dict[frozen_key]}'")

def demonstrate_invalid_keys():
    print("\n" + "="*60)
    print("INVALID KEY TYPES DEMONSTRATION")
    print("="*60)
    
    print("1. Lists cannot be used as keys (mutable):")
    try:
        invalid_dict = {[1, 2, 3]: "will fail"}
    except TypeError as e:
        print(f"   Error: {e}")
    
    print("\n2. Sets cannot be used as keys (mutable):")
    try:
        invalid_dict = {{1, 2, 3}: "will fail"}
    except TypeError as e:
        print(f"   Error: {e}")
    
    print("\n3. Dictionaries cannot be used as keys (mutable):")
    try:
        invalid_dict = {{"a": 1}: "will fail"}
    except TypeError as e:
        print(f"   Error: {e}")
    
    print("\n4. But their immutable counterparts work:")
    valid_dict = {
        tuple([1, 2, 3]): "tuple works",
        frozenset({1, 2, 3}): "frozenset works"
    }
    print(f"   Valid keys: {list(valid_dict.keys())}")

if __name__ == "__main__":
    analyze_dict_behavior()
    demonstrate_hash_uniqueness()
    demonstrate_invalid_keys()
    
    print("\n" + "="*60)
    print("KEY TAKEAWAYS:")
    print("="*60)
    print("1. ✅ Python dictionaries use hashing for O(1) average access")
    print("2. ✅ Duplicate keys overwrite previous values")
    print("3. ✅ Keys must be hashable and immutable")
    print("4. ✅ Dictionary automatically resizes when needed")
    print("5. ✅ Hash collisions are handled internally")
    print("6. ✅ Equal objects must have equal hash values")
    print("7. ✅ Different objects can have same hash (collisions)")
    print("8. ❌ Mutable objects (lists, sets, dicts) cannot be keys")
    print("9. ✅ Use tuple() or frozenset() for compound keys")
