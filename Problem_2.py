def calculate_determinant(matrix):
    """Calculate determinant of 3x3 matrix using formula"""
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]
    d = matrix[1][0]
    e = matrix[1][1]
    f = matrix[1][2]
    g = matrix[2][0]
    h = matrix[2][1]
    i = matrix[2][2]
    
    # Determinant = a(ei - fh) - b(di - fg) + c(dh - eg)
    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    
    return det

def display_matrix(matrix):
    """Display matrix in proper format"""
    print("\nGiven Matrix:")
    for row in matrix:
        print("|", end=" ")
        for element in row:
            print(f"{element:8.2f}", end=" ")
        print("|")

def main():
    print("=" * 60)
    print("3x3 MATRIX DETERMINANT CALCULATOR")
    print("=" * 60)
    
    # Initialize 3x3 matrix
    matrix = []
    
    # Input matrix elements
    print("\nEnter elements of 3x3 matrix row by row:")
    for i in range(3):
        while True:
            try:
                row = list(map(float, input(f"Row {i+1} (3 elements): ").split()))
                if len(row) != 3:
                    print("Please enter exactly 3 elements!")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Invalid input! Please enter numeric values.")
    
    # Display the input matrix
    display_matrix(matrix)
    
    # Calculate and display determinant
    print("\n" + "=" * 60)
    print("CALCULATION:")
    print("=" * 60)
    
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    
    # Show step-by-step calculation
    print(f"\nMatrix elements:")
    print(f"a = {a}, b = {b}, c = {c}")
    print(f"d = {d}, e = {e}, f = {f}")
    print(f"g = {g}, h = {h}, i = {i}")
    
    print(f"\nUsing formula: det = a(ei - fh) - b(di - fg) + c(dh - eg)")
    
    term1 = a * (e * i - f * h)
    term2 = b * (d * i - f * g)
    term3 = c * (d * h - e * g)
    
    print(f"\nStep 1: a(ei - fh) = {a}({e}×{i} - {f}×{h}) = {a}({e*i} - {f*h}) = {a}({e*i - f*h}) = {term1}")
    print(f"Step 2: b(di - fg) = {b}({d}×{i} - {f}×{g}) = {b}({d*i} - {f*g}) = {b}({d*i - f*g}) = {term2}")
    print(f"Step 3: c(dh - eg) = {c}({d}×{h} - {e}×{g}) = {c}({d*h} - {e*g}) = {c}({d*h - e*g}) = {term3}")
    
    print(f"\nDeterminant = {term1} - {term2} + {term3}")
    
    # Calculate final determinant
    determinant = calculate_determinant(matrix)
    
    print("\n" + "=" * 60)
    print("RESULT:")
    print("=" * 60)
    print(f"\n✓ Determinant of the matrix = {determinant:.2f}")
    
    # Additional info
    if determinant == 0:
        print("→ The matrix is SINGULAR (non-invertible)")
    else:
        print("→ The matrix is NON-SINGULAR (invertible)")

if __name__ == "__main__":
    main()