import tkinter as tk

from tkinter.filedialog import *

window = tk.Tk()  # Initializes Tkinter window

window.title("Zorro Editor")  # Gives window a Title

window.rowconfigure(0, minsize=600)
window.columnconfigure(1, minsize=600)


window.mainloop()
