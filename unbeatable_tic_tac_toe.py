import tkinter as tk
from tkinter import messagebox

def terminal(board, player):
    win = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8),(0, 4, 8), (2, 4, 6)] #combinations to win
    for combo in win:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def check_draw(board):
    if " " not in board:
        return True
    return False

def minimax(board, is_maximizing):      
    if terminal(board, "X"):
        return -1
    if terminal(board, "O"):
        return 1
    if check_draw(board):
        return 0

    if is_maximizing:           #max player turn
        best_score = -1000      #-infinity
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:                      #min player turn
        best_score = 1000      #+infinity
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -1.0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move_index = i
    return best_move_index

def make_move(index):
    if board[index] == " " and not game_over:
        buttons[index].config(text="X", font=('normal',20,'bold'), state="disabled")
        board[index] = "X"
        if terminal(board, "X"):
            win = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8),(0, 4, 8), (2, 4, 6)] #combinations to win
            for combo in win:
                if board[combo[0]] == board[combo[1]] == board[combo[2]] == "X":
                    buttons[combo[0]].config(bg="lime")
                    buttons[combo[1]].config(bg="lime")
                    buttons[combo[2]].config(bg="lime")
            messagebox.showinfo("Tic Tac Toe", "Player X wins!")
            end_game()

        elif check_draw(board):
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            end_game()

        else:
            ai_move()

def ai_move():
    index = best_move(board)
    if index is not None:
        buttons[index].config(text="O", font=('normal',20,'bold'), state="disabled")
        board[index] = "O"
        if terminal(board, "O"):
            win = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8),(0, 4, 8), (2, 4, 6)] #combinations to win
            for combo in win:
                if board[combo[0]] == board[combo[1]] == board[combo[2]] == "O":
                    buttons[combo[0]].config(bg="lime")
                    buttons[combo[1]].config(bg="lime")
                    buttons[combo[2]].config(bg="lime")
            messagebox.showinfo("Tic Tac Toe", "Player O wins!")
            end_game()
        elif check_draw(board):
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            end_game()

def reset_board():
    global board, game_over
    board = [" " for i in range(9)]
    game_over = False
    for button in buttons:
        button.config(text=" ", bg="white", state="normal")

def end_game():
    global game_over
    game_over = True

# Create the GUI
window = tk.Tk()
window.title("Tic Tac Toe")

buttons = []
board = [" " for i in range(9)]
game_over = False

for i in range(9):
    button = tk.Button(window, text=" ", font=('normal', 20,'bold'), height=2, width=5, command= lambda x=i: make_move(x))
    buttons.append(button)
    row = i // 3
    col = i % 3
    button.grid(row=row, column=col)

# Add Reset Button
reset_button = tk.Button(window, text="Reset", command=reset_board)
reset_button.grid(row=3, column=0, columnspan=3, sticky="we")

# Add Exit Button
exit_button = tk.Button(window, text="Exit", command=window.destroy)
exit_button.grid(row=4, column=0, columnspan=3, sticky="we")

window.mainloop()
