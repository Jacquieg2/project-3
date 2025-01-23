# Author: Jacqueline Garcia
# GitHub username: Jgarcia2
# Date: 01/13/2025
# Description: Asks the user for five numbers and prints out the average.

print("Enter the integer for the player to guess.")
target_number = int(input())

guess_count = 0
guessed_correctly = False

print("Enter your guess.")
while not guessed_correctly:
    guess = int(input())
    guess_count += 1
    if guess > target_number:
        print("Too high - try again:")
    elif guess < target_number:
        print("Too low - try again:")
    else:
        guessed_correctly = True

if guess_count == 1:
    print("You guessed it in 1 try.")
else:
    print(f"You guessed it in {guess_count} tries.")
