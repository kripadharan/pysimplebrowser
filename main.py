import PySimpleGUI as sg
import random
from pwafeats import *

#sg.theme(random.choice(list(sg.LOOK_AND_FEEL_TABLE)))

layout = [  [sg.Button('Choose Text File', key = 'CFILE')],
            [sg.Text(size=(40, 1), key = 'Contents')],
            [sg.Button('Choose Image File', key = 'CFILE2')],
            [sg.Image(size=(40, 1), key = 'Img')],
            [sg.Button('Start Video', key = 'VidStart'), sg.Button('End Video', key = 'VidEnd')]]

window = sg.Window('Hello world', layout)
contents = "test"
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
    if(event == 'CFILE'):
        contents = selOpenFile()   
        print(contents)
        window['Contents'].update(contents)
    if(event == 'CFILE2'):
        image = selOpenImgFile()
        window['Img'].update(image)
    if(event == 'VidStart'):
         vidId = startVideoFeed()
    if(event == 'VidEnd'):
         endVideoFeed()
window.close()
