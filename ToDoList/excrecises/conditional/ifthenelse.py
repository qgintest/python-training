# if-else
# list slicing

user_prompt = "Type ADD or SHOW or EDIT or COMPLETE or EXIT:"


while True:
    user_action = input(user_prompt)
    user_action = user_action.strip().upper()
    #print(user_action)


    if 'ADD' in user_action or 'new' in user_action:
            todo = user_action[4:] + "\n"


            with open('todos.txt', 'r') as file:
                todos = file.readlines() # grab existing data from text and put it in list


            todos.append(todo)

            # store list in text file
            with open('todos.txt', 'w') as file:
                file.writelines(todos)


    elif 'SHOW' in user_action:

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.replace("\n", "")
            print(f"{index+1}:{item}")

        # print('Total Number of Items: ', len(todos))
    elif 'EDIT' in user_action:

        with open('todos.txt', 'r') as file:
            todos = file.readlines()  # grab existing data from text and put it in list

        number = int(input("Which Item do you want to edit?"))
        number = number - 1
        print("Write new Item.. ")

        todos[number] = input()


    elif 'COMPLETE' in user_action:

        with open('todos.txt', 'r') as file:
            todos = file.readlines()  # grab existing data from text and put it in list

        item = input('Which Task is Complete? ')
        todos.remove(item)
        print('Removed Item: ', item)

    elif 'EXIT' in user_action:
        break

    else:
        print('Unknown option selected')

print("Program Terminated")



