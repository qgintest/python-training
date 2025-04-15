import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)
    print(todos)
    st.session_state["new_todo"] = ""


# todos = [s.replace('\n', '') for s in todos]


st.title("My Todo App")
st.subheader("This is my TODO App")
st.write("add items one a a time")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a TODO: ", placeholder="Add a TODO",
              on_change=add_todo, key="new_todo")