import streamlit as st # to import libarary
import math

# ---------------- to creates the title ------------------
st.title("Researcher cchat Assistant")
# ---------------- to creates a horizontal line -------------------
st.write("---")
 
# ---------------- to enter the Patient Parameters -------------------
st.header("Research Paper Info") # header 

st.write("Upload the file here")
quesation = st.text_input('Ask your q, 'write here')
# -------------------- to calculate eq. ----------------
def calculate():
st.write('Your Question is', quesation)

# -------------------- to run the button ----------------
if st.button("Answer"):
    calculate()
