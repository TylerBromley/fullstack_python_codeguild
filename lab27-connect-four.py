# lab27-connect-four.py

class Player:
    """ A connect4 player """
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Game:
    """ A game of Connect4 """
    def __init__(self):
        self.board = [
                      [" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "]]

    # print the board representation
    def __repr__(self):
        nums = "  1   2   3   4   5   6   7  "
        base = "-----------------------------"
        line = ""
        for i in range(len(self.board)):
            line += f"| {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]} | {self.board[i][3]} | {self.board[i][4]} | {self.board[i][5]} | {self.board[i][6]} |\n"
        return f"\n{nums}\n{line}{base}"

    # return the remaining free space in a column
    def get_height(self, position):
        height = 0
        col = [r[position-1] for r in self.board]
        for i in col:
            if i != " ":
                height += 1
        return height

    # add player color to the next open row of the column
    def move(self, player, position):
        place = self.get_height(position)
        if place > 0:
            new_val = 5 - place
            print(new_val)
        else:
            new_val = len(self.board) - 1
        self.board[new_val][position-1] = player.color

    # check for four-in-a-row
    def calc_winner(self):
        # rows
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if j >= 0 and j <= 3:
                    if self.board[i][j] != " ":
                        if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3]:
                            return self.board[i][j]
        # columns
        for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if i <=5 and i >=3: 
                        if self.board[i][j] != " ":
                            if self.board[i-3][j] == self.board[i-2][j] == self.board[i-1][j] == self.board[i][j]:
                                return self.board[i][j]

        # diagonal
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if j >= 0 and j <= 3:
                    if self.board[i][j] != " ":
                        if self.board[i][j] == self.board[i-1][j+1] == self.board[i-2][j+2] == self.board[i-3][j+3]:
                            return self.board[i][j]
                elif (i <=5 and i >=3) and j >= 3:
                    if self.board[i][j] != " ":
                        if self.board[i][j] == self.board[i-1][j-1] == self.board[i-2][j-2] == self.board[i-3][j-3]:
                            return self.board[i][j]

    # determine if game board is full
    def is_full(self):
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != " ":
                    count += 1
        if count == 42:
            return True

    # return true if board is full or a player has won
    def is_game_over(self):
        if self.is_full() == True:
            print("It's a draw!")
            return True
        elif self.calc_winner() == "R":
            print("Player 1 wins!\n")
            return True
        elif self.calc_winner() == "Y":
            print("Player 2 wins!\n")
            return True


def main():
    while True:
        # Establish player 1 and player 2 or exit the game
        message = input("Welcome To Connect4!\nType [P] to play or [Q] to quit: ").strip().lower()
        if message.startswith("q"):
            break
        player1_name = input("Player 1: What is your name? ").strip()
        player1 = Player(player1_name, "R")
        player2_name = input("Player 2: What is your name? ").strip()
        player2 = Player(player2_name, "Y")
        # create a new game and display to users
        new_game = Game()
        print(new_game)
        # keep asking for moves as long as the game is not over
        while not new_game.is_game_over():
            player1_col = int(input(f"{player1.name}: What is your move? "))
            new_game.move(player1, player1_col)
            print(new_game)
            if new_game.is_game_over():
                break
            player2_col = int(input(f"{player2.name}: What is your move? "))
            new_game.move(player2, player2_col)
            print(new_game)
            if new_game.is_game_over():
                break

main()
