# Function to get player's name
def get_player_name(player):
    return input(f"{player}, enter your name: ")


# Function to get player's input for placing X or O
def get_player_input(player_name, sign, board):
    while True:
        box_number = int(input(f"{player_name}, enter box number: "))
        row = (box_number - 1) // 3
        col = (box_number - 1) % 3

        # Check if row and column are within valid range
        if 0 <= row < 3 and 0 <= col < 3:
            # Check if the chosen box is empty
            if board[row][col] == ' ':
                board[row][col] = sign
                break
            else:
                print("Box already occupied! Try again.")
        else:
            print("Invalid box number! Try again.")


# Function to display the tic-tac-toe board
def show_board(board):
    print(
        f" {board[0][0]} | {board[0][1]} | {board[0][2]}\n" +
        "---+---+---\n" +
        f" {board[1][0]} | {board[1][1]} | {board[1][2]}\n" +
        "---+---+---\n" +
        f" {board[2][0]} | {board[2][1]} | {board[2][2]}\n"
    )


# Function to check if a player has won
def check_winner(board, sign):
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True  # Row win
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True  # Column win
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True  # Diagonal win (top-left to bottom-right)
    return board[0][2] == sign and board[1][1] == sign and board[2][
        0] == sign  # Diagonal win (top-right to bottom-left)


# Main function
def main():
    print(
        " 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9\n"
    )
    X = 'X'
    O = 'O'
    board = [[' ' for _ in range(3)] for _ in range(3)]

    # Get player names
    player_one = get_player_name("Player X")
    player_two = get_player_name("Player O")

    # Game loop
    for turn in range(9):
        if turn % 2 == 0:
            get_player_input(player_one, X, board)
        else:
            get_player_input(player_two, O, board)

        show_board(board)

        if check_winner(board, X):
            print(player_one + " wins!")
            break
        elif check_winner(board, O):
            print(player_two + " wins!")
            break

    if not check_winner(board, X) and not check_winner(board, O):
        print("It's a tie!")


# Entry point of the program
if __name__ == "__main__":
    main()
