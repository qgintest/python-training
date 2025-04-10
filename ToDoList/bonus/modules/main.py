
def get_todos(filepath="todos.txt"):
    """Gets the content from the todos file"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(local_todos, filepath="todos.txt"):
    """
    Wriites content to a file
    :param local_todos:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(local_todos)



user_prompt = "Type ADD or SHOW or EDIT or COMPLETE or EXIT:"

text = """
    Can store values in a variable in this multi-line text
    second line
    third line
"""

print(text)

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip().upper()


    if user_action.startswith('ADD'):
            todo = user_action[4:]


            todos = get_todos()


            todos.append(todo + "\n")

            # store list in text file
            write_todos(todos)


    elif user_action.startswith('SHOW'):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.replace("\n", "")
            print(f"{index+1}:{item}")

        # print('Total Number of Items: ', len(todos))
    elif user_action.startswith('EDIT'):

        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new TODO")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print('Your command is not valid')
            continue

    elif user_action.startswith('COMPLETE'):

        try:
            number = int((user_action[9:]))

            todos = get_todos()

            index = number - 1
            todos_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"TODO {todos_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print('Your command is not valid')
            continue

    elif user_action.startswith('EXIT'):
        break

    else:
        print('Unknown option selected')

print("Program Terminated")



