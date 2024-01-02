from tkinter import font
from typing import Text
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button, theme_background_color, theme_button_color, theme_element_background_color, theme_element_text_color, theme_input_background_color, theme_slider_color, theme_text_element_background_color 
import HypDate as hd
import Saving

(ls, weather, location) = Saving.load()
today = hd.HypDate.fromList(ls)

control_state_layout = [
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
    [sg.Text('Weather:'), 
     sg.Input(size=(25,1), key='weather',
        default_text=weather)],
    [sg.Text('Location:'), 
     sg.Input(size=(25,1), key='location',
        default_text=location)],
]

control_ac_layout = [
    [
        sg.Column(
            [[sg.Text('Name'),],] +
            [[sg.Input(justification='right', key='name ' + str(i))] for i in range(6)],
            element_justification='right',
        ),
        sg.Column(
            [[sg.Text('AC'),],] +
            [[sg.Input(size=(2,1), key='AC ' + str(i))] for i in range(6)]
        ),
    ]
]

control_layout = [
    [sg.TabGroup(
        [
            [sg.Tab('World State', control_state_layout, tooltip='World State', key="state tab"),
             sg.Tab('ACs', control_ac_layout, tooltip='ACs', key="ac tab")],    
        ],
        enable_events=True,
        key="active tab")],
    [sg.Button('Bring to Front'), sg.Button('Send to Back')],
    [sg.Button('Update'), sg.Button('Close')],
]
controlWindow = sg.Window('Controls', control_layout)



display_state_column = [    
    [sg.Text('Date: '), 
     sg.Text(today.dateName(), size=(25,1), key='date')],
    [sg.Text('Hour: '),
     sg.Text(str(today.hour), size=(25,1), key='hour')],
    [sg.Text('Weather: '), 
     sg.Text(weather, size=(25,1), key='weather')],
    [sg.Text('Location: '), 
     sg.Text(location, size=(25,1), key='location')]
]

dayList = []
for dayName in hd.dayNames:
    dayList.append(
        sg.Column(
            [[
                sg.Text(dayName, font=('helvetica', 35), 
                    key=dayName,)
            ]],
            expand_x=True, element_justification='center'
        ))

display_state_layout = [ 
    dayList,
    [sg.Text(key='-EXPAND-', font='ANY 1', pad=(0, 0))],
    [sg.Column(display_state_column, vertical_alignment='center', key='-C-')]
]

display_ac_column = [
    [
        sg.Column(
            [[sg.Text('Name: '),],] +
            [[sg.Text(key='name ' + str(i))] for i in range(6)],
            element_justification='right',
        ),
        sg.Column(
            [[sg.Text('AC'),],] +
            [[sg.Text(key='AC ' + str(i))] for i in range(6)]
        ),
    ]
]

display_ac_layout = [
    [sg.Text(key='-EXPAND-', font='ANY 1', pad=(0, 0))],
    [sg.Column(display_ac_column, vertical_alignment='center', key='-C-')],
]

display_layout = [
    [sg.Column(display_state_layout, key="state tab"),
     sg.Column(display_ac_layout, visible=False, key="ac tab")]
]

display_col_keys = ['state tab', 'ac tab']

displayWindow = sg.Window('Display', display_layout, 
    finalize=True, resizable=True, 
    font=('helvetica', 50),
    auto_size_text=True,
    element_padding=(0,15))

displayWindow['-C-'].expand(True, True, True)
displayWindow['-EXPAND-'].expand(True, True, True)       
displayWindow[today.dayName()].update(background_color=theme_button_color()[1])

while True:
    event, values = controlWindow.read()
    #print(values)
    #print(event)
    displayWindow[today.dayName()].update(background_color=theme_background_color()) 

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
    elif event == 'active tab':
        for key in display_col_keys:
            if key == values['active tab']:
                displayWindow[key].update(visible=True)
            else:
                displayWindow[key].update(visible=False)
    
    today = today.plus(hd.HypDate())
    weather = values['weather']
    location = values['location']

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
    displayWindow[today.dayName()].update(
        background_color=theme_button_color()[1])
    for i in range(6):
        name = 'name ' + str(i)
        ac = 'AC ' + str(i)
        displayWindow[name].update(values[name] + ': ' if values[name] else '')
        displayWindow[ac].update(values[ac])


Saving.save(
    today.toList(),
    weather or '',
    location or '')
controlWindow.close()
displayWindow.close()
