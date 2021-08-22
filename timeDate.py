from typing import Text
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button 
import HypDate as hd

#dayRadio = [sg.Radio('Day 1', "dayRadio", default=True, key='day1'), sg.Radio('Day 2', "dayRadio", key='day2')]

today = hd.HypDate(0,0,0,0)

controlLayout = [
    [sg.Text('year:'), sg.Input(size=(5,1), key='year')],
    [sg.Text('season:'), sg.Input(size=(5,1), key='season'),
     sg.Text(today.seasonName(), size=(6,1), key='seasonName')],
    [sg.Text('cycle:'), sg.Input(size=(5,1), key='cycle')],
    [sg.Text('day:'), sg.Input(size=(5,1), key='day'),
     sg.Text(today.dayName(), size=(6,1), key='dayName'),
     sg.Button('Prev'), sg.Button('Next')],
    [sg.Text('hour:'), sg.Input(size=(5,1), key='hour')],
    [sg.Text('Weather:'), sg.Input(size=(25,1), key='weather')],
    [sg.Text('Location:'), sg.Input(size=(25,1), key='location')],
    [sg.Button('Update'), sg.Button('Close')]
]
controlWindow = sg.Window('Controls', controlLayout)

displayColumn = [
    [sg.Text('Date:'), 
     sg.Text(today.dateName(), size=(25,1), key='date')],
    [sg.Text('Hour:'),
     sg.Text(str(today.hour), size=(25,1), key='hour')],
    [sg.Text('Weather:'), sg.Text(size=(25,1), key='weather')],
    [sg.Text('Location:'), sg.Text(size=(25,1), key='location')]
]

displayLayout = [ 
    [sg.Text(key='-EXPAND-', font='ANY 1', pad=(0, 0))],
    [sg.Column(displayColumn, vertical_alignment='center', key='-C-')]
]

displayWindow = sg.Window('Display', displayLayout, 
    finalize=True, resizable=True, 
    font=('helvetica', 50),
    auto_size_text=True,
    element_padding=(0,15))

displayWindow['-C-'].expand(True, True, True)
displayWindow['-EXPAND-'].expand(True, True, True)

while True:
    event, values = controlWindow.read()
    if event == sg.WIN_CLOSED or event == 'Close':
        break
    elif event == 'Next':        
        today = today.plus(hd.HypDate(day=1))  
    elif event == 'Prev':        
        today = today.plus(hd.HypDate(day=-1))
        
    else:
        try:
            today.year = int(values['year'])
        except: 
            today.year = 0

        try:
            today.season = int(values['season'])-1
        except: 
            today.season = 0

        try:
            today.cycle = int(values['cycle'])-1
        except: 
            today.cycle = 0

        try:
            today.day = int(values['day'])-1
        except: 
            today.day = 0  

        try:
            today.hour = int(values['hour'])
        except: 
            today.hour = 0      
    
    today = today.plus(hd.HypDate())
    controlWindow['year'].update(str(today.year))
    controlWindow['seasonName'].update(today.seasonName())
    controlWindow['season'].update(str(today.season+1))
    controlWindow['cycle'].update(str(today.cycle+1))
    controlWindow['dayName'].update(today.dayName())
    controlWindow['day'].update(str(today.day+1))
    controlWindow['hour'].update(str(today.hour))

    displayWindow['date'].update(today.dateName())
    displayWindow['hour'].update(str(today.hour))
    displayWindow['weather'].update(values['weather'])
    displayWindow['location'].update(values['location'])

    print(today.toList())

controlWindow.close()
displayWindow.close()