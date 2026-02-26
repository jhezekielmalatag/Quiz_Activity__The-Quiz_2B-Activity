import math

def solve_quadratic(a, b, c):
    """Solve Ax² + Bx + C = 0 and return roots"""
    if a == 0:
        return []
    
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return []  # No real roots
    elif discriminant == 0:
        return [-b / (2*a)]  # One real root
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return sorted([root1, root2])

def calculate_vertex(a, b, c):
    """Calculate vertex of parabola"""
    h = -b / (2*a)
    k = c - (b**2) / (4*a)
    return h, k

def calculate_focus(a, b, c):
    """Calculate focus of parabola"""
    h, k = calculate_vertex(a, b, c)
    # Focus is at (h, k + 1/(4a))
    focus_y = k + 1/(4*a)
    return h, focus_y

def calculate_directrix(a, b, c):
    """Calculate directrix of parabola"""
    h, k = calculate_vertex(a, b, c)
    # Directrix: y = k - 1/(4a)
    directrix_y = k - 1/(4*a)
    return directrix_y

def calculate_latus_rectum(a):
    """Calculate length of latus rectum"""
    return abs(1/a)

def calculate_slope(a, b, x):
    """Calculate slope at given x"""
    return 2*a*x + b

def main():
    print("=" * 70)
    print("PARABOLA ANALYZER")
    print("=" * 70)
    print("\nThis program analyzes a parabola in the form: y = Ax² + Bx + C")
    
    # Input coefficients
    while True:
        try:
            a = float(input("\nEnter coefficient A (for x²): "))
            if a == 0:
                print("Error: A cannot be zero for a parabola!")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid number!")
    
    b = float(input("Enter coefficient B (for x): "))
    c = float(input("Enter constant C: "))
    
    print("\n" + "=" * 70)
    print("PARABOLA EQUATION:")
    print("=" * 70)
    print(f"\n  y = {a}x² + {b}x + {c}")
    
    # Vertex
    print("\n" + "=" * 70)
    print("3. VERTEX:")
    print("=" * 70)
    h, k = calculate_vertex(a, b, c)
    print(f"\n  Formula: h = -B/(2A), k = C - B²/(4A)")
    print(f"  h = -{b}/(2×{a}) = {h:.4f}")
    print(f"  k = {c} - ({b})²/(4×{a}) = {k:.4f}")
    print(f"\n  ✓ Vertex: ({h:.4f}, {k:.4f})")
    
    direction = "upward" if a > 0 else "downward"
    print(f"  Parabola opens: {direction}")
    
    # Focus
    print("\n" + "=" * 70)
    print("1. FOCUS:")
    print("=" * 70)
    focus_x, focus_y = calculate_focus(a, b, c)
    print(f"\n  Formula: (h, k + 1/(4A))")
    print(f"  1/(4A) = 1/(4×{a}) = {1/(4*a):.4f}")
    print(f"\n  ✓ Focus: ({focus_x:.4f}, {focus_y:.4f})")
    
    # Directrix
    directrix_y = calculate_directrix(a, b, c)
    print(f"\n  Directrix: y = {directrix_y:.4f}")
    
    # Latus Rectum
    print("\n" + "=" * 70)
    print("2. LATUS RECTUM:")
    print("=" * 70)
    latus_length = calculate_latus_rectum(a)
    print(f"\n  Formula: |1/A|")
    print(f"  Length = |1/{a}| = {latus_length:.4f}")
    print(f"\n  ✓ Latus rectum length: {latus_length:.4f} units")
    
    # Endpoints of latus rectum
    print(f"\n  Endpoints: ({focus_x - latus_length/2:.4f}, {focus_y:.4f})")
    print(f"              ({focus_x + latus_length/2:.4f}, {focus_y:.4f})")
    
    # Intercepts
    print("\n" + "=" * 70)
    print("4. INTERCEPTS:")
    print("=" * 70)
    
    # Y-intercept
    print(f"\n  Y-Intercept:")
    print(f"    At x = 0, y = {c}")
    print(f"    ✓ Y-intercept: (0.0000, {c:.4f})")
    
    # X-intercepts
    print(f"\n  X-Intercepts:")
    roots = solve_quadratic(a, b, c)
    if roots:
        print(f"    Solving: {a}x² + {b}x + {c} = 0")
        discriminant = b**2 - 4*a*c
        print(f"    Discriminant: {discriminant:.4f}")
        
        for i, root in enumerate(roots, 1):
            print(f"    ✓ X-intercept {i}: ({root:.4f}, 0.0000)")
    else:
        print(f"    ✗ No real x-intercepts (discriminant < 0)")
    
    # Slope at a point
    print("\n" + "=" * 70)
    print("5. SLOPE AT A GIVEN POINT:")
    print("=" * 70)
    
    while True:
        try:
            x_point = float(input("\n  Enter x-coordinate to find slope: "))
            break
        except ValueError:
            print("  Error: Please enter a valid number!")
    
    slope = calculate_slope(a, b, x_point)
    y_point = a*x_point**2 + b*x_point + c
    
    print(f"\n  Formula: dy/dx = 2Ax + B")
    print(f"  Slope = 2({a})({x_point}) + ({b})")
    print(f"  Slope = {2*a*x_point:.4f} + {b:.4f}")
    print(f"\n  ✓ At x = {x_point}:")
    print(f"     y = {a}({x_point})² + {b}({x_point}) + {c} = {y_point:.4f}")
    print(f"     Slope = {slope:.4f}")
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY:")
    print("=" * 70)
    print(f"""
  Equation:       y = {a}x² + {b}x + {c}
  Vertex:         ({h:.4f}, {k:.4f})
  Focus:          ({focus_x:.4f}, {focus_y:.4f})
  Directrix:      y = {directrix_y:.4f}
  Latus Rectum:   {latus_length:.4f} units
  Y-intercept:    (0.0000, {c:.4f})
  X-intercepts:   {len(roots)} real root(s)
  Direction:      Opens {"upward" if a > 0 else "downward"}
    """)

def test_cases():
    """Run test cases"""
    print("\n" + "=" * 70)
    print("TEST CASES:")
    print("=" * 70)
    
    test_cases = [
        (1, -2, -3),   # y = x² - 2x - 3
        (1, 4, 4),     # y = x² + 4x + 4
        (1, 0, -4),    # y = x² - 4
    ]
    
    for a, b, c in test_cases:
        print(f"\n  y = {a}x² + {b}x + {c}")
        h, k = calculate_vertex(a, b, c)
        focus = calculate_focus(a, b, c)
        latus = calculate_latus_rectum(a)
        roots = solve_quadratic(a, b, c)
        print(f"    Vertex: ({h:.2f}, {k:.2f})")
        print(f"    Focus: {focus}")
        print(f"    Latus Rectum: {latus:.2f}")
        print(f"    X-intercepts: {roots}")

if __name__ == "__main__":
    main()
    test_cases()