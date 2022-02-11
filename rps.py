#!/usr/bin/python
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.name = 'RockPlayer'

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def __init__(self):
        self.name = 'RandomPlayer'

    def move(self):
        return moves[random.randint(0, 2)]


class HumanPlayer(Player):
    def __init__(self):
        self.name = 'HumanPlayer'

    def move(self):
        move = ''
        while move not in moves:
            move = input("rock, paper, scissors? ").lower()
        return move


class ReflectPlayer(Player):
    def __init__(self):
        self.name = 'ReflectPlayer'
        self.opponentMoves = []

    def move(self):
        # FIRST ROUND HAS TO BE RANDOM
        if len(self.opponentMoves) == 0:
            return moves[random.randint(0, 2)]
        else:
            return self.opponentMoves[len(self.opponentMoves)-1]

    def learn(self, my_move, their_move):
        self.opponentMoves.append(their_move)


class CyclePlayer(Player):
    def __init__(self):
        self.name = 'CyclePlayer'
        self.myMoves = []

    def move(self):
        # FIRST ROUND HAS TO BE RANDOM
        if len(self.myMoves) == 0:
            return moves[random.randint(0, 2)]
        else:
            lastMove = self.myMoves[len(self.myMoves)-1]
            if lastMove == 'rock':
                return 'paper'
            elif lastMove == 'paper':
                return 'scissors'
            else:
                return 'rock'

    def learn(self, my_move, their_move):
        self.myMoves.append(my_move)


# Created to provide the human player a random computer player
computerPlayers = [Player(), RandomPlayer(), ReflectPlayer(), CyclePlayer()]


def beats(one, two):
    if (one == two):
        return "tie"
    elif ((one == 'rock' and two == 'scissors') or
          (one == 'scissors' and two == 'paper') or
          (one == 'paper' and two == 'rock')):
        return 1
    else:
        return 2


class Game:
    def __init__(self, p1, p2, rounds):
        self.p1 = p1
        self.p2 = p2
        # PLUS 1 SO WE CAN START AT ROUND 1 INSTEAD OF 0
        self.rounds = int(rounds) + 1
        self.p1Score = 0
        self.p2Score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        results = beats(move1, move2)
        if results == 1:
            self.p1Score += 1
            print("PLAYER 1 WINS!")
        elif results == 2:
            self.p2Score += 1
            print("PLAYER 2 WINS!")
        else:
            print("This round was a tie")

        print(f"\nPlayer 1 Current Score:{self.p1Score}")
        print(f"Player 2 Current Score:{self.p2Score}\n")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Let the RPS Games Begin!")
        for round in range(1, int(self.rounds)):
            print(f"Round {round}:")
            self.play_round()

        print("Game over!")
        print(f"\nPlayer 1 (TYPE:{self.p1.name}) Final Score:{self.p1Score}")
        print(f"Player 2 (TYPE:{self.p2.name}) Final Score:{self.p2Score}")


if __name__ == '__main__':
    print("\nWelcome to the RPS(Rock, Paper, Scissors) Tournament\n")
    option = 0
    rounds = ""
    while True:
        option = input("""Press 1 to play against the computer
Press 2 to watch 2 computer players\nOPTION: """)

        if option == '1':
            while(not rounds.isnumeric()):
                rounds = input("How many rounds would you like to play? ")
            game = Game(HumanPlayer(),
                        computerPlayers[random.randint(0, 3)],
                        rounds)
            game.play_game()
            break
        if option == '2':
            while(not rounds.isnumeric()):
                rounds = input("How many rounds would you like to watch? ")
            game = Game(computerPlayers[random.randint(0, 3)],
                        computerPlayers[random.randint(0, 3)],
                        rounds)
            game.play_game()
            break
