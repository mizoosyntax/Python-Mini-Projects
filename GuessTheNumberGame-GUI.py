import tkinter as tk
import random

def guessTheNumber():
    stages = {
        'Stage 1': (1, 25),
        'Stage 2': (1, 50),
        'Stage 3': (1, 75),
        'Stage 4': (1, 100)
    }

    stageKeys = list(stages.keys())
    stageIndex = 0
    attempt = 0
    maxAttempts = 5
    stageRange = stages[stageKeys[stageIndex]]
    computerChoice = random.randint(stageRange[0], stageRange[1])

    def handleGuess():
        nonlocal stageIndex, attempt, computerChoice, stageRange
        try:
            userChoice = int(userEntry.get())
            feedbackLabel.config(text="")
        except ValueError:
            feedbackLabel.config(text = "Please enter a valid number.")
            return

        attempt += 1

        if userChoice == computerChoice:
            feedbackLabel.config(text = f"Correct! You won {stageKeys[stageIndex]}!")
            stageIndex += 1

            if stageIndex >= len(stageKeys):
                feedbackLabel.config(text = "Congratulations! You completed all stages!")
                guessButton.config(state = "disabled")
                return

            stageRange = stages[stageKeys[stageIndex]]
            computerChoice = random.randint(stageRange[0], stageRange[1])
            stageLabel.config(text = f"Stage {stageKeys[stageIndex]}: Guess between {stageRange[0]} and {stageRange[1]}")
            attempt = 0
        else:
            if userChoice > computerChoice:
                feedbackLabel.config(text = "Too high, try again!")
            else:
                feedbackLabel.config(text = "Too low, try again!")

        if attempt >= maxAttempts:
            feedbackLabel.config(text = f"Game Over! The number was {computerChoice}.")
            guessButton.config(state = "disabled")

    stageLabel.config(text = f"Stage {stageKeys[stageIndex]}: Guess between {stageRange[0]} and {stageRange[1]}")
    feedbackLabel.config(text = "")
    guessButton.config(command = handleGuess)


root = tk.Tk()
root.geometry("280x180")
root.title("Guess The Number Game")

stageLabel = tk.Label(root, text = "Click 'Start' to begin the game.")
feedbackLabel = tk.Label(root, text = "", fg = "red")
userEntry = tk.Entry(root)
guessButton = tk.Button(root, text="Guess", state = "disabled")
startButton = tk.Button(root, text="Start", command = lambda: [guessTheNumber(), guessButton.config(state = "normal")])

stageLabel.grid(row = 0, column = 0, columnspan = 3, pady = 10)
feedbackLabel.grid(row = 1, column = 0, columnspan = 3, pady = 5)
userEntry.grid(row = 2, column = 0, columnspan = 2, pady = 5)
guessButton.grid(row = 2, column = 2, padx = 5)
startButton.grid(row = 3, column = 1, pady = 10)

root.mainloop()
