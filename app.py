
# import module
import streamlit as st

# Title
st.title("Welcome To Calculator")


# Text Input

# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
var_1 = st.number_input(label="Enter First Number")
var_2 = st.number_input(label="Enter Second Number")

st.write("Operation")

# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
operation = st.radio("Select Operator: ", ('Adddition', 'Subtraction','Multiplication','Division'))


def cal():
	if(operation == "Addition"):
		result = var_1 + var_2
	elif(operation == "Subtraction"):
		result = var_1 - var_2
	elif(operation == "Multiplication"):
		result = var_1 * var_2
	elif(operation == "Division"):
		if(var_1==0 and var_2==0):
			result = 0
		else:
			result = var_1 / var_2
	else:
		result = 0
	return result

  
if st.button("Calculate result"):
	st.success(f"Answer = {cal()}")

