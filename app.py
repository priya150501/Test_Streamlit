
# import module
import streamlit as st

# Title
st.title("Hello GeeksForGeeks !!!")

# success
st.success("Success")

# success
st.info("Information")

# success
st.warning("Warning")

# success
st.error("Error")

# Exception - This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.execption(exp)
