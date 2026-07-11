from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("350x300")

choices = ["Rock", "Paper", "Scissors"]

result = Label(root, text="Click a button to play!", font=("Arial", 12))
result.pack(pady=20)

def play(user):
    computer = random.choice(choices)

    if user == computer:
        text = "Draw!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        text = "You Win!"
    else:
        text = "Computer Wins!"

    result.config(text="You: " + user +
                       "\nComputer: " + computer +
                       "\n" + text)

Button(root, text="Rock", width=15, command=lambda: play("Rock")).pack(pady=5)

Button(root, text="Paper", width=15, command=lambda: play("Paper")).pack(pady=5)

Button(root, text="Scissors", width=15, command=lambda: play("Scissors")).pack(pady=5)

root.mainloop()