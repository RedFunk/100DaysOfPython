import PySimpleGUI as sg
from datetime import datetime
from datetime import timedelta

# Initialize variables
timer_running = False
timer_value = timedelta(hours=(int(5)/60))

def setTimer(timer_start_value):
    global timer_value
    timer_value = timedelta(hours=(int(timer_start_value)/60))


sg.theme('DarkAmber')   # Add a touch of color
sg.set_options(font=("Courier New", 16))

# All the stuff inside your window.
layout = [  [sg.Text('0:05:00', key="timer")],
            [sg.Text('Timer:'), 
             sg.InputText(key="timer_start_value", 
                          default_text=5, 
                          enable_events=True), 
             sg.Text('min')],
            [sg.Button('Start', key="btn_start"), 
             sg.Button('Stop', key="btn_stop"), 
             sg.Button('Reset', key="btn_reset")] ]

# Create the Window
window = sg.Window('Pomodoro Timer (Day 03)', layout, 
                   finalize=True)
window['timer_start_value'].bind("<KP_Enter>", "_Enter")

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read(timeout=1000)
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    if event == 'timer_start_value' and not timer_running:
        try:
            int(values["timer_start_value"])
            setTimer(values["timer_start_value"])
        except:
            pass
    
    if event == "btn_start":
        timer_running = True
    if event == "btn_stop":
        timer_running = False
    if event == "btn_reset":
        timer_running = False
        setTimer(values["timer_start_value"])
    
    if timer_running and timer_value > timedelta(hours=0):
        timer_value -= timedelta(hours=(1/3600))

    # Update the timer display      
    window['timer'].update(timer_value)
    
    
    
window.close()