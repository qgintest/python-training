
def getTodos():
    with open('todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


user_prompt = "Type ADD or SHOW or EDIT or COMPLETE or EXIT:"


while True:
    user_action = input(user_prompt)
    user_action = user_action.strip().upper()


    if user_action.startswith('ADD'):
            todo = user_action[4:]


            todos = getTodos()


            todos.append(todo + "\n")

            # store list in text file
            with open('todos.txt', 'w') as file:
                file.writelines(todos)


    elif user_action.startswith('SHOW'):

        todos = getTodos()

        for index, item in enumerate(todos):
            item = item.replace("\n", "")
            print(f"{index+1}:{item}")

        # print('Total Number of Items: ', len(todos))
    elif user_action.startswith('EDIT'):

        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = getTodos()

            new_todo = input("Enter new TODO")
            todos[number] = new_todo + '\n'


            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        except ValueError:
            print('Your command is not valid')
            continue

    elif user_action.startswith('COMPLETE'):

        try:
            number = int((user_action[9:]))

            todos = getTodos()

            index = number - 1
            todos_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

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



