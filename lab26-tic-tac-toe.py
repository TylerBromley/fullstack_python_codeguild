# lab26-tic-tac-toe.py

class Player:
    """ Create players with their names and tokens: "X" or "O" """
    def __init__(self, name, token):
        self.name = name
        self.token = token


class Game:
    """ A game of tic-tac-toe """
    # set up the board as a list of rows
    def __init__(self):
        self.board = [[1,2,3],[4,5,6],[7,8,9]]
        self.count = 0
    # print the board to resemble tic-tac-toe
    def __repr__(self):
        return f"{self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]}\n{self.board[1][0]}|{self.board[1][1]}|{self.board[1][2]}\n{self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]}"
    # replace the user-selected number with user token "X" or "O"
    def move(self, n, player):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == n:
                    self.board[i][j] = player.token
                    self.count += 1
    # determine winning combinations, return player token
    def calc_winner(self):
        # rows
        for i in range(len(self.board)):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
        # columns
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[0][j] == self.board[1][j] == self.board[2][j]:
                    return self.board[i][0]
        # diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        elif self.board[2][0] == self.board[1][1] == self.board[0][2]:
            return self.board[2][0]
    # determine if board is full
    def is_full(self):
        if self.count == 9:
            return True
    # if board is full or a winner has been established, end game
    def is_game_over(self):
        if self.is_full():
            print("It's a draw!\n")
            return True
        elif self.calc_winner() == "X":
            print("Player 1 wins!\n")
            return True
        elif self.calc_winner() == "O":
            print("Player 2 wins!\n")
            return True


def main():
    # get the players' names and ask if they'd like to quit
    while True:
        message = input("TYLER'S TIC TAC TOE\nType [P] to play or [Q] to quit: ").strip().lower()
        if message.startswith("q"):
            break
        player1_name = input("Player 1: What is your name? ").strip()
        player1 = Player(player1_name, "X")
        player2_name = input("Player 2: What is your name? ").strip()
        player2 = Player(player2_name, "O")
        # create a new game and display to users
        new_game = Game()
        print(new_game)
        # keep asking for moves as long as the game is not over
        while not new_game.is_game_over():
            player1_num = int(input(f"{player1.name}: What is your move? "))
            new_game.move(player1_num, player1)
            print(new_game)
            if new_game.is_game_over():
                break
            player2_num = int(input(f"{player2.name}: What is your move? "))
            new_game.move(player2_num, player2)
            print(new_game)
            if new_game.is_game_over():
                break

main()



