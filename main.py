import tkinter as tk
import ttkbootstrap as ttk
from lookup_frame import LookupFrame
from entry_frame import EntryFrame

try:
	with open("recipes.txt", "r") as fin:
		pass # we're just trying to open it to see if it exists
except OSError:
	with open("recipes.txt", "w") as fout:
		pass

def switch_display_mode():
	if check_value.get() == "1":
		style.theme_use("darkly")
	else:
		style.theme_use("minty")

window = ttk.Window()
style= ttk.Style(theme= "minty")
window.geometry("740x1280") # you keep at 370x640

check_value = tk.StringVar()

top_bar = ttk.Frame(master= window)
dark_mode_toggle = ttk.Checkbutton(master= top_bar, text= "Toggle dark mode", variable= check_value, command= switch_display_mode)
dark_mode_toggle.pack(anchor= "w", pady= 10)
top_bar.pack(padx= 10, fill= "x")

notebook = ttk.Notebook(master= window)

lookup_frame = LookupFrame(master= notebook)
entry_frame = EntryFrame(master= notebook)

notebook.add(lookup_frame, text= "Lookup Recipes")
notebook.add(entry_frame, text= "Add Recipes")

notebook.pack(fill= "both")

window.mainloop()