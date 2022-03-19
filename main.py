import streamlit as st

st.write("# Welcome to dineGraph")

food = st.text_input("What have you eaten today? ")
calories = st.text_input("Calorie of the food: ")

if food and calories is None:
    st.write("Nothing written")
else:
    st.write(f"Food: {food} , Calories of {food}: {calories}")
