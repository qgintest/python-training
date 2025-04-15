FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Gets the content from the todos file"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(local_todos, filepath=FILEPATH):
    """
    Wriites content to a file
    :param local_todos:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(local_todos)


print(__name__)

if __name__ == "__main__":
    print('Howdy from functions module')
    print(get_todos())