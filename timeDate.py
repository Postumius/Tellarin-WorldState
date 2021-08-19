from typing import Text
import PySimpleGUI as sg 
import HypDate as hd

#dayRadio = [sg.Radio('Day 1', "dayRadio", default=True, key='day1'), sg.Radio('Day 2', "dayRadio", key='day2')]

today = hd.HypDate(0,0,0,0)

controlLayout = [
    [sg.Text('day:'), sg.Button('Next')],
    [sg.Text('Weather:'), sg.Input(key='weather')],
    [sg.Button('Update'), sg.Button('Close')]
]
controlWindow = sg.Window('Controls', controlLayout)

displayLayout = [ 
    [sg.Text('Day:'), 
        sg.Text(today.dayName(), size=(6,1), key='day')],
    [sg.Text('Weather:'), sg.Text(size=(15,1), key='weather')]
]
displayWindow = sg.Window('Display', displayLayout, finalize=True)

#print(controlLayout[0][0].Key)

def getRadioChoice(radioList, values):
    for radio in radioList:
        if values[radio.Key] == True:
            return radio.Text

while True:
    event, values = controlWindow.read()
    if event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks cancel
        break
    elif event == 'Next':        
        today = today.plus(hd.HypDate(0,0,0,1))
        print(today.show())
        displayWindow['day'].update(today.dayName())
    else:
        
        displayWindow['weather'].update(values['weather'])

controlWindow.close()
displayWindow.close()