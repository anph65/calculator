import streamlit as st
import math

# Define the style for the circular buttons
button_style = "border-radius: 50%; height: 50px; width: 50px; font-size: 20px; text-align: center; line-height: 1.9;"

# Title of the app
st.title("Simple Calculator")

# User input for two numbers and operation
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)

# Define the buttons
add_button = st.markdown("<button style='" + button_style + "'>&plus;</button>", unsafe_allow_html=True)
subtract_button = st.markdown("<button style='" + button_style + "'>&minus;</button>", unsafe_allow_html=True)
multiply_button = st.markdown("<button style='" + button_style + "'>&times;</button>", unsafe_allow_html=True)
divide_button = st.markdown("<button style='" + button_style + "'>&divide;</button>", unsafe_allow_html=True)

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
