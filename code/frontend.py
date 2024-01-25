import tkinter as tk
from tkinter import Canvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from data_import_editing import *

# pokemon = Pokemon('Bulbasaur')
# print(Bul.get_weaknesses())

# Create main window
root = tk.Tk()
root.title("Tkinter Square and Plot")

# Right Frame (Plot)
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

fig, ax = plt.subplots()
canvas_plot = FigureCanvasTkAgg(Pokemon('Bulbasaur').get_weaknesses(), master=right_frame)
canvas_plot.draw()
canvas_plot.get_tk_widget().pack()

# Entry for Square Size
entry_label = tk.Label(root, text="Enter Square Size:")
entry_label.pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

# Start Tkinter main loop
root.mainloop()
