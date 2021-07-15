import PySimpleGUI as sg
import random

#sg.theme(random.choice(list(sg.LOOK_AND_FEEL_TABLE)))

layout = [ [sg.Text("Enter total amount in dollars:")],
            [sg.Input(default_text='100', key='-INPUT-')],
            [sg.Text("Select a tip percentage:")],
            [sg.Radio('5%', 'RADIO1', enable_events=True, key = "R1"), sg.Radio('10%', 'RADIO1', enable_events=True, key = "R2"), sg.Radio('15%', 'RADIO1', enable_events=True, key = "R3"), sg.Radio('Custom', 'RADIO1', enable_events=True, key = "R4")],
            [sg.Text("Enter custom tip amount:", key='prompt', visible=False)],
            [sg.Input(default_text='18', key='IN2', visible=False)],
            [sg.Button('Calculate', key='Calc')],
            [sg.Text(size=(40, 1), key='OUTPUT')]]

window = sg.Window('Hello world', layout)

while True:
    event, values = window.read()
    if(event == sg.WIN_CLOSED):
    	break
    if(event == 'R4'):
        window['prompt'].update(visible=True)
        window['IN2'].update(visible=True)
    if(event == 'R1'):
        window['prompt'].update(visible=False)
        window['IN2'].update(visible=False)
    if(event == 'R2'):
        window['prompt'].update(visible=False)
        window['IN2'].update(visible=False)
    if(event == 'R3'):
        window['prompt'].update(visible=False)
        window['IN2'].update(visible=False)
    msg = ""
    if(event == 'Calc'):
        if (values['-INPUT-'] != None):
            amount = int(values['-INPUT-'])
            msg = ""
            if(values["R1"] == True):
                msg = f'5% tip: {0.05 * amount}'
            if(values["R2"] == True):
                msg = f'10% tip: {0.1 * amount}'
            if(values["R3"] == True):
                msg = f'15% tip: {0.15 * amount}'
            if(values["R4"] == True):
                tip = int(values["IN2"])
                msg = f'{tip}% tip: {tip / 100 * amount}'
            window['OUTPUT'].update(msg)


window.close()
