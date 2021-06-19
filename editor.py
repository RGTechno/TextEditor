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

window.rowconfigure(0, minsize=500)
window.columnconfigure(1, minsize=500)
tools = tk.Frame(window)
# tools.grid(row=0, column=0, sticky="ns")
tools.pack(expand=True)
text_editor = tk.Text(window)
# text_editor.grid(row=0, column=1, sticky="nsew")
text_editor.pack()

open_button = tk.Button(tools, text="Open File", command=openFile)
open_button.grid(row=0, column=0, padx=3, pady=3)
# open_button.pack()

saveas_button = tk.Button(tools, text="Save As", command=saveAsFile)
saveas_button.grid(row=0, column=1, padx=3, pady=3)
# saveas_button.pack()

save_button = tk.Button(tools, text="Save", command=saveFile)
save_button.grid(row=0, column=2,padx=3, pady=3)
# save_button.pack()

window.bind("<Control-o>",lambda x:openFile())
window.bind("<Control-s>",lambda x:saveFile())

window.mainloop()
