import functions

import FreeSimpleGUI as sg

label = sg.Text("Manage your TO-DO List ")
input_box = sg.InputText(tooltip="Enter TODO")
add_button = sg.Button("Add")

window = sg.Window("TODO APP", layout=[[label], [input_box, add_button]])
window.read() # Displays the window
window.close()

