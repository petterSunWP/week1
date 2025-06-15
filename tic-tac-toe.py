# tic_tac_toe.py

def print_board(board):
    """Prints the current state of the board."""
    print("\n")
    for index, row in enumerate(board):
        print(" | ".join(row))
        if index != len(board) - 1:
            print("-" * 10)
    print("\n")


def is_winner(board, player):
    """Checks if the given player has won."""
    win_states = [
        # rows
        board[0], board[1], board[2],
        # columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player] * 3 in win_states


def is_full(board):
    """Checks if the board is full."""
    return all(cell in ["X", "O"] for row in board for cell in row)


def get_move(player):
    """Prompts the player for their move."""
    while True:
        try:
            move = input(f"Player {player}, enter your move (row and col: 1 1): ")
            row, col = map(int, move.strip().split())
            if 1 <= row <= 3 and 1 <= col <= 3:
                return row - 1, col - 1
            else:
                print("Invalid input. Row and col must be between 1 and 3.")
        except ValueError:
            print("Please enter row and col as two numbers, e.g., 1 2.")


def play_game():
    """Main function to play the game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row, col = get_move(current_player)
        if board[row][col] != " ":
            print("That cell is already taken. Try again.")
            continue

        board[row][col] = current_player
        print_board(board)

        if is_winner(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()
