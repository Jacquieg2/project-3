# Author: Jacqueline Garcia
# GitHub username: Jgarcia2
# Date: 01/21/2025
# Description: Write a program that asks the user how many integers they would like to enter.

print("How many integers would you like to enter?")
num_integers = int(input())

print(f"Please enter {num_integers} integers.")

first_number = int(input())
min_value = first_number
max_value = first_number

# Process the remaining integers
for _ in range(num_integers - 1):
    current_number = int(input())
    if current_number < min_value:
        min_value = current_number
    if current_number > max_value:
        max_value = current_number

# Output the results
print(f"min: {min_value}")
print(f"max: {max_value}")
