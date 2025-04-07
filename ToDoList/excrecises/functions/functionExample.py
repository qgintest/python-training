
def getTodos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def writeTodos(filepath, local_todos):
    with open(filepath, 'w') as file_local:
        file_local.writelines(local_todos)


user_prompt = "Type ADD or SHOW or EDIT or COMPLETE or EXIT:"


while True:
    user_action = input(user_prompt)
    user_action = user_action.strip().upper()


    if user_action.startswith('ADD'):
            todo = user_action[4:]


            todos = getTodos(filepath='todos.txt')


            todos.append(todo + "\n")

            # store list in text file
            writeTodos('todos.txt', todos)


    elif user_action.startswith('SHOW'):

        todos = getTodos('todos.txt')

        for index, item in enumerate(todos):
            item = item.replace("\n", "")
            print(f"{index+1}:{item}")

        # print('Total Number of Items: ', len(todos))
    elif user_action.startswith('EDIT'):

        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = getTodos('todos.txt')

            new_todo = input("Enter new TODO")
            todos[number] = new_todo + '\n'

            writeTodos('todos.txt', todos)

        except ValueError:
            print('Your command is not valid')
            continue

    elif user_action.startswith('COMPLETE'):

        try:
            number = int((user_action[9:]))

            todos = getTodos('todos.txt')

            index = number - 1
            todos_to_remove = todos[index].strip('\n')
            todos.pop(index)

            writeTodos('todos.txt', todos)

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



