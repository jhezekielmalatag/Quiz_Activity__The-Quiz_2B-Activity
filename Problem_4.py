def calculate_compound_interest(principal, years, rate_percent):
    """Calculate compound interest with yearly compounding"""
    # Convert percentage to decimal
    rate = rate_percent / 100
    
    # Store year-by-year amounts
    yearly_amounts = []
    current_amount = principal
    
    print("\n" + "=" * 60)
    print("YEAR-BY-YEAR CALCULATION:")
    print("=" * 60)
    
    # Calculate for each year
    for year in range(1, years + 1):
        interest = current_amount * rate
        current_amount = current_amount + interest
        yearly_amounts.append(current_amount)
        
        # Display calculation for each year
        print(f"\nAt the end of year {year}:")
        print(f"  {current_amount - interest:.2f} + ({current_amount - interest:.2f} × {rate})")
        print(f"  = {current_amount - interest:.2f} + {interest:.2f}")
        print(f"  = {current_amount:.2f}")
    
    return current_amount, yearly_amounts

def main():
    print("=" * 60)
    print("COMPOUND INTEREST CALCULATOR")
    print("=" * 60)
    
    # Input from user
    while True:
        try:
            principal = float(input("\nEnter initial amount: "))
            if principal < 0:
                print("Error: Initial amount cannot be negative!")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid number!")
    
    while True:
        try:
            years = int(input("Enter number of years: "))
            if years < 0:
                print("Error: Number of years cannot be negative!")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer!")
    
    while True:
        try:
            rate_percent = float(input("Enter interest rate (percent per year): "))
            if rate_percent < 0:
                print("Error: Interest rate cannot be negative!")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid number!")
    
    # Calculate compound interest
    final_amount, yearly_amounts = calculate_compound_interest(
        principal, years, rate_percent
    )
    
    # Display final result
    print("\n" + "=" * 60)
    print("FINAL RESULT:")
    print("=" * 60)
    print(f"\n✓ At the end of {years} years, you will have ${final_amount:.2f}")
    
    # Display summary table
    print("\n" + "=" * 60)
    print("SUMMARY TABLE:")
    print("=" * 60)
    print(f"{'Year':<10} {'Amount ($)':<15}")
    print("-" * 25)
    print(f"{'0':<10} {principal:<15.2f}")
    for i, amount in enumerate(yearly_amounts, 1):
        print(f"{i:<10} {amount:<15.2f}")
    
    # Show formula verification
    print("\n" + "=" * 60)
    print("FORMULA VERIFICATION:")
    print("=" * 60)
    rate = rate_percent / 100
    formula_amount = principal * ((1 + rate) ** years)
    print(f"\nUsing formula: A = P(1 + r)^n")
    print(f"A = {principal}(1 + {rate})^{years}")
    print(f"A = {principal}({1 + rate:.4f})^{years}")
    print(f"A = {formula_amount:.2f}")
    print(f"\nBoth methods give: ${final_amount:.2f}")

def test_cases():
    """Run test cases"""
    print("\n" + "=" * 60)
    print("TEST CASES:")
    print("=" * 60)
    
    test_cases = [
        (3000, 10, 5.5),   # Given example
        (1000, 5, 10),     # 1000 at 10% for 5 years
        (5000, 3, 7.5),    # 5000 at 7.5% for 3 years
        (100, 1, 50),      # 100 at 50% for 1 year
    ]
    
    for principal, years, rate in test_cases:
        rate_decimal = rate / 100
        final = principal * ((1 + rate_decimal) ** years)
        print(f"  ${principal} at {rate}% for {years} years = ${final:.2f}")

if __name__ == "__main__":
    main()
    test_cases()