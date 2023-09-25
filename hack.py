from farmbot import FarmBot
from interface import PyWindow
import PySimpleGUI as sg

window = PyWindow().window

farmbot = FarmBot()

while True:

    event, values = window.read(timeout=1)
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    if event != sg.TIMEOUT_KEY:
        if event == '-FARMSTART-':
            farmbot.set_to_begin(values)
            farmbot.botting = not farmbot.botting
       

    if farmbot.botting:
        farmbot.runHack()
        window['-FARMSTART-'].update('STOP')
    else:
        window['-FARMSTART-'].update('START')

    

window.close()
