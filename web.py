import streamlit as st
from modules import functions
import time


todos = functions.get_todos()
clock = time.strftime("%d %b %Y")

def add_todo():
        todo = st.session_state["new_todo"] + "\n"
        todos.append(todo)
        functions.write_todos(todos)

def edit_todo():
    todo = st.session_state["edit_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My ToDo App")
st.subheader("This is my ToDo App")
st.write("This app is to increase your productivity.")
st.write("Today is " + time.strftime("%d %b %Y"))

col1, col2 = st.columns(2)

with col1:
    st.subheader("What to do:")
    for index, todo in enumerate(todos):
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            st.error("Do you want to edit or delete this task?")
            if st.button("Delete"):
                todos.pop(index)
                functions.write_todos(todos)
                del st.session_state[todo]
                st.experimental_rerun()
            if st.button("Edit"):
                todos.pop(index)
                new_todo = st.text_input(label="Enter new ToDo instead of this ToDo", on_change=edit_todo,
                                         key="edit_todo")

with col2:
    st.subheader("Date added:")
    for index, todo in enumerate(todos):
        st.write(clock)

st.text_input(label="Enter a ToDo", placeholder="Add new ToDo...", on_change=add_todo, key='new_todo')
