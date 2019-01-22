# lab27-connect-four_v1.py
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

    # print the game board representation
    def __repr__(self):
        nums = "  1   2   3   4   5   6   7  "
        base = "-----------------------------"
        line = ""
        for i in range(len(self.board)):
            line += f"| {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]} | {self.board[i][3]} | {self.board[i][4]} | {self.board[i][5]} | {self.board[i][6]} |\n"
        return f"\n{nums}\n{line}{base}"

    def get_height(self, position):
        height = 0
        col = [r[position-1] for r in self.board]
        for i in col:
            if i != " ":
                height += 1
        return height

    # send the player's token to the bottom of the column
    def move(self, player, position):
        place = self.get_height(position)
        if place > 0:
            new_val = 5 - place
        else:
            new_val = len(self.board) - 1
        self.board[new_val][position-1] = player.color

    # determine if a player has four in a row (horiz, vert or diag)
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

    # check if game board is full
    def is_full(self):
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != " ":
                    count += 1
        if count == 42:
            return True
    # end game if the game board is full or if someone has won
    def is_game_over(self):
        if self.is_full() == True:
            print("It's a draw!")
            return True
        elif self.calc_winner() == "Y":
            print("Player 1 wins!\n")
            return True
        elif self.calc_winner() == "R":
            print("Player 2 wins!\n")
            return True


def main():
    # open the file with the corresponding moves
    with open('connect-four-moves.txt', 'r') as f:
        lines = f.read()
    total_plays = [lines[i] for i in range(len(lines)) if i % 2 == 0]

    player1 = Player("Player 1", "Y")
    player2 = Player("Player 2", "R")
    player1_plays = []
    player2_plays = []

    new_game = Game()
    print(new_game)
    for i in range(len(total_plays)):
        if i % 2 == 0:
            player1_plays.append(total_plays[i])
        else:
            player2_plays.append(total_plays[i])
    # as long as someone hasn't won and the game board isn't full
    while not new_game.is_game_over():
        count1 = 0
        count2 = 0
        new_game.move(player1, int(player1_plays.pop(count1)))
        print(new_game)
        count1 += 1
        if new_game.is_game_over():
            break
        new_game.move(player2, int(player2_plays.pop(count2)))
        print(new_game)
        count2 += 1
        if new_game.is_game_over():
            break

main()