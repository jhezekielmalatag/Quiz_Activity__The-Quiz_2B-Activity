# Simple version using Python's built-in sorting

# Input 5 integers
numbers = []
for i in range(5):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

# Sort ascending
ascending = sorted(numbers)

# Sort descending
descending = sorted(numbers, reverse=True)

print("\nOriginal:", numbers)
print("Ascending:", ascending)
print("Descending:", descending)