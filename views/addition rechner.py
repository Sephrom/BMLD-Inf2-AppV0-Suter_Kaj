import streamlit as st
from functions.addition import add

st.title("additions rechner")

st.write("hier könnte ihre werbung stehen")


with st.form("addition_form"):
    a = st.number_input("Geben Sie die erste Zahl ein:")
    b = st.number_input("Geben Sie die zweite Zahl ein:")
    
    result = add(a, b)
    
    submit_button = st.form_submit_button("Berechnen")
if submit_button:
    st.write(f"Das Ergebnis ist: {result}")


    