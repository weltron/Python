# A Secret Auction Program
import os
from art import logo

#create a clear function that clers out the console each time a new bidder is entering a bid
clear = lambda: os.system('clear')
#print the ascii of the logo from the art.py file
print(logo)
auction = {}
highest = 0
winner = ""
#a loop to ask for bidders for their names and bids that are then stored in a dictionary
while True:
  name = input("What is your name? ")
  bid = int(input("How much do you bid? $"))
  auction[name] = bid
  ask = input("Are there any other bidder? ").lower()
  if ask == "yes":
    clear()
    continue
  else:
    break

for bidder in auction:
  if auction[bidder] > highest:
    highest = auction[bidder]
    winner = bidder
    
print(f"The winner is {winner} with a bid of ${highest}")
    