import tkinter as tk
from tkinter.constants import END

from tkinter.filedialog import *

def openFile():
    global file
    file = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not file:
        return
    text_editor.delete(1.0, tk.END)
    with open(file, "r") as ifile:
        notes = ifile.read()
        text_editor.insert(tk.END, notes)
    window.title(file + " - Zorro Editor")

def saveAsFile():
    global file
    file = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not file:
        return
    # else:
    #     print(file)
    with open(file, "w") as ofile:  # File handling with open() => Opens file
        notes = text_editor.get(1.0, tk.END)
        ofile.write(notes)
    window.title(file + " - Zorro Editor")

def saveFile():
    if not file:
        return
    with open(file, "w") as ofile:  # File handling with open() => Opens file
        notes = text_editor.get(1.0, tk.END)
        ofile.write(notes)
    window.title(file + " - Zorro Editor")
    print("Saved")

window = tk.Tk()  # Initializes Tkinter window

window.title("Zorro Editor")  # Gives window a Title

window.rowconfigure(0, minsize=600)
window.columnconfigure(1, minsize=600)

text_editor = tk.Text(window)
text_editor.grid(row=0, column=1, sticky="nsew")

tools = tk.Frame(window, relief=tk.RAISED, bd=2)
tools.grid(row=0, column=0, sticky="ns")

open_button = tk.Button(tools, text="Open File", command=openFile)
open_button.grid(row=0, column=0, padx=3, pady=3)

saveas_button = tk.Button(tools, text="Save As", command=saveAsFile)
saveas_button.grid(row=0, column=1, padx=3, pady=3)

save_button = tk.Button(tools, text="Save", command=saveFile)
save_button.grid(row=1, column=0)

window.bind("<Control-o>",lambda x:openFile())
window.bind("<Control-s>",lambda x:saveFile())

window.mainloop()
