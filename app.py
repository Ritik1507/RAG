import json
import os
import sys 
import boto3
import streamlit as st


from langchain_community.embeddings import BedrockEmbeddings
from langchain.llms.bedrock import Bedrock

from langchain.prompts import PromptTemplate
from langchain.chains import retrieval_qa

from langchain.vectorstores import FAISS

from QASystem.ingestion import data_ingestion,get_vector_store
 
from QASystem.retrievalandgeneration import get_titan_llm,get_response_llm