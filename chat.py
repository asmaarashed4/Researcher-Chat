import streamlit as st # to import libarary
import math

# ---------------- to creates the title -------------------
st.title("Researcher Chat Assistant")
# ---------------- to creates a horizontal line -------------------
st.write("---")
 
# ---------------- to enter the Patient Parameters -------------------
st.header("Research Paper Info") # header 

st.write("Upload the file here")

st.write("Ask your Question")

title = st.text_input('Movie title', label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )

# -------------------- to calculate eq. ----------------
def calculate():
if text_input:
        st.write("You entered: ", text_input)
# -------------------- to run the button ----------------
if st.button("Answer"):
    calculate()
