
import FreeSimpleGUI as sg


label1 = sg.Text("Enter Feet")
input_box = sg.Input()

label2 = sg.Text("Enter Inches")
input_box2 = sg.Input()

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")

window = sg.Window("Converter",
                   layout=[[label1, input_box],
                           [label2, input_box2],
                           [convert_button, exit_button]])

while True:
    event, values = window.read() # Displays the window
    print(event, values)

    match event:
        case "Exit":
            break

window.close()

