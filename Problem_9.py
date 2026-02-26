def find_factors(n):
    """Find all factors of a given number"""
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def find_factors_optimized(n):
    """Find factors using optimized method (O(√n))"""
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def classify_number(n, sum_of_factors):
    """Classify the number based on sum of factors"""
    # Exclude the number itself for classification
    proper_sum = sum_of_factors - n
    
    if proper_sum == n:
        return "Perfect Number"
    elif proper_sum > n:
        return "Abundant Number"
    else:
        return "Deficient Number"

def display_factor_details(factors, n):
    """Display detailed information about factors"""
    print("\n" + "=" * 60)
    print("FACTOR DETAILS:")
    print("=" * 60)
    
    # Count
    print(f"\nNumber of factors: {len(factors)}")
    
    # List all factors
    print(f"\nAll factors of {n}:")
    print("  ", factors)
    
    # Display as pairs
    print(f"\nFactor pairs:")
    for i in range(len(factors) // 2):
        f1 = factors[i]
        f2 = factors[-(i+1)]
        print(f"  {f1} × {f2} = {f1 * f2}")
    
    # If odd number of factors, show middle pair
    if len(factors) % 2 != 0:
        mid = len(factors) // 2
        print(f"  {factors[mid]} × {factors[mid]} = {factors[mid] ** 2}")

def main():
    print("=" * 60)
    print("FACTOR FINDER PROGRAM")
    print("=" * 60)
    print("\nThis program finds all factors (divisors) of a number.")
    
    # Input number
    while True:
        try:
            n = int(input("\nEnter a positive integer: "))
            if n <= 0:
                print("Please enter a positive integer!")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer!")
    
    print("\n" + "=" * 60)
    print("FINDING FACTORS:")
    print("=" * 60)
    print(f"\nFinding factors of {n}...")
    print(f"Checking from 1 to {n}...")
    
    # Find factors
    factors = find_factors(n)
    
    # Display results
    print("\n" + "=" * 60)
    print("RESULTS:")
    print("=" * 60)
    print(f"\n✓ Factors of {n}: {factors}")
    
    # Display factor details
    display_factor_details(factors, n)
    
    # Sum of factors
    sum_factors = sum(factors)
    print("\n" + "=" * 60)
    print("ADDITIONAL INFORMATION:")
    print("=" * 60)
    print(f"\nSum of all factors: {sum_factors}")
    print(f"Product of all factors: ", end="")
    
    # Product of factors: n^(n_factors/2)
    if len(factors) % 2 == 0:
        product = n ** (len(factors) // 2)
    else:
        product = n ** (len(factors) // 2) * int(n ** 0.5)
    print(product)
    
    # Prime check
    print(f"\nIs {n} a prime number?", "Yes ✓" if is_prime(n) else "No")
    
    # Number classification
    classification = classify_number(n, sum_factors)
    proper_sum = sum_factors - n
    print(f"\nNumber Classification:")
    print(f"  Sum of proper factors: {proper_sum}")
    print(f"  The number itself: {n}")
    print(f"  Classification: {classification}")
    
    # Show prime factors
    print("\n" + "=" * 60)
    print("PRIME FACTORIZATION:")
    print("=" * 60)
    
    def get_prime_factors(n):
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors
    
    prime_factors = get_prime_factors(n)
    print(f"\nPrime factors: {prime_factors}")
    print(f"Prime factorization: {' × '.join(map(str, prime_factors))} = {n}")

def test_cases():
    """Run test cases"""
    print("\n" + "=" * 60)
    print("TEST CASES:")
    print("=" * 60)
    
    test_cases = [1, 6, 12, 28, 100, 17]
    
    for n in test_cases:
        factors = find_factors(n)
        print(f"\n{n}: {factors} ({len(factors)} factors)")

if __name__ == "__main__":
    main()
    test_cases()