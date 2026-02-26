def generate_sequence(n: int):
    """Yield the first n terms of the pattern."""
    for i in range(1, n + 1):
        term = ((-1) ** (i + 1)) * (2 * i - 1)
        yield term

def main():
    
    #  Read the user’s input

    while True:
        try:
            user_input = input("Enter the number of terms (N): ").strip()
            N = int(user_input)
            if N < 0:
                print("Please enter a non‑negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.") # If the user put a negative integer the program will not continue to next step


    #  Generate the terms

    terms = list(generate_sequence(N))


    #  Compute the sum (two ways – loop & formula)

    # a) By direct addition
    sum_by_loop = sum(terms)

    # b) Using the closed‑form (optional, just for verification)
    sum_by_formula = N if N % 2 == 1 else -N

    #  Output
    
    print("\n--- Results ---")
    print(f"First {N} term(s): {', '.join(str(t) for t in terms)}")
    print(f"Sum (computed by loop) : {sum_by_loop}")
    print(f"Sum (using formula)    : {sum_by_formula}")

if __name__ == "__main__":
    main()