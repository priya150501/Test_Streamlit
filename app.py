
# import module
import streamlit as st

# Title
st.title("Welcome To Calculator")


# Text Input

# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
var_1 = st.text_input("Enter First Number", "Type Here ...")
var_2 = st.text_input("Enter Second Number", "Type Here ...")


# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
operation = st.radio("Select Operator: ", ('Adddition', 'Subtraction','Multiplication','Division'))

# conditional statement to print
# show the result using the success function
if (operation == 'Addition'):
	st.success("Addition")
elif(operation == 'Subtraction'):
	st.success("Subtraction")
elif(operation == 'Multiplication'):
	st.success("Multiplication")
elif(operation == 'Division'):
	st.success("Division")
# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
	result = operation.title()
	st.success(result)


def cal():
	if(operation == 'Addition'):
		result = var_1 + var_2
	elif(operation == 'Subtraction'):
		result = var_1 - var_2
	elif(operation == 'Multiplication'):
		result = var_1 * var_2
	elif(operation == 'Division'):
		if(var_1==0 and var_2==0):
			result = 0
		else:
			result = var_1 / var_2
	else:
		result = 0

	st.success(f"Answer = {result}")
  
if st.button("Calculate result"):
    cal()


