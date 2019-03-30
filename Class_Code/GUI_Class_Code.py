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
        self.tempFrame = Frame(self, width=50, height=40)
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
        self.FrameForSettings.grid_propagate(False)
        self.getPomodoroSettings()
        self.getBreakSettings()
        self.getUpdateButton()
        self.getPauseandResetButtons()

    def getPomodoroSettings(self):
        # Drawing the label for Number of Pomodoro Sessions
        self.numberOfPomodoroSessionsLabelframe = LabelFrame(self.FrameForSettings, height=40, width=110)
        self.numberOfPomodoroSessionsLabelframe.grid(row=0, column=0, columnspan=2)
        self.numberOfPomodoroSessionsLabelframe.grid_propagate(False)
        self.numberOfPomodoroSessionsLabelframe.rowconfigure(0, weight=1)
        self.numberOfPomodoroSessionsLabelframe.columnconfigure(0, weight=1)
        self.numberOfPomodoroSessionsLabel = Label(self.numberOfPomodoroSessionsLabelframe, text="Number of\nPomodoro Sessions")
        self.numberOfPomodoroSessionsLabel.grid(row=0, column=0, sticky="nsew")
        # Drawing ComoboBox for number of Sessions
        self.numberOfPomodoroSessionsFrame = Frame(self.FrameForSettings, height=40, width=110)
        self.numberOfPomodoroSessionsFrame.grid(row=1, column=0, columnspan=2)
        self.numberOfPomodoroSessionsFrame.grid_propagate(False)
        self.numberOfPomodoroSessionsFrame.rowconfigure(0, weight=1)
        self.numberOfPomodoroSessionsFrame.columnconfigure(0, weight=1)
        self.numberOfPomodoroSessionsComboBox = ttk.Combobox(self.numberOfPomodoroSessionsFrame)
        self.numberOfPomodoroSessionsComboBox.grid(row=0, column=0, sticky="nsew")
        # No. of minutes for pomodoro
        self.numberOfMinutesForPomodoroLabelframe = LabelFrame(self.FrameForSettings, width=110, height=40)
        self.numberOfMinutesForPomodoroLabelframe.grid(row=0, column=2, columnspan=2)
        self.numberOfMinutesForPomodoroLabelframe.grid_propagate(False)
        self.numberOfMinutesForPomodoroLabelframe.rowconfigure(0, weight=1)
        self.numberOfMinutesForPomodoroLabelframe.columnconfigure(0, weight=1)
        self.numberOfMinutesForPomodoroLabel = Label(self.numberOfMinutesForPomodoroLabelframe, text="Number of minutes\nfor Pomodoro")
        self.numberOfMinutesForPomodoroLabel.grid(row=0, column=0, sticky="nsew")
        # Draw ComboBox for number of Minutes
        self.numberOfMinutesForPomodoroFrame = Frame(self.FrameForSettings, width=110, height=40)
        self.numberOfMinutesForPomodoroFrame.grid(row=1, column=2, columnspan=2)
        self.numberOfMinutesForPomodoroFrame.grid_propagate(False)
        self.numberOfMinutesForPomodoroFrame.rowconfigure(0, weight=1)
        self.numberOfMinutesForPomodoroFrame.columnconfigure(0, weight=1)
        self.numberOfMinutesForPomodoroComboBox = ttk.Combobox(self.numberOfMinutesForPomodoroFrame)
        self.numberOfMinutesForPomodoroComboBox.grid(row=0, column=0, sticky="nsew")
        # Draw number of seconds for pomodoro
        self.numberOfSecondsForPomodoroLabelframe = LabelFrame(self.FrameForSettings, width=110, height=40)
        self.numberOfSecondsForPomodoroLabelframe.grid(row=0, column=4, columnspan=2)
        self.numberOfSecondsForPomodoroLabelframe.grid_propagate(False)
        self.numberOfSecondsForPomodoroLabelframe.rowconfigure(0, weight=1)
        self.numberOfSecondsForPomodoroLabelframe.columnconfigure(0, weight=1)
        self.numberOfSecondsForPomodoroLabel = Label(self.numberOfSecondsForPomodoroLabelframe, text="Number of minutes\nfor Pomodoro")
        self.numberOfSecondsForPomodoroLabel.grid(row=0, column=0, sticky="nsew")
        # Draw number of seconds for pomodoro Combobox
        self.numberOfSecondsForPomodoroFrame = Frame(self.FrameForSettings, width=110, height=40)
        self.numberOfSecondsForPomodoroFrame.grid(row=1, column=4, columnspan=2)
        self.numberOfSecondsForPomodoroFrame.grid_propagate(False)
        self.numberOfSecondsForPomodoroFrame.rowconfigure(0, weight=1)
        self.numberOfSecondsForPomodoroFrame.columnconfigure(0, weight=1)
        self.numberOfSecondsForPomodoroComboBox = ttk.Combobox(self.numberOfSecondsForPomodoroFrame)
        self.numberOfSecondsForPomodoroComboBox.grid(row=0, column=0, sticky="nsew")

    def getBreakSettings(self):
        # Draw Number of Minutes for Break Label
        self.numberOfMinutesForBreakLabelframe = LabelFrame(self.FrameForSettings, width=110, height=40)
        self.numberOfMinutesForBreakLabelframe.grid(row=2, column=0, columnspan=2)
        self.numberOfMinutesForBreakLabelframe.grid_propagate(False)
        self.numberOfMinutesForBreakLabelframe.rowconfigure(0, weight=1)
        self.numberOfMinutesForBreakLabelframe.columnconfigure(0, weight=1)
        self.numberOfMinutesForBreakLabel = Label(self.numberOfMinutesForBreakLabelframe, text="Number of minutes\nfor Pomodoro")
        self.numberOfMinutesForBreakLabel.grid(row=0, column=0, sticky="nsew")
        # Draw Number Of Minutes for Break Combobox
        self.numberOfMinutesForBreakFrame = Frame(self.FrameForSettings, width=110, height=40)
        self.numberOfMinutesForBreakFrame.grid(row=3, column=0, columnspan=2)
        self.numberOfMinutesForBreakFrame.grid_propagate(False)
        self.numberOfMinutesForBreakFrame.rowconfigure(0, weight=1)
        self.numberOfMinutesForBreakFrame.columnconfigure(0, weight=1)
        self.numberOfMinutesForBreakComboBox = ttk.Combobox(self.numberOfMinutesForBreakFrame)
        self.numberOfMinutesForBreakComboBox.grid(row=0, column=0, sticky="nsew")
        # Draw Number of Seconds for Break Label
        self.numberOfSecondsForBreakLabelframe = LabelFrame(self.FrameForSettings, width=110, height=40)
        self.numberOfSecondsForBreakLabelframe.grid(row=2, column=2, columnspan=2)
        self.numberOfSecondsForBreakLabelframe.grid_propagate(False)
        self.numberOfSecondsForBreakLabelframe.rowconfigure(0, weight=1)
        self.numberOfSecondsForBreakLabelframe.columnconfigure(0, weight=1)
        self.numberOfSecondsForBreakLabel = Label(self.numberOfSecondsForBreakLabelframe, text="Number of Seconds\nfor Break")
        self.numberOfSecondsForBreakLabel.grid(row=0, column=0, sticky="nsew")
        # Draw Number of Seconds for Break Combobox
        self.numberOfSecondsForBreakFrame = Frame(self.FrameForSettings, width=110, height=40)
        self.numberOfSecondsForBreakFrame.grid(row=3, column=2, columnspan=2)
        self.numberOfSecondsForBreakFrame.grid_propagate(False)
        self.numberOfSecondsForBreakFrame.rowconfigure(0, weight=1)
        self.numberOfSecondsForBreakFrame.columnconfigure(0, weight=1)
        self.numberOfSecondsForBreakComboBox = ttk.Combobox(self.numberOfSecondsForBreakFrame)
        self.numberOfSecondsForBreakComboBox.grid(row=0, column=0, sticky="nsew")

    def getUpdateButton(self):
        pass

    def getPauseandResetButtons(self):
        pass


root = Tk()
root.geometry("450x360")
GUI_Framework_Code(root)
root.mainloop()