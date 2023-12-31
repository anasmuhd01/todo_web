import function
import streamlit as st

todos = function.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    function.write_todos(todos)


st.title("To Do ✅")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input("Enter New TO DO ", on_change=add_todo, key='new_todo')

st.caption("! if todo is done click to remove !")
# st.session_state

