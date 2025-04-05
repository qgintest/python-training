user_prompt = "Enter TODO Here:"

todos = []

while True:
    todo = input(user_prompt)
    todos.append(todo.capitalize())
    print(todos)