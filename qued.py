import queue
import time
import threading
import tkinter as tk
import random

q1 = queue.Queue()
q1.put(20)



root = tk.Tk()
root.geometry("500x500")
my_label = tk.Label(root,text="getting")
my_label.pack(pady= 20)
my_button = tk.Button(root, text="my text")
my_button.pack()

def update():
    if not q1.empty():
        x = q1.get()
        my_label.config(text="getting data : " + str(x))
    my_label.after(1000, update)


def threader():
    for i in range(10):
        time.sleep(1)
        q1.put(i)

threading.Thread(target=threader).start()
update()



root.mainloop()
