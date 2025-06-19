
import streamlit as st
from sentence_transformers import SentenceTransformer
import openai
import os
import pandas as pd
import chromadb
from chromadb.config import Settings
# Set your OpenAI API key
import datetime
# time= datetime.time()
# print(time)
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, OpenAIChatCompletion, AzureTextCompletion
import semantic_kernel as sk
from semantic_kernel.connectors.ai.ai_exception import AIException
from semantic_kernel.kernel_exception import KernelException
# using in code now
from dotenv import load_dotenv
import os
# ------------------- Load API credentials from .env -------------------
load_dotenv("config.env")  
azure_openai_key_gpt4 = os.getenv("azure_openai_key_gpt4")
azure_openai_endpoint_gpt4 = os.getenv("azure_openai_endpoint_gpt4")
azure_openai_deployment_name_gpt4 =os.getenv("azure_openai_deployment_name_gpt4")
# print(azure_openai_deployment_name_gpt4,azure_openai_endpoint_gpt4,azure_openai_key_gpt4)

# ------------------- Model Config -------------------
temp = 0.23 #0.23
top_p = 0.23 #0.23
maxtokens=4096

# ------------------- Initialize Semantic Kernel Chat Service -------------------
kernel_chatbot_gpt4 = sk.Kernel()
kernel_chatbot_gpt4.add_chat_service("chat_completion", 
    AzureChatCompletion(azure_openai_deployment_name_gpt4, 
                        azure_openai_endpoint_gpt4, 
                        azure_openai_key_gpt4))
# ------------------- Initialize Embedding Model -------------------
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Helper to load Excel file and convert to text
def load_excel(file):
    df = pd.read_excel(file)
    return df.to_string(index=False)

# Helper to chunk text
def split_text(text, chunk_size=5000):
    print("hey splitting the text")
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# Creating Chroma collection and add documents
def create_chroma_collection(chunks):
    print("hey in creating collection")
    chroma_client = chromadb.PersistentClient(path="./chroma_store")
    collection = chroma_client.get_or_create_collection(name=f"doc_chunks_abc")
    embeddings = embedder.encode(chunks).tolist()
    print("encoding emdeddingss")
    ids = [f"doc_{i}" for i in range(len(chunks))]
    collection.add(documents=chunks, embeddings=embeddings, ids=ids)
    print("Added in collection")
    return collection

# Search relevant chunks
def retrieve_chunks(question, collection, k=3):
    q_embedding = embedder.encode([question])[0].tolist()
    results = collection.query(query_embeddings=[q_embedding], n_results=k)
    print("The retrieved contents are")
    return results['documents'][0]

# Ask llm for an answer
def get_answer(question, context):
    print("hey inside prompt function")
    prompt = f"Answer the question based on the context below.\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
    chat_function_gpt4 = kernel_chatbot_gpt4.create_semantic_function(prompt, "ChatBot", max_tokens=maxtokens, temperature=temp, top_p=top_p,)
    context_gpt4=kernel_chatbot_gpt4.create_new_context()
    chatbot_response =  chat_function_gpt4.invoke(context=context_gpt4)
    return chatbot_response.result

# Streamlit App
st.title("AI Agent for Excel Document QA")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])
question = st.subheader("Ask a question about the document")
# st.markdown("""
#     # <style>
#     #     .stApp {
#     #         background-image: url("https://images.unsplash.com/photo-1522075469751-3a6694fb2f61");
#     #         background-size: cover;
#     #         background-repeat: no-repeat;
#     #         background-attachment: fixed;
#     #     }
#     # </style>
# """, unsafe_allow_html=True)
if uploaded_file:
    with st.spinner("Processing document..."):
        text = load_excel(uploaded_file)
        chunks = split_text(text)
        collection = create_chroma_collection(chunks)
q_idx=0
while True:
                question = st.text_input(f"Ask question", key=f"q_{q_idx}")
                if question:
                    relevant = retrieve_chunks(question, collection)
                    context = "\n".join(relevant)
                    answer = get_answer(question, context)
                    # st.markdown(f"**Q:** {question}")
                    st.markdown(f"**A:** {answer}")
                    q_idx += 1
                else:
                    break