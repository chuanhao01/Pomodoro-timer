from tkinter import *
import time

def blink():
    e.config(bg='green')
    time.sleep(1)
    e.config(bg="white")
    # e.after(1000, lambda: e.config(bg='white')) # after 1000ms

root = Tk()
root.geometry('200x200')
e = Entry(root)
e.pack()
b = Button(root, text='blink', command=blink)
b.pack()
root.mainloop()