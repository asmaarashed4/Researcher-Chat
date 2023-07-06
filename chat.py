import streamlit as st # to import libarary
import math
import wget
from langchain.embeddings.openai import OpenAIEmbeddings
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
import wget

# ---------------- to creates the title ------------------
st.title("Researcher Chat Assistant")
# ---------------- to creates a horizontal line -------------------
st.write("---")
 
# ---------------- to enter the Patient Parameters -------------------
st.header("Research Paper Info") # header 

st.write("Upload the file here")
quesation = st.text_input('Ask your q', '')
# -------------------- to calculate eq. ----------------
def calculate():
 st.write('Your Question is', quesation)

# -------------------- to run the button ----------------
if st.button("Answer"):
    calculate()
