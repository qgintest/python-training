import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open('todos.txt', 'w') as file:
        pass

#sg.theme("White")

clock = sg.Text('', key="Clock")
label = sg.Text("Manage your TO-DO List ")
input_box = sg.InputText(tooltip="Enter TODO", key="todo")
add_button = sg.Button("Add")
#add_button = sg.Button(size=2, image_source="add.png", mouseover_colors="LightBlue2", tooltip="Add Todo", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

# Displays the window
window = sg.Window("TODO APP",
                   layout=layout,
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)  # event returns as a tuple

    # print(1, event)
    # print(2, values)
    # print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)

            except IndexError:
               sg.popup('Please Select an Item First', font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Please Select an Item First', font=("Helvetica", 20))
        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            window.close()
            break

    window["Clock"].update(value=time.strftime("%Y-%m-%d-%H:%M:%S"))

#window.close()
#exit()  # terminates program entirely