import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.comp_score = 0
        self.rounds_played = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors:")
        self.label.pack()

        self.button_rock = tk.Button(self.root, text="Rock", command=lambda: self.play_game("Rock"))
        self.button_rock.pack()

        self.button_paper = tk.Button(self.root, text="Paper", command=lambda: self.play_game("Paper"))
        self.button_paper.pack()

        self.button_scissors = tk.Button(self.root, text="Scissors", command=lambda: self.play_game("Scissors"))
        self.button_scissors.pack()

        self.button_play_again = tk.Button(self.root, text="Play Again", command=self.reset_game)
        self.button_play_again.pack()
        self.button_play_again.config(state=tk.DISABLED)

        self.label_score = tk.Label(self.root, text="")
        self.label_score.pack()

    def play_game(self, user_choice):
        comp_choice = random.choice(self.choices)

        result = self.determine_winner(user_choice, comp_choice)

        messagebox.showinfo("Result", f"User: {user_choice}\nComputer: {comp_choice}\nResult: {result}")

        if result == "Win":
            self.user_score += 1
        elif result == "Lose":
            self.comp_score += 1

        self.rounds_played += 1
        self.show_score()

        if self.rounds_played >= 3:  # Change this number for the desired rounds
            self.disable_buttons()
            messagebox.showinfo("Game Over", "Game over! Maximum rounds played.")

    def determine_winner(self, user_choice, comp_choice):
        if user_choice == comp_choice:
            return "Tie"
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Paper" and comp_choice == "Rock") or \
             (user_choice == "Scissors" and comp_choice == "Paper"):
            return "Win"
        else:
            return "Lose"

    def show_score(self):
        score_info = f"User: {self.user_score} | Computer: {self.comp_score} | Rounds Played: {self.rounds_played}"
        self.label_score.config(text=score_info)

    def reset_game(self):
        self.user_score = 0
        self.comp_score = 0
        self.rounds_played = 0
        self.enable_buttons()
        self.show_score()

    def disable_buttons(self):
        self.button_rock.config(state=tk.DISABLED)
        self.button_paper.config(state=tk.DISABLED)
        self.button_scissors.config(state=tk.DISABLED)
        self.button_play_again.config(state=tk.NORMAL)

    def enable_buttons(self):
        self.button_rock.config(state=tk.NORMAL)
        self.button_paper.config(state=tk.NORMAL)
        self.button_scissors.config(state=tk.NORMAL)
        self.button_play_again.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()

