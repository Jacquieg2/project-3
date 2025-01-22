# Author: Jacqueline Garcia
# GitHub username: Jgarcia2
# Date: 01/21/2025
# Description: Write a program that asks the user to enter a positive integer. 

print("Please enter a positive integer:", end=" ")
number = int(input())

if number <= 0:
    print("The number must be a positive integer.")
else:
    print(f"The factors of {number} are:")

    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
