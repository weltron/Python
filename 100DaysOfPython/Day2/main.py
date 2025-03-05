#Tip Calculator
print("Welcome to the tip calculator.")
bill = int(input("What was the bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
pips = int(input("How many people to split the bill? "))

final = (bill/pips) * (1 + tip/100)
print(f"Each person should pay: ${final:.2f}")