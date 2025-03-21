from tkinter import Tk, Canvas, ttk, StringVar
import tkinter

# Function to handle button click
def on_button_click(value):
    current = entry.get()
    entry.delete(0, tkinter.END)
    entry.insert(0, current + value)

# Function to evaluate the expression
def evaluate_expression():
    try:
        # Replace the '^' with '**' for exponentiation
        expression = entry.get().replace("^", "**")
        result = eval(expression)
        entry.delete(0, tkinter.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tkinter.END)
        entry.insert(0, "cant divide by zero")

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tkinter.END)

# Hover effect for buttons
def on_enter(event):
    event.widget.config(highlightbackground="#FFFFFF", highlightcolor="#FFFFFF", highlightthickness=2)

def on_leave(event):
    event.widget.config(highlightbackground=event.widget.cget("bg"), highlightthickness=0)

# Create the main window
window = Tk()
window.title("Calculator")
window.geometry("400x500")  # This sets the window size

# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Get the window width and height
window_width = 400
window_height = 500

# Calculate the position for the window to be centered
position_top = int((screen_height - window_height) / 2)
position_left = int((screen_width - window_width) / 2)

# Set the window geometry with the calculated position
window.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')

window.configure(bg="#000000")  # Black background for the iPhone look

# Entry widget for the expression
entry = tkinter.Entry(
    window,
    width=16,
    font=("Arial", 24),
    borderwidth=2,
    relief="solid",
    bg="#000000",  # Black background
    fg="#FFFFFF",  # White text
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons for the calculator
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("(", 5, 1), (")", 5, 2), ("^", 5, 3),
]

# Styling for buttons
button_colors = {
    "number": "#333333",  # Dark gray
    "operator": "#FF9500",  # Orange
    "special": "#A5A5A5",  # Light gray
    "text": "#FFFFFF"  # White text
}

# Add buttons to the grid
for (text, row, col) in buttons:
    if text in "0123456789.":
        bg_color = button_colors["number"]
    elif text in "+-*/^=()":
        bg_color = button_colors["operator"]
    else:  # Clear button
        bg_color = button_colors["special"]
    
    button = tkinter.Button(
        window,
        text=text,
        font=("Arial", 18),
        bg=bg_color,
        fg=button_colors["text"],
        activebackground="#666666",
        activeforeground="#FFFFFF",
        command=(evaluate_expression if text == "=" else
                 clear_entry if text == "C" else
                 lambda value=text: on_button_click(value)),
        highlightthickness=0,  # Initially no outline
        borderwidth=0,
        width=5,
        height=2
    )
    
    # Bind hover effects
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    # Adjust grid position to make buttons centered
    button.grid(row=row, column=col, padx=10, pady=10)

# Run the application
window.mainloop()
