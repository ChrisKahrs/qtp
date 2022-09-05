# from curses import keyname
import queue
import time
import threading
import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

q1 = queue.Queue()
q1.put(0)

root = tk.Tk()
root.geometry("500x500")
my_label = tk.Label(root,text="getting")
my_label.pack(pady= 20)
my_button = tk.Button(root, text="my text")
my_button.pack()
counter = 0

fig = Figure(figsize=(10, 4), dpi=100)
# t = np.arange(0, 3, .01)
t = [1]
y = [10]
u = [2]
z = [20]
tm = 1
xx = 1
ax = fig.add_subplot()
line, = ax.plot(t, y)

ax.set_xlim(0,30)
ax.set_ylim(0,20)
line2, = ax.plot(u, z)
ax.set_xlabel("time [s]")
ax.set_ylabel("f(t)")

my_input = tk.Button(root, text = "start")
my_input.pack()

def clicker(event):
    print("in clicker")
    global counter
    if event.keysym == "Up":
        counter += 1
    if event.keysym == "Down":
        counter -= 1
    my_input.config(text = "Counter = " + str(counter))
    my_input.pack()

root.bind("<Key>",clicker)
my_input.pack(pady=20)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()

def update():
    global tm
    global xx
    if not q1.empty():
        xx = q1.get()
        my_label.config(text="getting data : " + str(xx))
    y.append(xx)
    tm += 1
    t.append(tm)
    line.set_data(t, y)
    u.append(tm+2)
    z.append(xx+4)
    line2.set_data(u,z)
    canvas.draw()
    root.focus_set()
    my_label.after(1000, update)

def threader():
    for i in range(10):
        time.sleep(1)
        q1.put(i)

threading.Thread(target=threader).start()
update()

# pack_toolbar=False will make it easier to use a layout manager later on.
toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()

# canvas.mpl_connect(
#     "key_press_event", lambda event: print(f"you pressed {event.key}"))
# canvas.mpl_connect("key_press_event", key_press_handler)

button_quit = tk.Button(master=root, text="Quit", command=root.quit)

def update_frequency(new_val):
    # retrieve frequency
    f = float(new_val)

    # update data
    # y = 2 * np.sin(2 * np.pi * f * t)
    t.append(f+2)
    y.append(f)
    
    line.set_data(t, y)
    line2.set_data(u,z)

    # required to update canvas and attached toolbar!
    canvas.draw()


slider_update = tk.Scale(root, from_=1, to=5, orient=tk.HORIZONTAL,
                              command=update_frequency, label="Frequency [Hz]")

# Packing order is important. Widgets are processed sequentially and if there
# is no space left, because the window is too small, they are not displayed.
# The canvas is rather flexible in its size, so we pack it last which makes
# sure the UI controls are displayed as long as possible.
button_quit.pack(side=tk.BOTTOM)
slider_update.pack(side=tk.BOTTOM)
toolbar.pack(side=tk.BOTTOM, fill=tk.X)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.bind("<Key>",clicker)
root.focus_set()


root.mainloop()
