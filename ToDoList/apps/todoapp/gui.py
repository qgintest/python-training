import functions

import FreeSimpleGUI as sg

label = sg.Text("Manage your TO-DO List ")
input_box = sg.InputText(tooltip="Enter TODO", key="todo")
add_button = sg.Button("Add")

# Displays the window
window = sg.Window("TODO APP",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()  # event returns as a tuple
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        case sg.WIN_CLOSED:
            break

window.close()