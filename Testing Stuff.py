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
        self.getFrameForSettings()


    # To draw PomodoroSessionLabel in the main tkinter window
    def getPomodoroSessionLabel(self):
        # Temp frame to get the widgets to line up properly for now
        self.tempFrame = Frame(self, width=75, height=40)
        self.tempFrame.grid(row=0, column=0)
        # Code for framework of PomodoroSessionLabel widget
        self.PomodoroSessionLabelframe = LabelFrame(self, width=200, height=40)
        self.PomodoroSessionLabelframe.grid(row=0, column=1, columnspan=4)
        self.PomodoroSessionLabelframe.grid_propagate(False)
        self.PomodoroSessionLabelframe.rowconfigure(0, weight=1)
        self.PomodoroSessionLabelframe.columnconfigure(0, weight=1)
        self.PomodoroSessionLabel = Label(self.PomodoroSessionLabelframe, text="Pomodoro Session:__")
        self.PomodoroSessionLabel.grid(row=0, column=0, sticky="nsew")

    # To draw the Timer Label in the main tkinter window
    def getTimerLabel(self):
        self.TimerLabelframe = LabelFrame(self, height=80, width=300)
        self.TimerLabelframe.grid(row=1, column=1, columnspan=6, rowspan=2)
        self.TimerLabelframe.grid_propagate(False)
        self.TimerLabelframe.rowconfigure(0, weight=1)
        self.TimerLabelframe.columnconfigure(0, weight=1)
        self.TimerLabel = Label(self.TimerLabelframe, text="00:00", font=("Courier", 44))
        self.TimerLabel.grid(row=0, column=0, sticky="nsew")

    def getFrameForSettings(self):
        self.FrameForSettings = Frame(self, width=450, height=240)
        self.FrameForSettings.grid(row=3, column=0, rowspan=6, columnspan=9)
        self.getPomodoroSettings()
        self.getBreakSettings()
        self.getUpdateButton()
        self.getPauseandResetButtons()

    def getPomodoroSettings(self):
        pass

    def getBreakSettings(self):
        pass

    def getUpdateButton(self):
        pass

    def getPauseandResetButtons(self):
        pass


root = Tk()
root.geometry("450x360")
GUI_Framework_Code(root)
root.mainloop()