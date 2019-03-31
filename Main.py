# importing libraries
from Class_Code.GUI_Class_Code import GUI_Framework_Code
from tkinter import *
from win10toast import ToastNotifier

# Declaring classes
class PomodoroTimer(GUI_Framework_Code):
    def __init__(self, master=None):
        GUI_Framework_Code.__init__(self, master)
        self.updateButtonButton.config(command=lambda :self.getUpdateAndStart())


    def getUpdateAndStart(self):
        valuesList = self.getValuesFromComboBoxes()


    def getValuesFromComboBoxes(self):
        listToReturn = []
        listToReturn.append(self.numberOfPomodoroSessionsComboBox.get())
        listToReturn.append(self.numberOfMinutesForPomodoroComboBox.get())
        listToReturn.append(self.numberOfSecondsForPomodoroComboBox.get())
        listToReturn.append(self.numberOfMinutesForBreakComboBox.get())
        listToReturn.append(self.numberOfSecondsForBreakComboBox.get())
        # print(listToReturn)
        # print(self.checkValuesType(listToReturn))
        return self.checkValuesType(listToReturn)

    def checkValuesType(self, values):
        for i in range(len(values)):
            if values[i] == "":
                self.updateTimerLabel("Error Code 1")
                return []
            try:
                values[i] = int(values[i])
            except:
                self.updateTimerLabel("Error Code 2")
                return []
        return values

    # Takes in a selector and then decides what to update the timer label with
    def updateTimerLabel(self, selector):
        if selector == "Error Code 1":
            print("Error Code 1")
        elif selector == "Error Code 2":
            print("Error Code 2")

root = Tk()
root.geometry("450x360")
PomodoroTimer(root)
root.mainloop()