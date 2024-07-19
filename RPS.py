#!/usr/bin/env python3

import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""



def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Player:
    def __init__(self):
        self.score = 0
        self.my_move=None
        self.their_move=None
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class AllRockPlayer:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass

class HumanPlayer(Player):
    def move(self):
        while True:
            options = str.lower(input("Rock, Paper, Scissors?: \n"))
            if options in moves:
                return options
            print(f"Move {options} unknown. Try again!")
    
    def learn(self, my_move, their_move):
        pass

class ReflectPlayer(Player):
    def __init__(self):
        self.last_move = None

    def learn(self, my_move, their_move):
        self.last_move = their_move
        return self.last_move

    def move(self):
        if self.last_move is None:
            return random.choice(moves)
        return self.last_move


class CyclePlayer(Player):
    def __init__(self):
        self.last_move = None


    def move(self):
        if self.last_move is None:
            self.last_move = "rock"
        elif self.last_move == "rock":
            self.last_move = "paper"

        elif self.last_move == "paper":
            self.last_move = "scissors"

        elif self.last_move == "scissors":
            self.last_move = "rock"

        return self.last_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if move1 not in moves:
            move1 = self.p1.move()
        print(f"Player 1 chooses \033[1m{move1}\033[0m.\n"
              f"Player 2 chooses \033[1m{move2}\033[0m.")
        if beats(move1, move2):
            print("***Player 1 wins!***")
            self.score1 += 1
        elif move1 == move2:
            print("***It's a tie!***")
        else:
            print("***Player 2 wins!***")
            self.score2 += 1

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!\n")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
            print(f"Player 1: \033[1m{self.score1}\033[0m Point(s)\n"
                  f"Opponent: \033[1m{self.score2}\033[0m Point(s)")
        if self.score1 > self.score2:
            print("***Congratulations, you win!***")
        elif self.score1 < self.score2:
            print("***Game Over! You loose!***")
        elif self.score1 == self.score2:
            print("***It's a tie!***")
        print(f"Final Results:\n"
              f"Player 1: \033[1m{self.score1}\033[0m Point(s)\n"
              f"Opponent: \033[1m{self.score2}\033[0m Point(s)")
        if self.score1 > self.score2:
            print("***Congratulations, you win!***")
        elif self.score1 < self.score2:
            print("***Game Over! You loose!***")
        elif self.score1 == self.score2:
            print("***It's a tie!***")
        play_again = str.lower(input("Do you want to play again? (y/n):\n"))
        if play_again == "y":
            game.play_game()


if __name__ == '__main__':

    opponents = [CyclePlayer(), RandomPlayer(), AllRockPlayer(), ReflectPlayer()]
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
