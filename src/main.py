import game_of_life.universe as gol
from game_of_life.gui import GridFrame
import tkinter as tk

uni = gol.Universe()
uni.create()
root = tk.Tk()
board = GridFrame(root,30)
board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
root.mainloop()
