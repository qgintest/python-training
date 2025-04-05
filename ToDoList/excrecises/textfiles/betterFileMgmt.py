
###With context manager

user_prompt = "Type ADD or SHOW or EDIT or COMPLETE or EXIT:"


while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action.upper().strip():
        case 'ADD':
            todo = input("Enter a TODO: ") + "\n"

            # don't have to close when using with context
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            # store list in text file
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'SHOW' | 'DISPLAY':

            with open('todos.txt', 'r')as file:
             #file = open(r"folder\subfolder\todos.txt", 'r') # WINDOWS: cancels out escape characters
             #file = open("folder/subfolder/todos.txt", 'r') # MAC/Unix/Linux: cancels out escape characters

                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.replace("\n", "")
                print(f"{index+1}:{item}")

            # print('Total Number of Items: ', len(todos))
        case 'EDIT':
            number = int(input("Which Item do you want to edit?"))
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            print('Existing TODOS', todos)

            print("Write new Item.. ")
            todos[number] = input() + "\n"

            print('NEW TODOS', todos)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'COMPLETE':
            item = int(input('Which Task is Complete? '))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = item - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(item - 1)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"TODO {todo_to_remove} was removed from the list."
            # todos.pop(1) - removes based on index
            # todos.clear() - clears entire list
            print(message)

        case 'EXIT':

            break

        case _:
            print('Unknown option selected')

print("Program Terminated")



