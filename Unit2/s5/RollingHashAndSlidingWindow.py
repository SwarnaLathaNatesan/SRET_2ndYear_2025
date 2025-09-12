def visualize_sliding_window_vs_rolling_hash():
    """
    CLEAR EXPLANATION: Sliding Window vs Rolling Hash
    """
    
    print("🎯" * 50)
    print("SLIDING WINDOW vs ROLLING HASH")
    print("UNDERSTANDING THE DIFFERENCE")
    print("🎯" * 50)
    
    print("\n📚 KEY CONCEPTS:")
    print("🔹 SLIDING WINDOW = The TECHNIQUE (what we do)")
    print("🔹 ROLLING HASH = The OPTIMIZATION (how we do it efficiently)")
    print("\n" + "="*60)
    
    text = "ABCDEFG"
    window_size = 3
    
    print(f"\n📖 Example: Text = '{text}', Window Size = {window_size}")
    print("="*60)
    
    # PART 1: SLIDING WINDOW CONCEPT
    print("\n🏠 PART 1: SLIDING WINDOW TECHNIQUE")
    print("─" * 40)
    print("💡 Concept: Move a fixed-size 'window' through the text")
    print("🎯 Goal: Examine every possible substring of size 3")
    
    print(f"\n📋 All possible windows in '{text}':")
    
    for i in range(len(text) - window_size + 1):
        window = text[i:i + window_size]
        
        # Visual representation
        visual = ""
        for j, char in enumerate(text):
            if i <= j < i + window_size:
                visual += f"[{char}]"
            else:
                visual += f" {char} "
        
        print(f"  Position {i}: {visual} → Window: '{window}'")
    
    input("\n⏸️  Press Enter to see the EFFICIENCY PROBLEM...")
    
    # PART 2: THE EFFICIENCY PROBLEM
    print("\n❌ PART 2: THE EFFICIENCY PROBLEM")
    print("─" * 40)
    print("🐌 Problem: If we need to compare windows, we do this:")
    
    print(f"\n💭 Naive approach - Calculate something for each window:")
    for i in range(len(text) - window_size + 1):
        window = text[i:i + window_size]
        # Simulate calculating hash from scratch
        hash_calc = " + ".join([f"'{char}'×base^{window_size-1-j}" for j, char in enumerate(window)])
        print(f"  Window '{window}': Calculate {hash_calc} from scratch")
    
    print("\n😱 PROBLEM: We recalculate EVERYTHING for each window!")
    print("📊 Time complexity: O(n × m) where n=text length, m=window size")
    
    input("\n⏸️  Press Enter to see the ROLLING HASH SOLUTION...")
    
    # PART 3: ROLLING HASH SOLUTION
    print("\n✅ PART 3: ROLLING HASH SOLUTION")
    print("─" * 40)
    print("🚀 Solution: REUSE calculations from previous window!")
    
    base = 3
    mod = 101
    
    print(f"\n🧮 Using base={base}, mod={mod}")
    print("💡 Key insight: When window slides, we can:")
    print("   1. Remove the leftmost character's contribution")
    print("   2. Add the new rightmost character's contribution")
    print("   3. Avoid recalculating the middle characters!")
    
    # Show the rolling process step by step
    print(f"\n🎢 ROLLING HASH DEMONSTRATION:")
    
    # Calculate first window normally
    first_window = text[:window_size]
    hash_value = 0
    
    print(f"\n🏗️  STEP 1: Calculate first window '{first_window}' normally")
    calculation_steps = []
    for i, char in enumerate(first_window):
        power = window_size - 1 - i
        contribution = ord(char) * (base ** power)
        hash_value += contribution
        calculation_steps.append(f"'{char}'×{base}^{power}")
    
    hash_value = hash_value % mod
    print(f"   Calculation: {' + '.join(calculation_steps)} = {hash_value} (mod {mod})")
    
    # Now show rolling for each subsequent window
    for i in range(1, len(text) - window_size + 1):
        print(f"\n🎢 STEP {i+1}: Roll from position {i-1} to {i}")
        
        old_window = text[i-1:i-1+window_size]
        new_window = text[i:i+window_size]
        old_char = text[i-1]
        new_char = text[i+window_size-1]
        
        print(f"   From: '{old_window}' → To: '{new_window}'")
        print(f"   Remove: '{old_char}' (leftmost)")
        print(f"   Add: '{new_char}' (new rightmost)")
        
        # Show the rolling calculation
        old_contribution = ord(old_char) * (base ** (window_size - 1))
        print(f"   Remove contribution: '{old_char}' × {base}^{window_size-1} = {old_contribution}")
        
        # Update hash: remove old, shift, add new
        hash_value = (hash_value - old_contribution) % mod
        hash_value = (hash_value * base) % mod
        hash_value = (hash_value + ord(new_char)) % mod
        
        print(f"   New hash: {hash_value}")
        print(f"   ✅ Window '{new_window}' processed with MINIMAL calculation!")
        
        input("   ⏸️  Press Enter for next step...")
    
    input("\n⏸️  Press Enter to see the COMPARISON...")
    
    # PART 4: DIRECT COMPARISON
    print("\n⚖️  PART 4: SIDE-BY-SIDE COMPARISON")
    print("="*60)
    
    print("🏠 SLIDING WINDOW (Technique):")
    print("   ✅ WHAT: Move a fixed-size window through data")
    print("   ✅ WHEN: When you need to examine all substrings of size k")
    print("   ✅ WHY: Systematic way to process data in chunks")
    print("   📋 Example uses: Finding max sum in subarray, pattern matching")
    
    print("\n🎢 ROLLING HASH (Optimization):")
    print("   ✅ WHAT: Efficient way to calculate hash for sliding windows")
    print("   ✅ WHEN: When you need to compare/process sliding windows")
    print("   ✅ WHY: Avoids recalculating hash from scratch each time")
    print("   📋 Example uses: Fast string matching, duplicate detection")
    
    print("\n🤝 TOGETHER:")
    print("   🔹 Sliding Window = Strategy")
    print("   🔹 Rolling Hash = Implementation Detail")
    print("   🔹 Rolling Hash makes Sliding Window faster!")
    
    print("\n📊 COMPLEXITY COMPARISON:")
    print("   Without Rolling Hash: O(n × m) - recalculate each window")
    print("   With Rolling Hash:    O(n)     - update incrementally")
    print(f"   For our example: {len(text)-window_size+1} windows × {window_size} chars = {(len(text)-window_size+1)*window_size} operations")
    print(f"   VS Rolling Hash: {len(text)-window_size+1} windows × 1 update = {len(text)-window_size+1} operations")


