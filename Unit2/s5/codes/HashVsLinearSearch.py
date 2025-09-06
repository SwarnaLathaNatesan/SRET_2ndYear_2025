class HashTable:
    """Simulate a hash table with linear probing to count actual probes"""
    
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.count = 0
    
    def _hash(self, key):
        """Simple hash function"""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert a key-value pair and return number of probes"""
        probes = 0
        index = self._hash(key)
        
        # Handle collisions with linear probing
        while self.table[index] is not None:
            probes += 1
            index = (index + 1) % self.size
        
        self.table[index] = (key, value)
        self.count += 1
        return probes
    
    def search(self, key):
        """Search for a key and return (value, actual_probes)"""
        probes = 0
        index = self._hash(key)
        initial_index = index
        
        while self.table[index] is not None:
            probes += 1
            if self.table[index][0] == key:
                return self.table[index][1], probes
            
            index = (index + 1) % self.size
            # If we've searched the entire table
            if index == initial_index:
                break
        
        return None, probes

def linear_search(arr, target):
    """Perform linear search and count probes"""
    probes = 0
    for i in range(len(arr)):
        probes += 1
        if arr[i] == target:
            return i, probes
    return -1, probes

def simulate_dictionary_maintenance(elements):
    """Simulate building and searching a hash table"""
    # Create hash table (simulating dictionary)
    hash_table = HashTable(size=len(elements) * 2)  # Larger size to reduce collisions
    
    print("Building hash table (simulated dictionary):")
    print("-" * 50)
    
    total_insert_probes = 0
    for i, element in enumerate(elements):
        insert_probes = hash_table.insert(element, f"Found at original position {i}")
        total_insert_probes += insert_probes
        print(f"Inserted {element}: {insert_probes} insertion probes")
    
    print(f"\nTotal insertion probes: {total_insert_probes}")
    print(f"Average insertion probes: {total_insert_probes/len(elements):.2f}")
    print("-" * 50)
    
    return hash_table

def compare_searches(elements, hash_table):
    """Compare linear search vs hash table search"""
    print(f"\n{'Element':<10} {'Linear Probes':<15} {'Hash Probes':<15} {'Winner':<10}")
    print("-" * 50)
    
    total_linear_probes = 0
    total_hash_probes = 0
    
    for target in elements:
        # Linear search
        linear_index, linear_probes = linear_search(elements, target)
        total_linear_probes += linear_probes
        
        # Hash table search
        hash_result, hash_probes = hash_table.search(target)
        total_hash_probes += hash_probes
        
        # Determine winner
        if linear_probes < hash_probes:
            winner = "Linear"
        elif hash_probes < linear_probes:
            winner = "Hash"
        else:
            winner = "Tie"
        
        print(f"{target:<10} {linear_probes:<15} {hash_probes:<15} {winner:<10}")
    
    print("-" * 50)
    print(f"{'TOTAL':<10} {total_linear_probes:<15} {total_hash_probes:<15}")
    print(f"{'AVERAGE':<10} {total_linear_probes/len(elements):<15.2f} {total_hash_probes/len(elements):<15.2f}")
    
    return total_linear_probes, total_hash_probes

def test_collision_scenario():
    """Test with elements that might cause hash collisions"""
    print("\n=== TEST: Potential Collision Scenario ===")
    
    # Elements that might hash to same or nearby buckets
    elements = [10, 20, 30, 40, 15, 25, 35, 45]  # Some might collide
    
    hash_table = simulate_dictionary_maintenance(elements)
    compare_searches(elements, hash_table)

def test_large_dataset():
    """Test with a larger dataset"""
    print("\n=== TEST: Large Dataset ===")
    
    elements = list(range(1, 101))  # 1 to 100
    
    hash_table = simulate_dictionary_maintenance(elements)
    linear_probes, hash_probes = compare_searches(elements, hash_table)
    
    efficiency_ratio = linear_probes / hash_probes
    print(f"\nEfficiency ratio (Linear/Hash): {efficiency_ratio:.1f}x")
    print(f"Hash table is {efficiency_ratio:.1f} times more efficient!")

def interactive_test():
    """Interactive test with custom elements"""
    print("\n=== INTERACTIVE TEST ===")
    
    elements = input("Enter elements separated by spaces (e.g., '5 2 8 1 9'): ")
    elements = [int(x) for x in elements.split()]
    
    print(f"\nTesting with elements: {elements}")
    
    hash_table = simulate_dictionary_maintenance(elements)
    compare_searches(elements, hash_table)
    
    # Test searching for specific element
    target = int(input(f"\nEnter element to search for: "))
    
    linear_index, linear_probes = linear_search(elements, target)
    hash_result, hash_probes = hash_table.search(target)
    
    print(f"\nSearching for {target}:")
    print(f"Linear Search: {linear_probes} probes, found at index {linear_index}")
    print(f"Hash Search: {hash_probes} probes, result: {hash_result}")

def analyze_hash_distribution(elements):
    """Analyze hash distribution to understand collision patterns"""
    print(f"\n=== HASH DISTRIBUTION ANALYSIS ===")
    
    hash_table = HashTable(size=len(elements) * 2)
    hash_counts = {}
    
    for element in elements:
        hash_val = hash_table._hash(element)
        hash_counts[hash_val] = hash_counts.get(hash_val, 0) + 1
    
    print("Hash bucket distribution:")
    for bucket, count in sorted(hash_counts.items()):
        print(f"Bucket {bucket}: {count} element(s)")
    
    collisions = sum(1 for count in hash_counts.values() if count > 1)
    print(f"\nTotal collisions: {collisions}")
    print(f"Collision rate: {collisions/len(elements)*100:.1f}%")

# Main program
if __name__ == "__main__":
    # Test 1: Small list
    print("=== TEST 1: Small List ===")
    elements1 = [15, 10, 5, 20, 25, 30, 35, 40]
    hash_table1 = simulate_dictionary_maintenance(elements1)
    compare_searches(elements1, hash_table1)
    
    # Test 2: Medium list with potential collisions
    test_collision_scenario()
    
    # Test 3: Large dataset
    test_large_dataset()
    
    # Analyze hash distribution
    analyze_hash_distribution(list(range(1, 21)))
    
    # Interactive test
    interactive_test()