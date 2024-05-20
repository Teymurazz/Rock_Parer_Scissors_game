import random

class Player:
    def __init__(self):
        self.score = 0

    def update_score(self, result):
        if result == "win":
            self.score += 1

class Move:
    def __init__(self, name):
        self.name = name
        

class Rock(Move):
    def __init__(self):
        super().__init__("rock")

class Paper(Move):
    def __init__(self):
        super().__init__("paper")

class Scissors(Move):
    def __init__(self):
        super().__init__("scissors")

class RockPaperScissors:
    def __init__(self):
        self.moves = [Rock(), Paper(), Scissors()]
        self.results = {
            "rock": {"rock": "draw", "paper": "lose", "scissors": "win"},
            "paper": {"rock": "win", "paper": "draw", "scissors": "lose"},
            "scissors": {"rock": "lose", "paper": "win", "scissors": "draw"}
        }

    def get_computer_move(self):
        return random.choice(self.moves)

    def play_round(self, user_move):
        computer_move = self.get_computer_move()
        result = self.results[user_move.name][computer_move.name]
        return result, computer_move

class Field:
    def __init__(self):
        self.score = {"Player": 0, "Computer": 0}

    def update_score(self, player, result):
        if result == "win":
            self.score[player] += 1
        elif result == "lose":
            self.score["Computer"] += 1

    def display_score(self):
        print("Current score:")
        for player, score in self.score.items():
            print(f"{player}: {score}")

class Interface:
    def get_user_move(self):
        while True:
            user_input = input("Choose rock, paper, or scissors (or exit to quit): ").lower()
            if user_input in ["rock", "paper", "scissors", "exit"]:
                return user_input
            print("Invalid choice. Please choose rock, paper, or scissors.")

    def display_moves(self, player_move, computer_move):
        print(f"Player chose {player_move}, Computer chose {computer_move}")

    def display_result(self, result):
        print(f"Result: {result}\n")

class Game:
    def __init__(self):
        self.rps = RockPaperScissors()
        self.field = Field()
        self.interface = Interface()

    def play(self):
        print("Welcome to Rock, Paper, Scissors game. Enjoy it!")
        while True:
            user_input = self.interface.get_user_move()
            if user_input == "exit":
                break
            player_move = Move(user_input)
            result, computer_move = self.rps.play_round(player_move)
            self.interface.display_moves(player_move.name, computer_move.name)
            self.interface.display_result(result)
            self.field.update_score("Player", result)
            self.field.display_score()

if __name__ == "__main__":
    game = Game()
    game.play()
