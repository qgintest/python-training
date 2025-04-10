from functions import get_todos, write_todos
# import functions -- another way to import but you have to call method such as functions.get_todos()
import time

now = time.strftime("%Y-%m-%d-%H:%M:%S")
print(now)

while True:
    user_prompt = "Type ADD or SHOW or EDIT or COMPLETE or EXIT:"

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



