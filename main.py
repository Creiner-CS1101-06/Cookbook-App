import tkinter as tk
import ttkbootstrap as ttk
from lookup_frame import LookupFrame
from entry_frame import EntryFrame

window = ttk.Window(themename= "minty")
window.geometry("740x1280") # you keep at 370x640

notebook = ttk.Notebook(master= window)

lookup_frame = LookupFrame(master= notebook)
entry_frame = EntryFrame(master= notebook)

notebook.add(lookup_frame, text= "Lookup Recipes")
notebook.add(entry_frame, text= "Add Recipes")

notebook.pack(fill= "both")

window.mainloop()