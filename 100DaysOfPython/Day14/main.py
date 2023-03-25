from game_data import data
import random
from art import logo, vs
import os


def get_account():
  """This function selects a random account from the list"""
  return random.choice(data)

def data_display(account):
  """This function unpacks the data from the dictionary and makes it readable to the user"""
  name = account['name']
  who = account['description']
  origin = account['country']
  return f"{name}, a {who}, from {origin}"

def compare(guess, acc1, acc2):
  """This function compares which of the two has a higher number of followers"""
  if acc1 > acc2:
    return guess == 'a'
  else:
    return guess == 'b'

def play():
  """This is the game play where after a correct guess value 'B' becomes 'A' and the games continues as long as the guess is correct"""
  print(logo)
  acc1 = get_account()
  acc2 = get_account()
  game_over = False
  score = 0
  
  while acc1 == acc2:
    acc2 = get_account()
  while not game_over:
    print(f"Compare A: {data_display(acc1)}")
    print(vs)
    print(f"Against B: {data_display(acc2)}")
    guess = input("Who has more followers? ('A' or 'B'): ").lower()
    acc1 = acc2
    acc2 = get_account()
    os.system('clear')
    print(logo)
    if compare(guess, acc1['follower_count'], acc2['follower_count']) == True:
      score += 1
      print(f"Correct. Your score is now {score}")
    else:
      game_over = True
      print(f"You are Wrong. Your score is {score}")
  
play()  