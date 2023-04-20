import streamlit as st

# Title of the app
st.title("Simple Calculator by Huu An")

# User input for two numbers and operation
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)
operation = st.selectbox("Select an operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Perform the selected operation
if operation == "Addition":
    result = num1 + num2
elif operation == "Subtraction":
    result = num1 - num2
elif operation == "Multiplication":
    result = num1 * num2
elif operation == "Division":
    result = num1 / num2

# Display the result
st.write("The answer is:", result)
