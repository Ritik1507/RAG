import json
import os
import sys
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS


embeddings = GoogleGenerativeAIEmbeddings(model="model/embedding-001")

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader=pdf_reader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text     


def get_text_chunks(text):
    text_splitter= RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks=text_splitter.split_text(text)  
    return chunks 



def get_vector_store(text_chunks):
    vector_store_faiss=FAISS.from_texts(text_chunks,embedding=embeddings)
    vector_store_faiss.save_local("faiss_index")

if __name__ == '__main__':
    text = get_pdf_text()
    chunks=get_text_chunks(text)
    get_vector_store(chunks)