# Read this the code in main.py
# Spot the problems 🐞.
# Modify the code to fix the program.
# No shortcuts - don't copy-paste to replace the code entirely with a working solution.
# The code needs to print the solution to the FizzBuzz game.

# Your program should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".

#   And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: #the first bug was 'or' was used instead on 'and'
    print("FizzBuzz")
  elif number % 3 == 0: #the bug here was that this was a n 'if' statement instead of 'elif'
    print("Fizz")
  elif number % 5 == 0: #the bug here was that this was a n 'if' statement instead of 'elif'
    print("Buzz")
  else:
    print(number) #the bug here was that the numbers were in brackets[] hence output was e.g. [1] instead of 1