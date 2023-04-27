# Определить индексы элементов (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

# Generate a list of 20 random numbers
numbers = [random.randint(1, 100) for _ in range(20)]

# Prompt the user to enter a range
minimum = int(input("Enter the minimum value: "))
maximum = int(input("Enter the maximum value: "))

# Get the indexes of the elements in the given range
indexes = [i for i, num in enumerate(numbers) if minimum <= num <= maximum]

# Print the generated list and the indexes of the elements in the given range
print("Generated numbers:", numbers)
print(f"Indexes of elements between {minimum} and {maximum}: {indexes}")
