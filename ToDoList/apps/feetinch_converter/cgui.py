
import FreeSimpleGUI as sg
from bonus.convertersFunction import convert

enter_feet_label = sg.Text("Enter feet:")
enter_feet_input_box = sg.Input(key="feet")

enter_inches_label = sg.Text("Enter inches:")
enter_inches_input_box = sg.Input(key="inches")

convert_button = sg.Button("Convert")
exit_button = sg.Button('Exit')
meter_output = sg.Text(key="Output", text_color="white")

window = sg.Window("Converter",
                   layout=[[enter_feet_label, enter_feet_input_box],
                           [enter_inches_label, enter_inches_input_box],
                           [convert_button, exit_button, meter_output]])

while True:
    event, values = window.read() # Displays the window
    print(event, values)
    print(type(values["feet"]))
    print(values["feet"])

    if event == "Exit":
        break

    try:
        feet = int(values["feet"])
        inches = float(values["inches"])
        meters = round(convert(feet, inches), 3)
        window["Output"].update(f"{meters} m")
    except ValueError:
        sg.popup("Please Enter a Value for Feet and Inches")

window.close()

