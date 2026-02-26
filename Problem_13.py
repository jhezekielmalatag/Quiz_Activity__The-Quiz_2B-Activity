import math

def calculate_area(x1, y1, x2, y2, x3, y3):
    """Calculate area using shoelace formula"""
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2

def check_collinear(x1, y1, x2, y2, x3, y3):
    """Check if three points are collinear"""
    area = calculate_area(x1, y1, x2, y2, x3, y3)
    return area == 0

def find_line_equation(x1, y1, x2, y2):
    """Find equation of line through two points"""
    if x2 - x1 == 0:  # Vertical line
        return "vertical", x1
    else:
        m = (y2 - y1) / (x2 - x1)
        c = y1 - m * x1
        return "normal", m, c

def find_midpoint(x1, y1, x2, y2):
    """Find midpoint of two points"""
    return (x1 + x2) / 2, (y1 + y2) / 2

def find_perpendicular_line(x0, y0, m):
    """Find equation of perpendicular line through a point"""
    if m == 0:  # Horizontal line -> perpendicular is vertical
        return "vertical", x0
    elif m == float('inf'):  # Vertical line -> perpendicular is horizontal
        return "horizontal", y0
    else:
        perp_m = -1 / m  # Negative reciprocal
        perp_c = y0 - perp_m * x0
        return "normal", perp_m, perp_c

def calculate_distance(x1, y1, x2, y2):
    """Calculate distance between two points"""
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    """Calculate area of triangle using formula"""
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2

def find_parallelogram_points(x1, y1, x2, y2, x3, y3):
    """Find fourth vertex to form parallelogram"""
    # Three possible fourth points:
    # P4 = P1 + P2 - P3 (using P1, P2 as adjacent)
    # P4 = P1 + P3 - P2 (using P1, P3 as adjacent)
    # P4 = P2 + P3 - P1 (using P2, P3 as adjacent)
    p4a_x, p4a_y = x1 + x2 - x3, y1 + y2 - y3
    p4b_x, p4b_y = x1 + x3 - x2, y1 + y3 - y2
    p4c_x, p4c_y = x2 + x3 - x1, y2 + y3 - y1
    return (p4a_x, p4a_y), (p4b_x, p4b_y), (p4c_x, p4c_y)

def display_point(name, x, y):
    """Display a point in formatted way"""
    print(f"  {name}: ({x}, {y})")

