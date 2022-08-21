import matplotlib
matplotlib.use("TkAgg") # Agg rendering to a Tk canvas (requires TkInter), where Ag renders png files
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk # Fancier buttons. See the difference between buttons using tk.Button and ttk.Button

import urllib
import json

import pandas as pd
import numpy as np

LARGE_FONT = ("Verdana", 12)
style.use("ggplot")

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111) # 111 = 1 row, 1 column, index 1


def animate(i):
	pullData = open("data.txt","r").read()
	dataList = pullData.split('\n')
	xList = []
	yList = []
	for eachLine in dataList:
		if len(eachLine)>1:
			x, y = eachLine.split(',')
			xList.append(int(x))
			yList.append(int(y))

	a.clear()
	a.plot(xList, yList)


class SeaofBTCapp(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		# tk.Tk.iconbitmap(self, default="icon.ico") # doesn't work on Ubuntu 16.04
		tk.Tk.wm_title(self, "Sea of BTC Client")

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, BTCe_Page):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()


class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="ALPHA Bitcoin trading application.\n"
									"Use at your own risk.\n"
									"There is no promise of warranty", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = ttk.Button(self, text="Agree", command=lambda: controller.show_frame(BTCe_Page))
		button1.pack()
		button2 = ttk.Button(self, text="Disagree", command=quit)
		button2.pack()


class PageOne(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page One", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
		button1.pack()
		button2 = tk.Button(self, text="Visit Page Two", command=lambda: controller.show_frame(PageTwo))
		button2.pack()


class BTCe_Page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
		button1.pack()



		canvas = FigureCanvasTkAgg(f, self)
		canvas.draw() # In Python 3.4, this is canvas.show() (used in the tutorial series). For 3.7, it is draw()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True) # Could use grid here as well

		toolbar = NavigationToolbar2Tk(canvas, self)
		toolbar.update()
		#canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)




app = SeaofBTCapp()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()
# print(help(SeaofBTCapp))