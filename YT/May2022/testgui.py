import PySimpleGUI as sg

layout = [
    [sg.Text('Text', enable_events= True, key='-TEXT-'), sg.Spin(['Item 1', 'Item 2', 'Item 3'], initial_value='Item 2')],
    [sg.Button('Button', key = '-BUTTON1-')],
    [sg.Input(key='-INPUT-')],
    [sg.Text('Hello'), sg.Button('Button', key = '-BUTTON2-')]
]

window = sg.Window('Convertor', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON1-':
        window['-TEXT-'].update(values['-INPUT-'])

    if event == '-BUTTON2-':
        print('OK Pressed')
        
    if event == '-TEXT-':
        print('Text Pressed')
window.close()
