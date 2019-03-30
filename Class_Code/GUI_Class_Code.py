# importing libraries
from tkinter import *
from tkinter import ttk

# class code
class GUI_Framework_Code(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Pomodoro-Timer")
        self.pack(fill=BOTH, expand=1)
        self.getPomodoroSessionLabel()
        self.getTimerLabel()
        self.getPomodoroSettings()
        self.getBreakSettings()
        self.getUpdateButton()
        self.getPauseandResetButtons()

    def getPomodoroSessionLabel(self):
        # Temp frame to get the widgets to line up properly for now
        self.tempFrame = Frame(self, width=100, height=40)
        self.tempFrame.grid(row=0, column=0)
        # Code for framework of PomodoroSessionLabel widget
        self.PomodoroSessionLabelframe = LabelFrame(self, width=200, height=40)
        self.PomodoroSessionLabelframe.grid(row=0, column=1, columnspan=2)
        self.PomodoroSessionLabelframe.grid_propagate(False)
        self.PomodoroSessionLabelframe.rowconfigure(0, weight=1)
        self.PomodoroSessionLabelframe.columnconfigure(0, weight=1)
        self.PomodoroSessionLabel = Label(self.PomodoroSessionLabelframe, text="Pomodoro Session:__")
        self.PomodoroSessionLabel.grid(row=0, column=0, sticky="nsew")

    def getTimerLabel(self):
        pass

    def getPomodoroSettings(self):
        pass

    def getBreakSettings(self):
        pass

    def getUpdateButton(self):
        pass

    def getPauseandResetButtons(self):
        pass


root = Tk()
root.geometry("500x500")
GUI_Framework_Code(root)
root.mainloop()