from random import randint
from tabulate import tabulate


class BattleshipGame:
    def __init__(self, board_size):
        self.board_size = board_size
        self.player_board = [['O' for _ in range(board_size)] for _ in range(board_size)]
        self.computer_board = [['O' for _ in range(board_size)] for _ in range(board_size)]
        self.player_ships = []
        self.computer_ships = []

    def print_board(self, board):
        headers = [''] + [chr(65 + i) for i in range(self.board_size)]
        table = [[i + 1] + row for i, row in enumerate(board)]
        print(tabulate(table, headers=headers, tablefmt="grid"))
        print()

    def place_ship(self, board, ship_size):
        while True:
            orientation = randint(0, 1)  # 0 for horizontal, 1 for vertical
            if orientation == 0:
                x = randint(0, self.board_size - ship_size)
                y = randint(0, self.board_size - 1)
                for i in range(ship_size):
                    if board[y][x + i] != 'O':
                        break
                else:
                    for i in range(ship_size):
                        board[y][x + i] = 'S'
                    return (x, y, x + ship_size - 1, y)
            else:
                x = randint(0, self.board_size - 1)
                y = randint(0, self.board_size - ship_size)
                for i in range(ship_size):
                    if board[y + i][x] != 'O':
                        break
                else:
                    for i in range(ship_size):
                        board[y + i][x] = 'S'
                    return (x, y, x, y + ship_size - 1)

    def get_guess(self):
        while True:
            guess = input("Enter your guess (e.g., A1): ").upper()
            if len(guess) != 2 or not guess[0].isalpha() or not guess[1].isdigit():
                print("Invalid guess! Please enter a valid guess.")
                continue
            x = ord(guess[0]) - 65
            y = int(guess[1]) - 1
            if x < 0 or x >= self.board_size or y < 0 or y >= self.board_size:
                print("Invalid guess! Please enter a valid guess.")
                continue
            return x, y

    def hit_ship(self, board, guess, ships):
        x, y = guess
        if board[y][x] == 'S':
            board[y][x] = 'X'
            ships[:] = [(x1, y1, x2, y2) for x1, y1, x2, y2 in ships if (x1, y1) != (x, y)]
            return True
        else:
            board[y][x] = '-'
            return False

    def play(self):
        print("Let's play Battleship!")
        print("You need to sink all the computer's ships.")
        print("The computer will take random shots on your board.")
        print("Good luck!")
        print()

        # Place player's ships
        for ship_size in [5, 4, 4, 3, 3, 3, 2, 2, 2, 2]:
            ship = self.place_ship(self.player_board, ship_size)
            self.player_ships.append(ship)

        # Place computer's ships
        for ship_size in [5, 4, 4, 3, 3, 3, 2, 2, 2, 2]:
            ship = self.place_ship(self.computer_board, ship_size)
            self.computer_ships.append(ship)

        while self.computer_ships:
            print("Your board:")
            self.print_board(self.player_board)

            print("Your turn:")
            guess = self.get_guess()
            if self.hit_ship(self.computer_board, guess, self.computer_ships):
                print("Congratulations! You hit a ship!")
                if not self.computer_ships:
                    print("Congratulations! You sank all the computer's ships!")
                    break
            else:
                print("Oops! You missed the ships.")

            print("Computer's turn:")
            guess = (randint(0, self.board_size - 1), randint(0, self.board_size - 1))
            if self.hit_ship(self.player_board, guess, self.player_ships):
                print("Oh no! The computer hit one of your ships!")
                if not self.player_ships:
                    print("Oh no! The computer sank all your ships!")
                    break
            else:
                print("Phew! The computer missed your ships.")
            print()

        print("Game over!")

# Main code
board_size = 10

game = BattleshipGame(board_size)
game.play()

