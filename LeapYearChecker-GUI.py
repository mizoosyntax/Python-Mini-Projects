import tkinter as tk

def leapYearChecker():
    year = yearEntry.get()

    try:
        year = int(year)
        if year <= 0:
            resultLabel.config(text = "Please enter a positive year.")
        elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            resultLabel.config(text = f"{year} is a leap year!")
        else:
            resultLabel.config(text = f"{year} is not a leap year.")
    except ValueError:
        resultLabel.config(text = "Invalid input. Please enter a valid year.")

root = tk.Tk()
root.title("Leap Year Checker")
root.geometry("320x60")

yearLabel = tk.Label(root, text = "Enter Year:")
yearEntry = tk.Entry(root)
checkButton = tk.Button(root, text = "Check", command = leapYearChecker)
resultLabel = tk.Label(root)

yearLabel.grid(padx = 5, pady = 5, row = 0, column = 0)
yearEntry.grid(pady = 5, row = 0, column = 1)
checkButton.grid(pady = 5, row = 0, column = 2)
resultLabel.grid(row = 1, columnspan = 3)

root.mainloop()