import random
import sys

#list of moves available
moves = ['rock', 'paper', 'scissors']

def main():
    player1_score = 0
    player2_score = 0
    player1_score, player2_score = game(player1_score, player2_score)


#a function that determines how what each move does
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or (one == 'paper' and two == 'rock') or (one == 'scissors' and two == 'paper'))


#a function that prompts a user for an input as a choice
def player():
    while True:
        prompt = input("Select Rock, Paper or Scissors. Type Quit to exit game: ").lower()

        if prompt not in moves and prompt != 'quit':
            print("Invalid Input! Please try again.")
        elif prompt == 'quit':
            sys.exit("Game Over")
        else:
            break
    return prompt


# a function that chooses a random option  in the list of available choices
def random_player():
    return random.choice(moves) 


#a function that simulates a single round of play
def round():
    player1 = player()
    player2 = random_player()
    print (f"Player 1 chose {player1.title()} and player 2 chose {player2.title()}")
    if beats(player1, player2):
        #player 1 gains one point while player 2 gains none
        return 1, 0 
    elif beats(player2, player1):
        #player 2 gains one point while player 1 gains none
        return 0, 1
    else:
        #both players get no points
        return 0, 0


#a function that keeps track of the scores and plays the round multiple times
def game(player1_score, player2_score):
    rounds = 1
    print("Let the games begin!")
    while rounds <= 10:
        print(f"Round {rounds}")
        #unpacks the tuple returned from the round function and uses it to add to the score 
        p1_score, p2_score = round()
        player1_score += p1_score
        player2_score += p2_score
        rounds += 1
    print("Game Over!")

    if (player1_score > player2_score):
        print(f"Player 1 WON with {player1_score} points againts Player 2's {player2_score}")
    elif (player2_score > player1_score):
        print(f"Player 2 WON with {player2_score} points againts Player 1's {player1_score} points")
    else: 
        print("It ends in a DRAW")

    #returns the scores for each player
    return player1_score, player2_score


if __name__ == "__main__":
    main()