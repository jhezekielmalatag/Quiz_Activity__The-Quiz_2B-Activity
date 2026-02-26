def generate_series(n):
    """Generate the series and calculate sum"""
    series = []
    total_sum = 0
    
    for term in range(1, n + 1):
        if term == 1:
            value = 1
            operator = "+"
        elif term % 2 == 0:  # Even term: positive
            value = term / (term + 1)
            operator = "+"
        else:  # Odd term (except first): negative
            value = -(term / (term + 1))
            operator = "-"
        
        series.append({
            'term': term,
            'value': value,
            'operator': operator,
            'fraction': f"{term}/{term+1}" if term > 1 else "1/1"
        })
        total_sum += value
    
    return series, total_sum

def main():
    print("=" * 60)
    print("SERIES SUM CALCULATOR")
    print("=" * 60)
    print("\nThe Series:")
    print("  1 + 2/3 - 3/4 + 4/5 - 5/6 + ...")
    print("\nPattern:")
    print("  • Term 1: 1")
    print("  • Even terms: +n/(n+1)")
    print("  • Odd terms (n>1): -n/(n+1)")
    
    # Input number of terms
    while True:
        try:
            n = int(input("\nEnter number of terms (N): "))
            if n <= 0:
                print("Please enter a positive integer!")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer!")
    
    # Generate series
    series, total_sum = generate_series(n)
    
    # Display all terms
    print("\n" + "=" * 60)
    print(f"SERIES TERMS (1 to {n}):")
    print("=" * 60)
    
    print(f"\n{'Term':<10} {'Fraction':<15} {'Operator':<12} {'Value':<20}")
    print("-" * 60)
    
    for item in series:
        term = item['term']
        frac = item['fraction']
        op = item['operator']
        val = item['value']
        
        if term == 1:
            print(f"{term:<10} {frac:<15} {'+' if op == '+' else '':<12} {val:<20.10f}")
        else:
            print(f"{term:<10} {frac:<15} {op:<12} {val:<20.10f}")
    
    # Display as equation
    print("\n" + "=" * 60)
    print("SERIES EXPANSION:")
    print("=" * 60)
    
    equation = []
    for item in series:
        if item['term'] == 1:
            equation.append("1")
        else:
            equation.append(f"{item['operator']} {item['fraction']}")
    
    print("\n  " + " ".join(equation[:5]))
    if len(equation) > 5:
        print("  " + " ".join(equation[5:10]))
        if len(equation) > 10:
            print("  ...")
    
    # Display sum
    print("\n" + "=" * 60)
    print("CALCULATION:")
    print("=" * 60)
    
    print("\n  Adding all terms step by step:")
    running_sum = 0
    for item in series:
        if item['term'] == 1:
            print(f"  Term {item['term']}: {item['value']:.10f}")
        else:
            print(f"  Term {item['term']}: {running_sum:.10f} + ({item['value']:.10f}) = {running_sum + item['value']:.10f}")
        running_sum += item['value']
    
    print("\n" + "=" * 60)
    print("RESULT:")
    print("=" * 60)
    print(f"\n  Number of terms: {n}")
    print(f"  Sum of all {n} terms: {total_sum:.10f}")
    print(f"  (Rounded to 6 decimal places: {total_sum:.6f})")

def verify_pattern():
    """Verify the pattern with first few terms"""
    print("\n" + "=" * 60)
    print("PATTERN VERIFICATION:")
    print("=" * 60)
    
    print("\n  Term 1:  1     =  1/1  → +1")
    print("  Term 2:  2/3    → +2/3")
    print("  Term 3:  -3/4   → -3/4")
    print("  Term 4:  +4/5  → +4/5")
    print("  Term 5:  -5/6  → -5/6")
    print("  Term 6:  +6/7  → +6/7")
    print("  Term 7:  -7/8  → -7/8")

def test_cases():
    """Run test cases"""
    print("\n" + "=" * 60)
    print("TEST CASES:")
    print("=" * 60)
    
    test_cases = [1, 2, 5, 10, 20]
    
    for n in test_cases:
        series, total_sum = generate_series(n)
        print(f"\n  N = {n}: Sum = {total_sum:.10f}")

if __name__ == "__main__":
    main()
    verify_pattern()
    test_cases()