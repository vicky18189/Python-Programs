import PySimpleGUI as sg

layout = [
    [
    sg.Input(key='-INPUT-'),
    sg.Spin(['km to mile', 'kg to pound', 'sec to min'],
            initial_value='km to mile', key='-UNITS-'),
    sg.Button('Convert', key='-CONVERT-')
    ],
    [sg.Text('Output', key='-OUTPUT-')]
]

window = sg.Window('Convertor', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'km to mile':
                    output_value = round(float(input_value) * 0.621371, 2)
                    output_string = f'{input_value} km is {output_value} miles'
                case 'sec to min':
                    output_value = round(float(input_value) / 60,2)
                    output_string = f'{input_value} seconds is {output_value} minutes'
                case 'kg to pound':
                    output_value = round(float(input_value) * 2.20462, 2)
                    output_string = f'{input_value} kg is {output_value} pounds'
                
            window['-OUTPUT-'].update(output_string)
        else:
            window['-OUTPUT-'].update('Please enter a number')
window.close()