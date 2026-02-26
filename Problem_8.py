def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def find_prime_pairs(n):
    """Find all pairs of prime numbers that sum to n"""
    pairs = []
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            pairs.append((i, n - i))
    return pairs

def main():
    print("=" * 60)
    print("SUM OF TWO PRIMES CHECKER")
    print("=" * 60)
    print("\nThis program checks if a number can be expressed")
    print("as the sum of two prime numbers.")
    print("\n(Based on Goldbach's Conjecture)")
    
    # Input number
    while True:
        try:
            n = int(input("\nEnter a positive integer: "))
            if n <= 2:
                print("Please enter a number greater than 2!")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer!")
    
    print("\n" + "=" * 60)
    print("CHECKING:")
    print("=" * 60)
    print(f"\nNumber to check: {n}")
    print(f"Range to check: 2 to {n//2}")
    
    # Find prime pairs
    pairs = find_prime_pairs(n)
    
    # Display results
    print("\n" + "=" * 60)
    print("RESULT:")
    print("=" * 60)
    
    if pairs:
        print(f"\n✓ YES! {n} can be expressed as sum of two primes:")
        print(f"\n  {n} = ", end="")
        
        for i, (p, q) in enumerate(pairs):
            if i > 0:
                print(f"\n       = ", end="")
            print(f"{p} + {q}")
            
            # Show verification
            print(f"       = {p} + {q} = {p + q}")
        
        print(f"\n  Total combinations found: {len(pairs)}")
        
        # Show all prime pairs in a table
        print("\n" + "-" * 40)
        print("All prime pairs that sum to {n}:")
        print("-" * 40)
        print(f"{'Prime 1':<12} {'Prime 2':<12} {'Sum':<10}")
        print("-" * 34)
        for p, q in pairs:
            print(f"{p:<12} {q:<12} {p+q:<10}")
    else:
        print(f"\n✗ NO! {n} cannot be expressed as sum of two primes")
    
    # Additional information
    print("\n" + "=" * 60)
    print("PRIME CHECK FOR INDIVIDUAL NUMBERS:")
    print("=" * 60)
    print(f"\nChecking all numbers from 2 to {n-2}:")
    print(f"\n{'Number':<12} {'Is Prime?'}")
    print("-" * 25)
    for i in range(2, min(n, 21)):
        status = "Prime ✓" if is_prime(i) else "Not Prime"
        print(f"{i:<12} {status}")
    


def test_cases():
    """Run test cases"""
    print("\n" + "=" * 60)
    print("TEST CASES:")
    print("=" * 60)
    
    test_cases = [4, 5, 10, 17, 20, 34, 100]
    
    for n in test_cases:
        pairs = find_prime_pairs(n)
        if pairs:
            print(f"\n{n}: {pairs[0][0]} + {pairs[0][1]} = {n} ({len(pairs)} combinations)")
        else:
            print(f"\n{n}: Cannot be expressed as sum of two primes")

if __name__ == "__main__":
    main()
    test_cases()