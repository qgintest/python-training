

user_prompt = "Type ADD or SHOW or EDIT or COMPLETE or EXIT:"


while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action.upper().strip():
        case 'ADD':
            todo = input("Enter a TODO: ") + "\n"

            file = open('todos.txt', 'r') # read mode
            todos = file.readlines() # grab existing data from text and put it in list
            file.close()

            todos.append(todo)

            # store list in text file
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'SHOW' | 'DISPLAY':

            file = open('todos.txt', 'r')
              #file = open(r"folder\subfolder\todos.txt", 'r') # WINDOWS: cancels out escape characters
             #file = open("folder/subfolder/todos.txt", 'r') # MAC/Unix/Linux: cancels out escape characters

            todos = file.readlines()
            # items = file.readlines()
            # for item in items:
            #     item = item.replace("\n", "")
            #     print(item)

            file.close()

            for index, item in enumerate(todos):
                item = item.replace("\n", "")
                print(f"{index+1}:{item}")

            # print('Total Number of Items: ', len(todos))
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



