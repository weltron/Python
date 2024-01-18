#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
level = input("Choose a difficuly. Type 'easy' or 'hard': ").lower()
number = random.randrange(1, 101)
#attempts = 0
if level == "easy":
  attempts = 10
else:
  attempts = 5

while attempts != 0:
  print(f"You have {attempts} attempts remaining to guess the number")
  guess = int(input("Make a guess: "))
  if guess == number:
    print(f"You got it! The answer is {number}")
    break
  elif guess > number:
    print("Too high.")
    attempts -= 1
  else:
    print("Too low.")
    attempts -= 1

  if attempts == 0:
    print("You've run out of guesses, you lose")
  else:
    print("Guess again.")
    
    