def sum_of_digits_iterative(n):
    """Calculate sum of digits using iteration"""
    num = abs(n)  # Handle negative numbers
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

def sum_of_digits_string(n):
    """Calculate sum of digits using string conversion"""
    num_str = str(abs(n))
    total = 0
    for digit in num_str:
        total += int(digit)
    return total

def sum_of_digits_recursive(n):
    """Calculate sum of digits using recursion"""
    n = abs(n)
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits_recursive(n // 10)

def main():
    print("=" * 60)
    print("SUM OF DIGITS CALCULATOR")
    print("=" * 60)
    print("\nThis program calculates the sum of digits of a number.")
    print("Example: 123 → 1 + 2 + 3 = 6")
    
    # Input number
    while True:
        try:
            n = input("\nEnter a number: ").strip()
            
            # Handle negative numbers
            is_negative = n.startswith('-')
            if is_negative:
                n = n[1:]
            
            # Validate input
            if n == '' or not n.replace('.', '').isdigit():
                print("Error: Please enter a valid number!")
                continue
            
            # Convert to appropriate type
            if '.' in n:
                num = float(n)
            else:
                num = int(n)
            
            break
        except ValueError:
            print("Error: Please enter a valid number!")
    
    # Store original for display
    original = n
    if '.' in n:
        num = float(n)
    else:
        num = int(n)
    
    print("\n" + "=" * 60)
    print("CALCULATION:")
    print("=" * 60)
    
    # Display the process
    print(f"\nInput number: {n}")
    print(f"\nProcess: ", end="")
    
    # Show digit-by-digit addition
    num_str = str(abs(num))
    if '.' in str(num):
        # Handle decimal numbers
        integer_part, decimal_part = str(abs(num)).split('.')
        digits = list(integer_part)
        digits.extend(list(decimal_part))
    else:
        digits = list(num_str)
    
    print(" + ".join(digits))
    
    # Calculate using different methods
    sum_iterative = sum_of_digits_iterative(num)
    sum_string = sum_of_digits_string(num)
    sum_recursive = sum_of_digits_recursive(int(num))
    
    print(f"        = ", end="")
    
    if '.' in str(num):
        print(f"{sum_string}")
    else:
        print(f"{' + '.join(digits)}")
        print(f"        = {sum_iterative}")
    
    # Display results
    print("\n" + "=" * 60)
    print("RESULT:")
    print("=" * 60)
    print(f"\n✓ Sum of digits of {n} = {sum_iterative}")
    
    # Show verification using different methods
    print("\n" + "=" * 60)
    print("VERIFICATION (Multiple Methods):")
    print("=" * 60)
    
    if not ('.' in str(num)):
        print(f"\nMethod 1 (Iterative): {sum_iterative}")
        print(f"Method 2 (String):    {sum_string}")
        print(f"Method 3 (Recursive): {sum_recursive}")
        print(f"\nAll methods give: {sum_iterative}")
    else:
        print(f"\nString method result: {sum_string}")
    
    # Show digit analysis
    print("\n" + "=" * 60)
    print("DIGIT ANALYSIS:")
    print("=" * 60)
    print(f"\n{'Digit':<12} {'Position':<15} {'Value':<10}")
    print("-" * 40)
    
    for i, digit in enumerate(num_str):
        position = len(num_str) - i
        print(f"{digit:<12} {position:<15} {int(digit):<10}")

def test_cases():
    """Run test cases"""
    print("\n" + "=" * 60)
    print("TEST CASES:")
    print("=" * 60)
    
    test_cases = [123, 4567, 1000, 999999, 7, 0, 11111]
    
    for n in test_cases:
        result = sum_of_digits_iterative(n)
        print(f"\n{n}: {result}")
        # Show process
        digits = list(str(n))
        print(f"  {digits[0]} + {' + '.join(digits[1:])} = {result}")

def interactive_demo():
    """Interactive demonstration"""
    print("\n" + "=" * 60)
    print("INTERACTIVE DEMO:")
    print("=" * 60)
    
    numbers = [123, 9876, 100]
    for num in numbers:
        digits = list(str(num))
        result = sum_of_digits_iterative(num)
        print(f"\n{num}: {' + '.join(digits)} = {result}")

if __name__ == "__main__":
    main()
    test_cases()
    interactive_demo()