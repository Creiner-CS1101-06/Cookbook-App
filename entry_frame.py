import tkinter as tk
import ttkbootstrap as ttk

class EntryFrame(ttk.Frame):
	def __init__(self, master):
		super().__init__(master= master)
		# here we will actually do everything
		# that the lookup frame should do
		self.name_text = tk.StringVar()
		self.status_text= tk.StringVar()

		self.name_label = ttk.Label(master= self, text= "Name of Recipe")
		self.name_entry = ttk.Entry(master= self, textvariable= self.name_text)
		self.desc_label = ttk.Label(master= self, text= "Instructions")
		self.desc_entry = ttk.Text(master= self, width= 30, height= 15)
		self.add_button = ttk.Button(master= self, text= "Add Recipe", command= self.add_recipe)
		self.status_label = ttk.Label(master= self, textvariable= self.status_text)

		self.name_label.pack()
		self.name_entry.pack()
		self.desc_label.pack()
		self.desc_entry.pack()
		self.add_button.pack()
		self.status_label.pack()

	def add_recipe(self):
		recipe_name = self.name_text.get() # grab the recipe name from the Tkinter Variable
		recipe_desc = self.desc_entry.get(1.0, 'end') # gets the actual recipe from the Text widget
		with open("recipes.txt", 'a') as fin:
			print(recipe_name, file= fin)
			print("###", file= fin)
			print(recipe_desc, file= fin)
			print("###", file= fin)
		self.status_text.set("Recipe added successfully.")

