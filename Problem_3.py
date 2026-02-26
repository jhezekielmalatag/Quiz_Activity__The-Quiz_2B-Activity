def calculate_arrangements(n, r):
    """Calculate number of arrangements using permutations formula"""
    result = 1
    for i in range(r):
        result = result * (n - i)
    return result

def factorial(n):
    """Calculate factorial of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    print("=" * 60)
    print("GUEST ARRANGEMENT CALCULATOR")
    print("=" * 60)
    
    # Input number of guests and chairs
    while True:
        try:
            n = int(input("\nEnter number of guests: "))
            r = int(input("Enter number of chairs: "))
            
            if n < r:
                print("Error: Number of guests cannot be less than chairs!")
                print("Please try again.\n")
                continue
            if n <= 0 or r <= 0:
                print("Error: Please enter positive integers!")
                continue
            break
        except ValueError:
            print("Error: Please enter valid integers!")
    
    # Display the problem
    print("\n" + "=" * 60)
    print("PROBLEM:")
    print("=" * 60)
    print(f"{n} guests need to sit in {r} chairs")
    print(f"({n - r} guests will remain standing)")
    
    # Show the calculation process
    print("\n" + "=" * 60)
    print("CALCULATION PROCESS:")
    print("=" * 60)
    
    print(f"\nUsing formula: n × (n-1) × (n-2) × ... × (n-r+1)")
    print(f"               = {n} × {n-1} × {n-2} × ... × {n-r+1}")
    print("\nStep by step:")
    
    # Show each step
    result = 1
    terms = []
    for i in range(r):
        term = n - i
        terms.append(str(term))
        result = result * term
        print(f"  Step {i+1}: Multiply by {term} → {result}")
    
    # Calculate using factorial formula for verification
    factorial_formula = factorial(n) // factorial(n - r)
    
    print(f"\n" + "-" * 40)
    print(f"Verification using factorial formula:")
    print(f"  P(n,r) = n! / (n-r)!")
    print(f"  P({n},{r}) = {n}! / ({n}-{r})!")
    print(f"  P({n},{r}) = {factorial(n)} / {factorial(n-r)}")
    print(f"  P({n},{r}) = {factorial_formula}")
    
    # Display final result
    print("\n" + "=" * 60)
    print("RESULT:")
    print("=" * 60)
    print(f"\n✓ Number of possible arrangements: {result}")
    print(f"✓ Written as: {' × '.join(terms)} = {result}")

def test_cases():
    """Run test cases to verify the program"""
    print("\n" + "=" * 60)
    print("TEST CASES:")
    print("=" * 60)
    
    test_cases = [
        (6, 4),   # Given example: 360
        (5, 3),   # 5 * 4 * 3 = 60
        (10, 2),  # 10 * 9 = 90
        (4, 4),   # 4 * 3 * 2 * 1 = 24 (4!)
        (1, 1),   # 1
        (8, 5),   # 8 * 7 * 6 * 5 * 4 = 6720
    ]
    
    for n, r in test_cases:
        result = calculate_arrangements(n, r)
        print(f"  {n} guests, {r} chairs → {result} arrangements")

if __name__ == "__main__":
    main()
    test_cases()