def demonstrate_analogy():
    """Perfect analogy to understand the difference"""
    
    print("\n🎭 PERFECT ANALOGY")
    print("="*50)
    
    print("🏠 SLIDING WINDOW is like:")
    print("   📖 Reading a book with a magnifying glass")
    print("   🔍 You move the magnifying glass (window) across each line")
    print("   👀 You examine each section (substring) of text")
    
    print("\n🎢 ROLLING HASH is like:")
    print("   🧮 Having a smart calculator that remembers previous calculations")
    print("   ➕ Instead of recounting everything, it:")
    print("      • Subtracts what left the view")
    print("      • Adds what entered the view")
    print("   ⚡ Makes the process much faster!")
    
    print("\n🤝 TOGETHER:")
    print("   📖 Sliding Window = Moving the magnifying glass (technique)")
    print("   🧮 Rolling Hash = Smart calculator (optimization)")
    print("   🚀 Result = Fast examination of all text sections!")


def interactive_demo():
    """Interactive demonstration"""
    
    print("\n🎮 INTERACTIVE DEMO")
    print("="*40)
    
    user_text = input("📝 Enter your text (or press Enter for 'HELLO'): ").strip()
    if not user_text:
        user_text = "HELLO"
    
    try:
        window_size = int(input("🔢 Enter window size (or press Enter for 3): ").strip() or "3")
    except:
        window_size = 3
    
    if window_size >= len(user_text):
        print("❌ Window size too large! Using size 2")
        window_size = 2
    
    print(f"\n🎯 Your Challenge: Find all windows of size {window_size} in '{user_text}'")
    
    print("\n🏠 SLIDING WINDOW VISUALIZATION:")
    for i in range(len(user_text) - window_size + 1):
        window = user_text[i:i + window_size]
        
        visual = ""
        for j, char in enumerate(user_text):
            if i <= j < i + window_size:
                visual += f"[{char}]"
            else:
                visual += f" {char} "
        
        print(f"  Step {i+1}: {visual} → '{window}'")
    
    print(f"\n🎢 ROLLING HASH MAGIC:")
    print("   Instead of recalculating each window's hash from scratch...")
    print("   We cleverly update: Remove old character + Add new character!")
    print("   This makes it super fast! ⚡")


def main():
    """Main demonstration focused on the key difference"""
    
    print("🎓" * 30)
    print("SLIDING WINDOW vs ROLLING HASH")
    print("CRYSTAL CLEAR EXPLANATION")
    print("🎓" * 30)
    
    while True:
        print("\n🎯 CHOOSE YOUR LEARNING PATH:")
        print("="*40)
        print("1. 📚 Complete Explanation (Recommended)")
        print("2. 🎭 Simple Analogy")
        print("3. 🎮 Interactive Demo")
        print("4. 🏁 Exit")
        
        choice = input("\n🤔 Choose (1-4): ").strip()
        
        if choice == "1":
            visualize_sliding_window_vs_rolling_hash()
        elif choice == "2":
            demonstrate_analogy()
        elif choice == "3":
            interactive_demo()
        elif choice == "4":
            print("\n🎉 Key Takeaway:")
            print("   🏠 Sliding Window = The technique (what)")
            print("   🎢 Rolling Hash = The optimization (how)")
            print("   🤝 Together = Fast and efficient!")
            break
        else:
            print("❌ Please choose 1-4")
        
        input("\n🔄 Press Enter to continue...")


if __name__ == "__main__":
    main()