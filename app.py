
# import module
import streamlit as st

# Title
st.title("Welcome To Calculator")


# import module
import streamlit as st

# radio button
# first argument is the title of calculator
# second argument is the options for the radio button
status = st.option("Select Operator: ", ('Adddition', 'Subtraction','Multiplication','Division'))

# conditional statement to print
# Male if male is selected else print female
# show the result using the success function
if (status == 'Addition'):
	st.success("Addition")
elif(status == 'Subtraction'):
	st.success("Subtraction")
elif(status == 'Multiplication'):
	st.success("Multiplication")
elif(status == 'Division'):
	st.success("Division")
