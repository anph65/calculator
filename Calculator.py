import streamlit as st

# Set page title
st.set_page_config(page_title="Calculator App")

# Define calculator function
def calculator():
    # Initialize variables
    num1 = ""
    num2 = ""
    operation = ""
    result = ""

    # Create calculator display
    col1, col2 = st.columns(2)
    with col1:
        st.write("## Calculator")
        st.write("Enter a number and select an operation")
        num1 = st.number_input("First number", step=0.1)
    with col2:
        st.write("## Result")
        st.write(result)

    # Create operation buttons
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("+"):
            operation = "+"
    with col2:
        if st.button("-"):
            operation = "-"
    with col3:
        if st.button("*"):
            operation = "*"
    with col4:
        if st.button("/"):
            operation = "/"

    # Create second number input and calculate result
    num2 = st.number_input("Second number", step=0.1)
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"

    # Update result display
    col1, col2 = st.columns(2)
    with col2:
        st.write(result)

# Call calculator function
calculator()
