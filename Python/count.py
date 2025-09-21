# List of numbers
numbers = [1, 2, 1, 2, 3, 4]

# Dictionary to store frequency
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Print frequency
for num, count in frequency.items():
    print(f"{num} → {count} {'times' if count > 1 else 'time'}")
