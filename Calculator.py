import streamlit as st
import math

# Define the style for the circular buttons
button_style = "border-radius: 50%; height: 50px; width: 50px; font-size: 20px;"

# Title of the app
st.title("Simple Calculator by Huu An")

# User input for two numbers and operation
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)

# Define the buttons
add_button = st.button(label="+", key="add", style=button_style)
subtract_button = st.button(label="-", key="subtract", style=button_style)
multiply_button = st.button(label="x", key="multiply", style=button_style)
divide_button = st.button(label="÷", key="divide", style=button_style)

# Perform the selected operation
if add_button:
    result = num1 + num2
elif subtract_button:
    result = num1 - num2
elif multiply_button:
    result = num1 * num2
elif divide_button:
    if num2 == 0:
        st.write("Error: Division by zero!")
    else:
        result = num1 / num2

# Display the result
if "result" in locals():
    st.write("The answer is:", result)
