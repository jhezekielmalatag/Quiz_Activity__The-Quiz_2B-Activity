def main():
    n = int(input("Enter number of terms: "))
    
    print(f"\nTriangle Series from T1 to T{n}:")
    
    for i in range(1, n + 1):
        tri_num = i * (i + 1) // 2
        print(f"T{i} = {tri_num}", end="  ")
        
        # New line every 5 terms
        if i % 5 == 0:
            print()

if __name__ == "__main__":
    main()