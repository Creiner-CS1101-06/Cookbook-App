import tkinter as tk
import ttkbootstrap as ttk

class LookupFrame(ttk.Frame):
	def __init__(self, master):
		super().__init__(master= master)
		# here we will actually do everything
		# that the lookup frame should do