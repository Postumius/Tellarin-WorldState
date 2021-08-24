from tkinter import font
from typing import Text
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button, theme_background_color 
import HypDate as hd
import Saving

today = hd.HypDate.fromList(Saving.load())

controlLayout = [
    [sg.Text('year:'), sg.Input(size=(5,1), key='year',
        default_text=str(today.year))],
    [sg.Text('season:'), sg.Input(size=(5,1), key='season',
        default_text=str(today.season+1)),
     sg.Text(today.seasonName(), size=(6,1), key='seasonName')],
    [sg.Text('cycle:'), sg.Input(size=(5,1), key='cycle',
        default_text=str(today.cycle+1))],
    [sg.Text('day:'), sg.Input(size=(5,1), key='day',
        default_text=str(today.day+1)),
     sg.Text(today.dayName(), size=(6,1), key='dayName'),
     sg.Button('Prev', key='prevDay'), 
     sg.Button('Next', key='nextDay')],
    [sg.Text('hour:'), sg.Input(size=(5,1), key='hour',
        default_text=str(today.hour)),
     sg.Button('Prev', key='prevHour'), 
     sg.Button('Next', key='nextHour')],
    [sg.Text('Weather:'), sg.Input(size=(25,1), key='weather')],
    [sg.Text('Location:'), sg.Input(size=(25,1), key='location')],
    [sg.Button('Bring to Front'), sg.Button('Send to Back')],
    [sg.Button('Update'), sg.Button('Close')]
]
controlWindow = sg.Window('Controls', controlLayout)

displayColumn = [    
    [sg.Text('Date: '), 
     sg.Text(today.dateName(), size=(25,1), key='date')],
    [sg.Text('Hour: '),
     sg.Text(str(today.hour), size=(25,1), key='hour')],
    [sg.Text('Weather: '), sg.Text(size=(25,1), key='weather')],
    [sg.Text('Location: '), sg.Text(size=(25,1), key='location')]
]

dayList = []
for dayName in hd.dayNames:
    dayList.append(sg.Text(dayName, font=('helvetica', 35), 
        key=dayName, pad=(10,0)))

displayLayout = [ 
    dayList,
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

def updateControl():
        controlWindow['year'].update(str(today.year))
        controlWindow['seasonName'].update(today.seasonName())
        controlWindow['season'].update(str(today.season+1))
        controlWindow['cycle'].update(str(today.cycle+1))
        controlWindow['dayName'].update(today.dayName())
        controlWindow['day'].update(str(today.day+1))
        controlWindow['hour'].update(str(today.hour))

displayWindow[today.dayName()].update(background_color='black')

while True:
    event, values = controlWindow.read()
    displayWindow[today.dayName()].update(background_color=theme_background_color())  
    if event == sg.WIN_CLOSED or event == 'Close':
        break
    elif event == 'nextDay':               
        today = today.plus(hd.HypDate(day=1))                 
    elif event == 'prevDay':        
        today = today.plus(hd.HypDate(day=-1))
    elif event == 'nextHour':        
        today = today.plus(hd.HypDate(hour=1))  
    elif event == 'prevHour':        
        today = today.plus(hd.HypDate(hour=-1))
    elif event == 'Bring to Front':
        displayWindow.BringToFront()
    elif event == 'Send to Back':
        displayWindow.SendToBack()
        
    else:
        try:
            today.year = int(values['year'])
        except: 
            0

        try:
            today.season = int(values['season'])-1
        except: 
            0

        try:
            today.cycle = int(values['cycle'])-1
        except: 
            0

        try:
            today.day = int(values['day'])-1
        except: 
            0 

        try:
            today.hour = int(values['hour'])
        except: 
            0      
    
    today = today.plus(hd.HypDate())
    updateControl()

    displayWindow['date'].update(today.dateName())
    displayWindow['hour'].update(str(today.hour))
    displayWindow['weather'].update(values['weather'])
    displayWindow['location'].update(values['location'])
    displayWindow[today.dayName()].update(background_color='black')

Saving.save(today.toList())
controlWindow.close()
displayWindow.close()