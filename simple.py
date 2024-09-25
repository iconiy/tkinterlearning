import PySimpleGUI as sg

layout = [  [sg.Text('Hello World!')],
            [sg.Text('I am a program')],
            [sg.Button('Yes'), sg.Button('No')]
]

window = sg.Window('My Window', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'No':
        break


window.close()