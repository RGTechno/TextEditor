import tkinter as tk

from tkinter.filedialog import *

def saveFile():
    fileLocation = asksaveasfilename(
        defaultextension = "txt",
        filetypes=[("Text Files","*.txt"),("All Files","*.*")]
    )

    if not fileLocation:
        return
    # else:
    #     print(fileLocation)
    with open(fileLocation,"w") as ofile:  # File handling with open() => Opens file
        notes = text_editor.get(1.0,tk.END)
        ofile.write(notes)
    window.title(fileLocation + " - Zorro Editor")

window = tk.Tk()  # Initializes Tkinter window

window.title("Zorro Editor")  # Gives window a Title

window.rowconfigure(0, minsize=600)
window.columnconfigure(1, minsize=600)

text_editor = tk.Text(window)
text_editor.grid(row=0, column=1, sticky="nsew")

tools = tk.Frame(window, relief=tk.RAISED, bd=2)
tools.grid(row=0, column=0, sticky="ns")

open_button = tk.Button(tools, text="Open File")
open_button.grid(row=0, column=0, padx=3, pady=3)

save_button = tk.Button(tools, text="Save As",command=saveFile)
save_button.grid(row=0, column=1, padx=3, pady=3)

window.mainloop()
