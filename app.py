
# import module
import streamlit as st

# Title
st.title("Welcome To Calculator")


# import module
import streamlit as st
status = st.options("Select Operator: ", ('Adddition', 'Subtraction','Multiplication','Division'))

# conditional statement to print
# show the result using the success function
if (status == 'Addition'):
	st.success("Addition")
elif(status == 'Subtraction'):
	st.success("Subtraction")
elif(status == 'Multiplication'):
	st.success("Multiplication")
elif(status == 'Division'):
	st.success("Division")
