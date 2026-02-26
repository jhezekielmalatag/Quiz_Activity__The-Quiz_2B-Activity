import math

def catalan_using_combination(n):
    """Calculate nth Catalan number using combination formula"""
    # C_n = (2n choose n) / (n+1)
    return math.comb(2 * n, n) // (n + 1)

def main():
    print("=" * 60)
    print("CATALAN SERIES (Using Combination Formula)")
    print("=" * 60)
    
    n = int(input("\nEnter number of terms: "))
    
    print(f"\nUsing formula: C_n = (2n choose n) / (n+1)")
    print(f"\nCatalan Series from C_0 to C_{n-1}:")
    
    for i in range(n):
        cat_num = catalan_using_combination(i)
        print(f"C_{i} = {cat_num}")

if __name__ == "__main__":
    main()