import PySimpleGUI as sg  # import PySimpleGui
# print(sg)#Testing if module has been loaded in my Virtual environment
# all My functions are here...


def add(num1, num2):
   return num1+num2



# GUI Code Start Here
layout = [[sg.Text("Number One"), sg.Input(key='-num1-',enable_events=True)],
          [sg.Text("Number Two"), sg.Input(key='-num2-',enable_events=True)],
          [sg.Button("Add"), sg.Text(key='-problem-')]]
window = sg.Window("Calculator", layout)
while True:
    event, value = window.read()
    # print(event, value)
    try:
          if  event == '-num1-' and value['-num1-'][-1] not in ('0123456789.'):
                window['-num1-'].update(value['-num1-'][:-1])
          if  event == '-num2-' and value['-num2-'][-1] not in ('0123456789.'):
                window['-num2-'].update(value['-num2-'][:-1])
    except:
        pass
        
    match event:
        case sg.WIN_CLOSED: break
        case "Add":
                    try:
                            window['-problem-'].update("")
                            sg.popup(f"Your Answer Is {add(float(value['-num1-']),float(value['-num2-']))}",
                            auto_close=True, auto_close_duration=2, title="This is your Answer")  # print(add(int(value[0]),int(value[1])))
                   
                    except: 
                            print("You did something wrong with application")
                            window['-problem-'].update("You did something wrong with application")


window.close()

