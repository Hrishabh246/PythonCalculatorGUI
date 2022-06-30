import PySimpleGUI as sg#import PySimpleGui
# print(sg)#Testing if module has been loaded in my Virtual environment
layout = [ [sg.Text("Hello"), sg.Button("OK")],[sg.Button("Cancel")]]
window =sg.Window("calculator", layout)
event,value = window.read()
# print(event,value)
window.close()

