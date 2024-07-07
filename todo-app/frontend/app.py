import streamlit as st
import requests

backend_url = "http://backend:8000"  # Change to your FastAPI backend URL if needed

st.title("To-Do App")

title = st.text_input("Title")
description = st.text_input("Description")

if st.button("Add To-Do"):
    response = requests.post(
        f"{backend_url}/todos/",
        json={"title": title, "description": description}
    )
    if response.status_code == 200:
        st.success("To-Do added successfully!")
    else:
        st.error("Failed to add To-Do")

if st.button("Get To-Dos"):
    response = requests.get(f"{backend_url}/todos/")
    if response.status_code == 200:
        todos = response.json()
        for todo in todos:
            st.write(f"Title: {todo['title']}, Description: {todo['description']}, Completed: {todo['completed']}")
    else:
        st.error("Failed to fetch To-Dos")
