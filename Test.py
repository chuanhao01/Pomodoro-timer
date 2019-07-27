from tkinter import *
class GUI(Frame):
    def __init__(self, master = True):
        Frame.__init__(self, master)
        self.master = master
        self.master.title('Tkinter')


root = Tk()
root.geometry('147x147')
GUI(root)
root.mainloop()