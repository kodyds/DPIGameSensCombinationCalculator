# Define the ranges for a and b
a_values = range(200, 12001, 50)
b_values = range(1, 21)

# Target value
target = 5086

# Initialize variables to store the best combination and the smallest difference
best_a = None
best_b = None
smallest_difference = float('inf')

# Loop through all combinations of a and b
for a in a_values:
    for b in b_values:
        product = a * b
        difference = abs(target - product)
        
        # Update the best combination if the current one is closer to the target
        if difference < smallest_difference:
            best_a = a
            best_b = b
            smallest_difference = difference

# Output the best combination
print(f"The best combination is a = {best_a} and b = {best_b} with a product of {best_a * best_b} (closest to 5086)")
