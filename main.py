import PySimpleGUI as sg  # import PySimpleGui
# print(sg)#Testing if module has been loaded in my Virtual environment
# all My functions are here...


def add(num1, num2):
    return num1+num2


# GUI Code Start Here
layout = [[sg.Text("Number One"), sg.Input()],
          [sg.Text("Number Two"), sg.Input()],
          [sg.Button("Add")]]
window = sg.Window("Calculator", layout)
while True:
    event, value = window.read()
    print(event, value)
    match event:
        case sg.WIN_CLOSED: break
        case "Add": sg.popup(f"Your Answer Is {add(int(value[0]),int(value[1]))}",
                             auto_close=True, auto_close_duration=3, title="This is your Answer")  # print(add(int(value[0]),int(value[1])))


window.close()
# editing file from Duo and now predator
