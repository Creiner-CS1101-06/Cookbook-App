import tkinter as tk
import ttkbootstrap as ttk

# options = ["Option 1", "Option 2", "Option 3", "Option 4"]
# combo = ttk.Combobox(master= window, values= options, state= 'readonly')
# combo.bind('<<ComboboxSelected>>', display_option)
# combo.set("Choose an option")
# combo.pack()

class LookupFrame(ttk.Frame):
	def __init__(self, master):
		super().__init__(master= master)
		# here we will actually do everything
		# that the lookup frame should do
		self.recipes_dict = self.get_recipes()
		self.desc_text = tk.StringVar()

		self.name_label = ttk.Label(master= self, text= "Choose Recipe")
		names = list(self.recipes_dict.keys())
		for i, name in enumerate(names):
			names[i] = name.strip()
		self.recipes_dropdown = ttk.Combobox(master= self, values= names, state= 'readonly')
		self.desc_label = ttk.Label(master= self, textvariable = self.desc_text)
		self.refresh_button = ttk.Button(master= self, text= "Refresh List", command= self.refresh_list)

		self.recipes_dropdown.bind("<<ComboboxSelected>>", self.display_recipe)

		self.name_label.pack()
		self.recipes_dropdown.pack()
		self.desc_label.pack()
		self.refresh_button.pack()

	def get_recipes(self):
		# TBD work in progress
		recipes_dict = {}
		with open("recipes.txt", "r") as fin:
			raw_list = fin.readlines() # return a list of the lines
		i = 0
		while i < len(raw_list)-1:
			name, desc, i = self.get_next_item(raw_list, i)
			recipes_dict[name] = desc
			i += 1
		return recipes_dict

	def get_next_item(self, raw_list, i):
		# assumption: line at index i is a name
		name = raw_list[i]
		i += 2
		desc = ""
		while raw_list[i].strip() != "###":
			desc += raw_list[i] # no stripping!
			i += 1
		return name, desc, i

	def display_recipe(self, thing):
		key = self.recipes_dropdown.get()
		key += "\n"
		description = self.recipes_dict[key]
		self.desc_text.set(description)

	def refresh_list(self):
		print("List refreshed")