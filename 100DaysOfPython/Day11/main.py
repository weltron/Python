############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo
import os

def deal_card():
  """Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(card_list):
  """Takes a list of cards and calculates the score"""
  score = sum(card_list)
  if len(card_list) == 2 and score == 21:
    score = 0
  # change 11 to 1 if score is over 21
  if 11 in card_list and score > 21:
    card_list.remove(11)
    card_list.append(1)
  return score

def compare(user_score, computer_score):
  """Takes and compares the scores of both players to determine the winner"""
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  if user_score == computer_score:
    return "It is DRAW 🙃"
  elif computer_score == 0:
    return "LOSE! Opponent WON with a Blackjack 😱"
  elif user_score == 0:
    return "WON with a Blackjack 😎"
  elif user_score > 21 :
    return "You went over. You LOSE 😭"
  elif computer_score > 21:
    return "Opponent went over. You WON 😁"
  elif user_score > computer_score:
    return "You WON 😃"
  else:
    return "You LOSE 😤"

  
def play():
  """Plays the game from start to finish"""
  print(logo)
  user_cards = []
  computer_cards = []
  game_over = False

  for _ in range(2):
    """Deal both playes with two cards at the beginning of the game"""
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not game_over:
    """While loop to run the game as long as user wants to play"""
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"    Your cards {user_cards}, current score: {user_score}")
    print(f"    Computer's first card {computer_cards[0]}")
    #check to see that the user score does not exceed 21 or equal 0
    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
      if input("Would you like to draw another card? (y or n): ").lower() == 'y':
        user_cards.append(deal_card())
      else:
        game_over = True

  while computer_score != 0 and computer_score < 17:
    """While loop to keep dealing cards for coputer if the score is less than 17 or not equal to 0"""
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"    Your final cards in hand: {user_cards}, final score: {user_score}")
  print(f"    Computer's final cards in hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? (y or n): ").lower() == "y":
  os.system('clear')
  play()
  
  