import PySimpleGUI as sg
from random import *

def calculations(times):
    head, tail, iterator = 0, 0, 0
    possibilities = ['head', 'tail']
    while iterator < (times):
        if choice(possibilities) == 'head':
            head +=1
            iterator +=1
        else:
            tail +=1
            iterator +=1
    return {"head":head, "tail": tail}

sg.theme('Black')
main_layout = [[sg.Text('How many times you want to toss a coin?')],
          [sg.Input(key='-input-', size=(8,1)), sg.Button('Next')],
          [sg.Button('Exit')]]

main_window = sg.Window('coinFlip', main_layout)
while True:
    event, value = main_window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    elif event == 'Next':
        times = value['-input-']
        try:
            times = int(times)
        except ValueError:
            main_window.Hide()
            error_layout = [[sg.Text(f'Ooops, wrong input. I need number, not {type(times)}')],
                              [sg.Button('Back')]]
            error_window = sg.Window('Error', error_layout)
            while True:
                event, value = error_window.read()
                if event == sg.WIN_CLOSED or 'Back':
                    error_window.Close()
                    main_window.UnHide()
                    break
        else:
            times = int(times)
            results = calculations(times)
            main_window.Hide()
            results_column = [[sg.Text('Heads:'), sg.Text(f"{results['head']} | {round((results['head']*100)/times,2)}%", key='-heads-', text_color='black', background_color='#eeeeee')],
                              [sg.Text('Tails:'), sg.Text(f"{results['tail']} | {round((results['tail']*100)/times,2)}%", key='-tails-', text_color='black', background_color='#eeeeee')]]
            results_frame = [[sg.Column(results_column, element_justification='right')]]
            results_layout = [[sg.Frame(f'Times: {times}', results_frame)],
                              [sg.Button('Back'), sg.Button('Refresh')]]
            results_window = sg.Window('Results', results_layout)
            while True:
                event, value = results_window.read()                
                if event == sg.WIN_CLOSED or event == 'Back':
                    results_window.Close()
                    main_window.UnHide()
                    break
                if event == 'Refresh':
                    results = calculations(times)
                    results_window['-heads-'].update(f"{results['head']} | {round((results['head']*100)/times,2)}%")
                    results_window['-tails-'].update(f"{results['tail']} | {round((results['tail']*100)/times,2)}%")
main_window.Close()
