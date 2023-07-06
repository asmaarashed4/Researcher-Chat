!pip install wget #python package to download files from internet
#langchain a software development framework designed to simplify the creation of applications using large language models
!pip install langchain
!pip install faiss-cpu
#tiktoken is a fast BPE tokeniser for use with OpenAI's models
!pip install tiktoken
#PyPDF2 is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files
!pip install PyPDF2
#we will use wget to download our pdf file
!pip install wget
# to work with openAI
!pip install openai
import streamlit as st # to import libarary
import math
import wget
from langchain.embeddings.openai import OpenAIEmbeddings
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS

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
