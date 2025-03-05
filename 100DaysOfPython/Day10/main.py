from art import logo
print(logo)
print("Welcome to the Calculator")

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def sub(n1, n2):
  return n1 - n2
  
#Multiply
def mult(n1, n2):
  return n1 * n2
  
#Division
def div(n1, n2):
  return n1 / n2

def calculator():
  print("Available operations for this calculator")
  operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
  }
  for symbol in operations:
    print(symbol)
  num1 = int(input("whats the first number?: "))
  while True:
    selected_symbol = input("Select operation: ")
    num2 = int(input("whats the next number?: "))
    func = operations[selected_symbol]
    answer = func(num1, num2)
    
    print(f"{num1} {selected_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue with {answer} or 'n' to start a new calculation: ") == "y":
      num1 = answer
    else:
      calculator()

calculator()