import streamlit as st

st.set_page_config(page_title="Casio Fx-570 Calculator")

# Constants
NUM_BUTTON_COLS = 5
NUM_BUTTON_ROWS = 5
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 75

# State variables
current_value = ""
stored_value = None
current_operator = None

# Define the buttons
buttons = [
    "7", "8", "9", "/", "sqrt",
    "4", "5", "6", "*", "%",
    "1", "2", "3", "-", "1/x",
    "0", ".", "Ans", "+", "=",
    "(", ")", "AC", "M+", "M-",
]

# Helper functions
def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def handle_number_button(button):
    global current_value
    if is_number(button):
        current_value += button
        st.write(current_value)

def handle_operator_button(button):
    global stored_value, current_value, current_operator
    if current_value:
        if stored_value is None:
            stored_value = float(current_value)
        else:
            if current_operator == "+":
                stored_value += float(current_value)
            elif current_operator == "-":
                stored_value -= float(current_value)
            elif current_operator == "*":
                stored_value *= float(current_value)
            elif current_operator == "/":
                stored_value /= float(current_value)
        current_operator = button
        current_value = ""
        st.write(stored_value)

def handle_other_button(button):
    global stored_value, current_value, current_operator
    if button == "AC":
        stored_value = None
        current_value = ""
        current_operator = None
        st.write("")
    elif button == "sqrt":
        current_value = str(math.sqrt(float(current_value)))
        st.write(current_value)
    elif button == "%":
        current_value = str(float(current_value) / 100)
        st.write(current_value)
    elif button == "1/x":
        current_value = str(1 / float(current_value))
        st.write(current_value)
    elif button == ".":
        if "." not in current_value:
            current_value += "."
            st.write(current_value)
    elif button == "=":
        handle_operator_button("=")
        current_value = str(stored_value)
        stored_value = None
        current_operator = None
        st.write(current_value)
    elif button == "Ans":
        if stored_value is not None:
            current_value = str(stored_value)
            st.write(current_value)
    elif button == "M+":
        if stored_value is not None:
            stored_value += float(current_value)
            st.write(stored_value)
    elif button == "M-":
        if stored_value is not None:
            stored_value -= float(current_value)
            st.write(stored_value)

# Create the UI
col1, col2, col3, col4, col5 = st.columns(NUM_BUTTON_COLS)
button_cols = [col1, col2, col3, col4, col5]
for i, button in enumerate(buttons):
    row = i // NUM_BUTTON_ROWS
    col = i % NUM_BUTTON_ROWS
    button_col = button_cols[col]
    button_col.button(button, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, key=
# Define functions for each operation
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2
# Define dictionary to map operation symbols to functions
operations = {
    "+": add,
    "-": subtract,
    "×": multiply,
    "÷": divide
}
# Define main function for calculator app
def main():
    st.set_page_config(page_title="Casio Fx-570", page_icon=":heavy_division_sign:")
    st.title("Casio Fx-570")

    # Initialize variables
    num1 = 0
    num2 = 0
    operation = ""
    result = ""

    # Get user input for first number
    num1 = st.number_input("Enter first number", value=num1)

    # Get user input for operation
    operation = st.selectbox("Select operation", list(operations.keys()))

    # Get user input for second number
    num2 = st.number_input("Enter second number", value=num2)

    # Perform selected operation
    if st.button("Calculate"):
        try:
            result = operations[operation](num1, num2)
            st.success(f"{num1} {operation} {num2} = {result}")
        except ZeroDivisionError:
            st.error("Cannot divide by zero")
        except:
            st.error("Error occurred during calculation")
# Call main function to run app
if __name__ == "__main__":
    main()
