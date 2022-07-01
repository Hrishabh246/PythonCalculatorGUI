import PySimpleGUI as sg  # import PySimpleGui
# print(sg)#Testing if module has been loaded in my Virtual environment
layout = [[sg.Text("Hello this is a practice for GUI",key='-OUT-'),
           sg.Button("OKBye")], [sg.Button("Change")]]
window = sg.Window("calculator", layout, margins=(100, 50))
while True:
    event, value = window.read()
    print(event,value)
    if event == sg.WIN_CLOSED:
        break
    if event == "Change":
        window['-OUT-'].update(f'you clicked  {event}')
        print(type(event))
    


window.close()
# editing file from Duo and now predator
