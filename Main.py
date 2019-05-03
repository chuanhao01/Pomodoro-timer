# importing libraries
from Class_Code.GUI_Class_Code import GUI_Framework_Code
from tkinter import *
from win10toast import ToastNotifier

# Notes for code below,
# For the list return after the button is pressed, [0] refers to number of sessions, [1] list of time per session
# [2] list of time per rest
# Problems with the code ATM:
# IDK how to implement reset button



# Declaring classes
class PomodoroTimer(GUI_Framework_Code):
    def __init__(self, master=None):
        GUI_Framework_Code.__init__(self, master)
        self.updateButtonButton.config(command=lambda :self.getUpdateAndStart())
        self.valuesList = 0
        self.checkPause = True
        self.checkRest = True

    # method to check time and update time
    def updateTime(self, time):
        if (time[1] == 0):
            time[0] -= 1
            time[1] = 59
            return time
        else:
            time[1] -= 1
            return time


    # method to call to check when time of timer is up
    def checkTimer(self):
        if (self.valuesList[0] == 0):
            # call done func, for now not implemented yet
            print('I\'m DONEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
        else:
            self.valuesList[0] -= 1


    # method for timerfunc, takes an array of time and counts down
    def timerFunc(self, time, type):
        if self.checkPause:
            if(time == [0,0]):
                if(type == "Timer"):
                    self.checkTimer()
                    self.timerFunc(self.valuesList[2], "Rest")
                elif(type == "Rest"):
                    self.timerFunc(self.valuesList[1], "Timer")
            else:
                time = self.updateTime(time)
                print("After 1s?", time, self.valuesList[1])
                self.after(1000, lambda :self.timerFunc(time, type))



    # Method called when update and start button is pressed
    def getUpdateAndStart(self):
        valuesList = self.getValuesFromComboBoxes()
        if valuesList == []:
            return
        print(valuesList)
        self.valuesList = (valuesList)
        self.timerFunc(self.valuesList[1], "Timer")



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

    # Takes a list as a arg when called. Used to check if all values in list are int. If blanks("") are present call
    # error code 1. If wrong type call error type 2. Returns [] if there is an error, else return list with all int values
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
        return self.formatValuesFromInput(values)

    # Method called after check is successful. Converts the minute and seconds in to seconds
    def formatValuesFromInput(self, values):
        listToReturn = []
        listToReturn.append(values[0])
        temp = []
        temp.append(values[1])
        temp.append(values[2])
        listToReturn.append(temp)
        temp = []
        temp.append(values[3])
        temp.append(values[4])
        listToReturn.append(temp)
        # print(listToReturn)
        return listToReturn

    # Takes in a selector and then decides what to update the timer label with(calling another method to update)
    def updateTimerLabel(self, selector):
        if selector == "Error Code 1":
            self.errorCode1TimerLabelUpdate()
        elif selector == "Error Code 2":
            self.errorCode2TimerLabelUpdate()

    # Update to timer label to show error code 1 message(blanks in configuration)
    def errorCode1TimerLabelUpdate(self):
        self.TimerLabel.config(text="There are some fields left blank when\nconfiguring the pomodoro timer", font=("Courier",9))
    # Update to timer label to show error code 2 message(Wrong variable type for input/ input not integers)
    def errorCode2TimerLabelUpdate(self):
        self.TimerLabel.config(text="There are some fields which are\nnot integers when configuring the\npomodoro timer", font=("Courier",9))



root = Tk()
root.geometry("450x360")
PomodoroTimer(root)
root.mainloop()
