import PySimpleGUI as sg
from random import *


# layout settings
sg.theme('Dark Brown 1')
layout = [[sg.Text('How many times you want me to flip a coin?')],
          [sg.Input(key='-times-',size=(9,1)),sg.Button('Show')],
          [sg.Text('Times: '), sg.Text(key='-repeats-', size=(28,1))],
          [sg.Text('Heads: '),sg.Text(key='-heads-', size=(9,1)),sg.Text(key='-headsPerc-', size=(4,1)),sg.Text("%")],
          [sg.Text('Tails: '),sg.Text(key='-tails-', size=(9,1)),sg.Text(key='-tailsPerc-', size=(4,1)),sg.Text("%")],
          [sg.Button('Exit')]]
window = sg.Window('coinFlip', layout)

# mainloop with logic
while True:
    event, values = window.read(0)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        if values['-times-'].isalpha():
            repeatsSize = (30,1)
            values['-times-'] = 'Input number, not alphabeth!'
            window['-repeats-'].update(values['-times-'])
            
        else:
            heads, iterator, tails = 0,0,0
            times = values['-times-']
            outcome = ['head', 'tail']
            while iterator < int(times):
                if choice(outcome) == 'tail':
                    tails += 1
                    iterator += 1
                else:
                    heads += 1
                    iterator += 1
            
            window['-repeats-'].update(values['-times-'])
            window['-heads-'].update(heads)
            window['-headsPerc-'].update(round((heads/int(times))*100, 2))
            window['-tails-'].update(tails)
            window['-tailsPerc-'].update(round((tails/int(times))*100, 2))

window.close()
