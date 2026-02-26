import math

def find_line_equation(x1, y1, x2, y2):
    """Find equation of line passing through two points"""
    if x2 - x1 == 0:  # Vertical line
        return None, None, x1  # x = constant
    else:
        m = (y2 - y1) / (x2 - x1)
        c = y1 - m * x1
        return m, c, None  # y = mx + c

def check_lines_relation(m1, c1, m2, c2, x1, y1, x2, y2, x3, y3, x4, y4):
    """Check relationship between two lines"""
    
    # Case 1: Lines intersect
    if m1 != m2:
        # Find intersection point
        x_intersect = (c2 - c1) / (m1 - m2)
        y_intersect = m1 * x_intersect + c1
        
        # Calculate acute angle between lines
        if m1 is None or m2 is None:  # One line is vertical
            if m1 is None:
                angle = 90 - math.degrees(math.atan(m2))
            else:
                angle = 90 - math.degrees(math.atan(m1))
        else:
            denominator = 1 + m1 * m2
            if denominator == 0:  # Lines are perpendicular
                angle = 90
            else:
                tan_angle = abs((m2 - m1) / denominator)
                angle = math.degrees(math.atan(tan_angle))
        
        return "intersect", (x_intersect, y_intersect), angle
    
    # Case 2: Lines are parallel or coincident
    else:
        # Check if lines are coincident (same line)
        if c1 == c2:
            return "coincident", None, None
        else:
            # Calculate distance between parallel lines
            # Distance = |c2 - c1| / sqrt(1 + m1²)
            if m1 is None:  # Both vertical lines
                distance = abs(x1 - x3)
            else:
                distance = abs(c2 - c1) / math.sqrt(1 + m1**2)
            return "parallel", None, distance

def main():
    print("=" * 60)
    print("LINE INTERSECTION CALCULATOR")
    print("=" * 60)
    
    # Input four points
    print("\nEnter coordinates for four points:")
    x1, y1 = map(float, input("P1 (x1, y1): ").split())
    x2, y2 = map(float, input("P2 (x2, y2): ").split())
    x3, y3 = map(float, input("P3 (x3, y3): ").split())
    x4, y4 = map(float, input("P4 (x4, y4): ").split())
    
    # Find equations
    m1, c1, v1 = find_line_equation(x1, y1, x2, y2)
    m2, c2, v2 = find_line_equation(x3, y3, x4, y4)
    
    print("\n" + "=" * 60)
    print("LINE EQUATIONS:")
    print("=" * 60)
    
    # Display line 1 equation
    if m1 is None:
        print(f"Line through P1 and P2: x = {v1}")
    else:
        print(f"Line through P1 and P2: y = {m1:.2f}x + {c1:.2f}")
    
    # Display line 2 equation
    if m2 is None:
        print(f"Line through P3 and P4: x = {v2}")
    else:
        print(f"Line through P3 and P4: y = {m2:.2f}x + {c2:.2f}")
    
    # Check relationship and display results
    relation, value1, value2 = check_lines_relation(
        m1, c1, m2, c2, x1, y1, x2, y2, x3, y3, x4, y4
    )
    
    print("\n" + "=" * 60)
    print("RESULTS:")
    print("=" * 60)
    
    if relation == "intersect":
        print(f"✓ Lines intersect at point: ({value1[0]:.2f}, {value1[1]:.2f})")
        print(f"✓ Acute angle between lines: {value2:.2f}°")
    
    elif relation == "parallel":
        print(f"✓ Lines are parallel")
        print(f"✓ Distance between parallel lines: {value2:.2f} units")
    
    elif relation == "coincident":
        print("✓ Coinciding Lines")

if __name__ == "__main__":
    main()