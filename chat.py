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

# input 1
PMA = st.text(label="Post menstural age (PMA), units = weeks")
# input 2
WT = st.text(label="Weight (WT), units = kilograms")


st.write("Time of infusion = fixed at 2 hours")

# -------------------- to calculate eq. ----------------
def calculate():
    volume_of_distribution = PMA + WT
                                             
# -------------------- to print the results ----------------
    st.write("Volume of Distribution = ",volume_of_distribution)

# -------------------- to run the button ----------------
if st.button("Answer"):
    calculate()
