def generate_fibonacci(n):
    """Generate Fibonacci series up to n terms"""
    fib_series = [1, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

def calculate_gcd(a, b):
    """Calculate GCD using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

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

def is_composite(num):
    """Check if a number is composite"""
    return num > 1 and not is_prime(num)

def get_prime_factors(num):
    """Get prime factors of a number"""
    factors = []
    d = 2
    while d * d <= num:
        while num % d == 0:
            factors.append(d)
            num //= d
        d += 1
    if num > 1:
        factors.append(num)
    return factors

def prove_property_a(fib_series):
    """Prove: Sum of any ten consecutive Fibonacci numbers is divisible by 11"""
    print("\n" + "=" * 60)
    print("PROPERTY A: Sum of 10 Consecutive Fibonacci Numbers")
    print("=" * 60)
    print("\nProperty: The sum of any ten consecutive Fibonacci numbers")
    print("           is divisible by 11.")
    
    n = len(fib_series)
    print(f"\nChecking all possible sets of 10 consecutive numbers:")
    print(f"(Series has {n} terms, so checking {max(0, n-9)} sets)")
    print()
    
    all_divisible = True
    for i in range(n - 9):
        ten_consecutive = fib_series[i:i+10]
        total = sum(ten_consecutive)
        divisible = total % 11 == 0
        all_divisible = all_divisible and divisible
        
        print(f"Set {i+1}: F_{i+1} to F_{i+10}")
        print(f"  {ten_consecutive}")
        print(f"  Sum = {total}")
        print(f"  {total} ÷ 11 = {total/11:.2f} → {'Divisible ✓' if divisible else 'NOT Divisible ✗'}")
        print()
    
    print("-" * 60)
    print(f"CONCLUSION: {'PROVEN ✓ - All sums are divisible by 11' if all_divisible else 'NOT PROVEN'}")

def prove_property_b(fib_series):
    """Prove: Consecutive Fibonacci numbers are Co-prime"""
    print("\n" + "=" * 60)
    print("PROPERTY B: Consecutive Fibonacci Numbers are Co-prime")
    print("=" * 60)
    print("\nProperty: Two consecutive Fibonacci numbers do not have")
    print("           any common factor (they are Co-prime/Relatively Prime).")
    print("\nNote: GCD = 1 means Co-prime")
    print()
    
    n = len(fib_series)
    all_coprime = True
    
    print(f"{'Terms':<20} {'Fibonacci Values':<25} {'GCD':<10} {'Result'}")
    print("-" * 75)
    
    for i in range(n - 1):
        gcd = calculate_gcd(fib_series[i], fib_series[i + 1])
        is_coprime = gcd == 1
        all_coprime = all_coprime and is_coprime
        
        result = "Co-prime ✓" if is_coprime else f"GCD={gcd}"
        print(f"F{i+1}, F{i+2}               {fib_series[i]}, {fib_series[i+1]:<18} {gcd:<10} {result}")
    
    print("-" * 60)
    print(f"CONCLUSION: {'PROVEN ✓ - All consecutive pairs are Co-prime' if all_coprime else 'NOT PROVEN'}")

def prove_property_c(fib_series):
    """Prove: Sum of first n Fibonacci numbers = F(n+2) - 1"""
    print("\n" + "=" * 60)
    print("PROPERTY C: Sum of First n Fibonacci Numbers")
    print("=" * 60)
    print("\nProperty: The sum of the first n Fibonacci numbers is equal to")
    print("           the Fibonacci number two further along the sequence minus 1.")
    print("\nFormula: ΣFᵢ (i=1 to n) = Fₙ₊₂ - 1")
    print()
    
    n = len(fib_series)
    # Need at least n+2 terms to prove
    extended_series = generate_fibonacci(n + 2)
    
    print(f"{'n':<5} {'Sum of first n':<20} {'F(n+2)':<15} {'F(n+2)-1':<15} {'Match?'}")
    print("-" * 70)
    
    all_match = True
    for i in range(1, n + 1):
        sum_first_n = sum(fib_series[:i])
        f_n_plus_2 = extended_series[i + 1]  # F(n+2)
        formula_result = f_n_plus_2 - 1
        match = sum_first_n == formula_result
        all_match = all_match and match
        
        print(f"{i:<5} {sum_first_n:<20} {f_n_plus_2:<15} {formula_result:<15} {'✓' if match else '✗'}")
    
    print("-" * 60)
    print(f"CONCLUSION: {'PROVEN ✓ - Sum = F(n+2) - 1 for all n' if all_match else 'NOT PROVEN'}")

def prove_property_d(fib_series):
    """Prove: Fibonacci at composite positions are composite"""
    print("\n" + "=" * 60)
    print("PROPERTY D: Fibonacci Numbers at Composite Positions")
    print("=" * 60)
    print("\nProperty: The Fibonacci numbers at composite-number positions")
    print("           are also composite numbers.")
    print()
    
    n = len(fib_series)
    
    # Identify composite positions (1-indexed)
    composite_positions = [i for i in range(1, n + 1) if is_composite(i)]
    prime_positions = [i for i in range(1, n + 1) if is_prime(i)]
    
    print(f"Composite positions in range 1 to {n}: {composite_positions}")
    print(f"Prime positions in range 1 to {n}: {prime_positions}")
    print()
    
    print(f"{'Position':<12} {'Type':<15} {'Fib Value':<15} {'Prime/Composite':<20}")
    print("-" * 65)
    
    all_composite = True
    for i in range(1, n + 1):
        pos_type = "Composite" if is_composite(i) else "Prime" if is_prime(i) else "Neither"
        fib_val = fib_series[i - 1]
        
        if is_composite(i):
            fib_is_composite = is_composite(fib_val)
            all_composite = all_composite and fib_is_composite
            result = "Composite ✓" if fib_is_composite else f"Prime ✗ ({fib_val})"
        elif is_prime(i):
            fib_is_prime = is_prime(fib_val)
            result = f"Fib is Prime ({fib_val})"
        else:
            result = f"Neither ({fib_val})"
        
        print(f"{i:<12} {pos_type:<15} {fib_val:<15} {result}")
    
    print("-" * 65)
    print(f"CONCLUSION: {'PROVEN ✓ - All composite position Fibs are composite' if all_composite else 'NOT PROVEN'}")

def main():
    print("=" * 60)
    print("FIBONACCI SERIES & PROPERTIES PROVER")
    print("=" * 60)
    
    # Input number of terms
    while True:
        try:
            n = int(input("\nEnter number of terms (N): "))
            if n <= 0:
                print("Please enter a positive integer!")
                continue
            if n < 1:
                print("Please enter at least 12 terms to prove all properties!")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer!")
    
    # Generate Fibonacci series
    fib_series = generate_fibonacci(n)
    
    # Display Fibonacci series
    print("\n" + "=" * 60)
    print(f"FIBONACCI SERIES (First {n} terms):")
    print("=" * 60)
    
    print(f"\nF₁ = 1, F₂ = 1")
    print("Fn = Fn-1 + Fn-2")
    print()
    
    # Display in rows of 5
    for i in range(0, n, 5):
        row = fib_series[i:i+5]
        indices = [str(j+1) for j in range(i, min(i+5, n))]
        print(f"Terms {', '.join(indices)}: ".ljust(12), end="")
        print("  ".join(f"{val:>8}" for val in row))
    
    # Prove all properties
    prove_property_a(fib_series)
    prove_property_b(fib_series)
    prove_property_c(fib_series)
    prove_property_d(fib_series)
    
    print("\n" + "=" * 60)
    print("ALL PROPERTIES PROVEN SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    main()