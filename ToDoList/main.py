#print("Enter TODO Here:")

# input() #triggers on-demand mode, waiting for user input

user_prompt = "Enter TODO Here:"
todo1 = input(user_prompt) # creating a variable and assigning it to user's input
todo2 = input(user_prompt)
todo3 = input(user_prompt)

#print(todos)
todos = [todo1, todo2, todo3]
print(todos)

print(type(todos)) # prints out type of variable
print(type(user_prompt))