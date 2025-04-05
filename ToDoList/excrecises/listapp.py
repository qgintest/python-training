

user_prompt = "Type ADD or SHOW or EDIT or COMPLETE or EXIT:"

todos = []


while True:
    user_action = input(user_prompt)

    match user_action.upper().strip():
        case 'ADD':
            todo = input("Enter a TODO: ")
            todos.append(todo)
        case 'SHOW' | 'DISPLAY':
            for index, item in enumerate(todos):
                print(f"{index+1}:{item}")

            print('Total Number of Items: ', len(todos))
        case 'EDIT':
            number = int(input("Which Item do you want to edit?"))
            number = number - 1
            print("Write new Item.. ")
            todos[number] = input()

        case 'COMPLETE':
            item = input('Which Task is Complete? ')
            todos.remove(item)
            # todos.pop(1) - removes based on index
            # todos.clear() - clears entire list
            print('Removed Item: ', item)

        case 'EXIT':

            break

        case _:
            print('Unknown option selected')

print("Program Terminated")



