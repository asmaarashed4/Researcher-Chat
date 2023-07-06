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

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

# -------------------- to calculate eq. ----------------
def calculate():
 st.write("Ask your Question")

# -------------------- to run the button ----------------
if st.button("Answer"):
    calculate()