def main():
    print("=" * 70)
    print("COLLINEARITY AND GEOMETRY CALCULATOR")
    print("=" * 70)
    
    # Input three points
    print("\nEnter three points:")
    print("-" * 40)
    
    x1, y1 = map(float, input("Point P1 (x1 y1): ").split())
    x2, y2 = map(float, input("Point P2 (x2 y2): ").split())
    x3, y3 = map(float, input("Point P3 (x3 y3): ").split())
    
    print("\n" + "=" * 70)
    print("INPUT POINTS:")
    print("=" * 70)
    display_point("P1", x1, y1)
    display_point("P2", x2, y2)
    display_point("P3", x3, y3)
    
    # Check collinearity
    area = calculate_area(x1, y1, x2, y2, x3, y3)
    
    print("\n" + "=" * 70)
    print("COLLINEARITY CHECK:")
    print("=" * 70)
    print(f"\nUsing area formula: |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)| / 2")
    print(f"Calculation: |{x1}({y2}-{y3}) + {x2}({y3}-{y1}) + {x3}({y1}-{y2})| / 2")
    print(f"Area = {area}")
    
    if area == 0:
        print("\n✓ Points ARE collinear (area = 0)")
        
        # Part a: Collinear case
        print("\n" + "=" * 70)
        print("a. LINE EQUATION:")
        print("=" * 70)
        
        line_type, *line_params = find_line_equation(x1, y1, x2, y2)
        if line_type == "vertical":
            print(f"\n  Equation: x = {line_params[0]}")
        else:
            m, c = line_params
            print(f"\n  Slope (m) = {m}")
            print(f"  Equation: y = {m}x + {c}")
        
        print("\n" + "=" * 70)
        print("b. MIDPOINTS:")
        print("=" * 70)
        
        mx1, my1 = find_midpoint(x1, y1, x2, y2)
        mx2, my2 = find_midpoint(x2, y2, x3, y3)
        mx3, my3 = find_midpoint(x1, y1, x3, y3)
        
        print(f"\n  Midpoint of P1P2: ({mx1}, {my1})")
        print(f"  Midpoint of P2P3: ({mx2}, {my2})")
        print(f"  Midpoint of P1P3: ({mx3}, {my3})")
        
        print("\n" + "=" * 70)
        print("c. PERPENDICULAR LINES:")
        print("=" * 70)
        
        # Find slope of the line
        if x2 != x1:
            m = (y2 - y1) / (x2 - x1)
        else:
            m = float('inf')  # Vertical line
        
        print(f"\n  Original line slope: {m if m != float('inf') else 'undefined (vertical)'}")
        
        # Perpendicular at P1
        print(f"\n  Perpendicular at P1({x1}, {y1}):")
        ptype1, *pparams1 = find_perpendicular_line(x1, y1, m)
        if ptype1 == "vertical":
            print(f"    x = {pparams1[0]}")
        elif ptype1 == "horizontal":
            print(f"    y = {pparams1[0]}")
        else:
            pm, pc = pparams1
            print(f"    y = {pm}x + {pc}")
        
        # Perpendicular at P2
        print(f"\n  Perpendicular at P2({x2}, {y2}):")
        ptype2, *pparams2 = find_perpendicular_line(x2, y2, m)
        if ptype2 == "vertical":
            print(f"    x = {pparams2[0]}")
        elif ptype2 == "horizontal":
            print(f"    y = {pparams2[0]}")
        else:
            pm, pc = pparams2
            print(f"    y = {pm}x + {pc}")
        
        # Perpendicular at P3
        print(f"\n  Perpendicular at P3({x3}, {y3}):")
        ptype3, *pparams3 = find_perpendicular_line(x3, y3, m)
        if ptype3 == "vertical":
            print(f"    x = {pparams3[0]}")
        elif ptype3 == "horizontal":
            print(f"    y = {pparams3[0]}")
        else:
            pm, pc = pparams3
            print(f"    y = {pm}x + {pc}")
    
    else:
        print("\n✗ Points are NOT collinear (area > 0)")
        
        # Part b: Non-collinear case
        print("\n" + "=" * 70)
        print("a. DISTANCES BETWEEN POINTS:")
        print("=" * 70)
        
        d12 = calculate_distance(x1, y1, x2, y2)
        d23 = calculate_distance(x2, y2, x3, y3)
        d13 = calculate_distance(x1, y1, x3, y3)
        
        print(f"\n  Distance P1P2: {d12:.4f} units")
        print(f"  Distance P2P3: {d23:.4f} units")
        print(f"  Distance P1P3: {d13:.4f} units")
        
        print("\n" + "=" * 70)
        print("b. TRIANGLE AREA:")
        print("=" * 70)
        
        triangle_area = calculate_triangle_area(x1, y1, x2, y2, x3, y3)
        print(f"\n  Using formula: |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)| / 2")
        print(f"  Area = {triangle_area:.4f} square units")
        
        # Perimeter
        perimeter = d12 + d23 + d13
        print(f"  Perimeter = {perimeter:.4f} units")
        
        print("\n" + "=" * 70)
        print("c. PARALLELOGRAM POINTS:")
        print("=" * 70)
        
        (p4a_x, p4a_y), (p4b_x, p4b_y), (p4c_x, p4c_y) = find_parallelogram_points(x1, y1, x2, y2, x3, y3)
        
        print(f"\n  To form a parallelogram, add point:")
        print(f"    Option 1: P4({p4a_x}, {p4a_y}) using P1, P2 as adjacent vertices")
        print(f"    Option 2: P4({p4b_x}, {p4b_y}) using P1, P3 as adjacent vertices")
        print(f"    Option 3: P4({p4c_x}, {p4c_y}) using P2, P3 as adjacent vertices")

if __name__ == "__main__":
    main()