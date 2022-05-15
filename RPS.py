"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            response = input("Please choose: Rock, Paper or Scissors? ")
            response = response.lower()

            if response not in moves and response != 'quit':
                print("Invalid input. Please try again.")
            elif response == 'quit':
                exit()
            else:
                break
        return response


class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = None

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):

    def __init__(self):
        self.my_move = None

    def learn(self, my_move, their_move):
        self.my_move = my_move

    def move(self):
        if self.my_move is None:
            move = moves[0]
        else:
            index = moves.index(self.my_move) + 1
            if index >= len(moves):
                index = 0
            move = moves[index]
        self.my_move = move
        return move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1win = 0
        self.p2win = 0
        self.tie_count = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.p1win += 1
            print("Player 1 wins \n")
        elif beats(move2, move1):
            self.p2win += 1
            print("Player 2 wins \n")
        else:
            self.tie_count += 1
            print("It's a TIE \n")

        print(f'Player 1 scored: {self.p1win},'
              f' Player 2 scored: {self.p2win},'
              f' Ties: {self.tie_count}\n')

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        round = 1
        while abs(self.p1win - self.p2win) <= 3:
            print(f"Round {round}:")
            self.play_round()
            round += 1
        print("Game over! \n")
        print(f'Total rounds: {round - 1},'
              f' Player 1 scored: {self.p1win},'
              f' Player 2 scored: {self.p2win},'
              f' Ties: {self.tie_count}\n')

        if self.p1win > self.p2win:
            print("Player 1 WON!")
        elif self.p2win > self.p1win:
            print("Player 2 WON!")
        else:
            print("It's a DRAW!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
