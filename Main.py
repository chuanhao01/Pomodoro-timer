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

    # Method for updating time by 1s
    def updateTimePerS(self, valuesList, selector):
        if (selector == "Timer"):
            selector = 1
        elif(selector == "Rest"):
            selector = 2
        valuesList[selector][1] -= 1
        return valuesList


    # method for rest
    def restTimer(self, valuesList):
        checkPause = True
        checkRest = True
        while(checkPause):
            while(checkRest):
                checkPause = self.checkPause
                checkRest = self.checkRest
                valuesList = self.checkTimeRemaining(valuesList, "Rest")
                valuesList = self.updateTimePerS(valuesList, "Rest")
                print("Hi2")
                self.after(1000)
            return


    # method to check if time has depleted
    def checkTimeRemaining(self, valuesList, selector):
        if (selector == "Timer"):
            selector = 1
        elif(selector == "Rest"):
            selector = 2
        #   if time is depleted reset and check if its
        if (valuesList[selector] == [0,0]):
            valuesList[selector] = self.valuesList[selector]
            if (selector == 1):
                valuesList[0] -= 1
                self.restTimer(valuesList)
            elif (selector == 2):
                self.checkRest = False
            return valuesList
        elif(valuesList[selector][1] == 0):
            valuesList[selector][0] -= 1
            valuesList[selector][1] = 60
            return valuesList
        else:
            return valuesList



    # method called to start promodoro timer
    def startTimer(self, valuesList):
        checkPause = True
        # checks is pause button has been pressed
        while(checkPause):
            # if the number of sessions is larger than 0 i.e. there are more session
            while(valuesList[0]>0):
                checkPause = self.checkPause
                valuesList = self.checkTimeRemaining(valuesList, "Timer")
                valuesList = self.updateTimePerS(valuesList, "Timer")
                print("Hi1")
                self.after(1000)
            return

    # Method called when update and start button is pressed
    def getUpdateAndStart(self):
        valuesList = self.getValuesFromComboBoxes()
        if valuesList == []:
            return
        print(valuesList)
        self.valuesList = valuesList
        self.startTimer(valuesList)



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
