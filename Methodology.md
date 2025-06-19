
## Overview

This project implements an AI-powered question-answering system that allows users to upload documents (Excel, PDF, or Word) and interactively ask questions about their contents. The system leverages:

* *Streamlit* for building the web UI
* *ChromaDB* for semantic search over document chunks
* *Sentence Transformers* for embedding text
* *Azure OpenAI GPT-4* (via Semantic Kernel) for generating answers



## Key Functional Components

### 1. *Environment and API Key Loading*

python
from dotenv import load_dotenv
load_dotenv("config.env")


* Loads credentials from a config.env file.
* These include Azure OpenAI keys and deployment info.


### 2. *Model Initialization*

python
kernel_chatbot_gpt4 = sk.Kernel()
kernel_chatbot_gpt4.add_chat_service(...)
embedder = SentenceTransformer('all-MiniLM-L6-v2')


* Initializes Semantic Kernel and adds Azure OpenAI GPT-4 as the chat model.
* Loads a sentence transformer model for generating dense vector embeddings.



### 3. *File Reading Logic*

python
def load_pdf(file), load_docx(file), load_excel(file)


* Based on file extension, the appropriate function is called:

  * .xlsx: read with pandas
  * .pdf: read with fitz (PyMuPDF)
  * .docx: read with python-docx

These functions extract *raw text* from the file.



### 4. *Text Chunking*

python
def split_text(text, chunk_size=5000)


* Splits the long document into smaller chunks to support efficient vector storage and retrieval.
* Default chunk size is set to 5000 characters.


### 5. *Embedding and Storing in ChromaDB*

python
def create_chroma_collection(chunks)


* Embeds each chunk using the SentenceTransformer model.
* Stores them in a *new ChromaDB collection* (named uniquely using uuid).


### 6. *Semantic Retrieval*

python
def retrieve_chunks(question, collection, k=3)


* Embeds the user's question.
* Performs *vector similarity search* in ChromaDB to find the top k relevant chunks.



### 7. *Answer Generation*

python
def get_answer(question, context)


* Creates a prompt using the retrieved context and user question.
* Uses Semantic Kernel to query GPT-4 and return a natural language answer.



### 8. *Streamlit UI*

python
st.title(), st.file_uploader(), st.text_input(), st.markdown()


* Users upload a file → it’s processed.
* A new input box appears after every question.
* Q\&A is displayed in markdown format for clarity.


##  End-to-End Flow

1. *User uploads a document*
2. Text is extracted → split into chunks
3. Chunks are embedded and stored in ChromaDB
4. User asks a question
5. System finds relevant chunks using vector similarity
6. Prompt is passed to GPT-4 to generate an answer
7. UI displays the Q\&A, and allows for continuous interaction



##  Features Summary

| Feature         | Description                               |
| --------------- | ----------------------------------------- |
| File Support    | .xlsx, .pdf, .docx                  |
| Vector DB       | ChromaDB                                  |
| Embedding Model | SentenceTransformers (all-MiniLM-L6-v2) |
| LLM             | Azure OpenAI GPT-4                        |
| Framework       | Streamlit                                 |
| Semantic Kernel | For clean GPT-4 integration               |

---

##  Notes

* Every session creates a unique ChromaDB collection to avoid conflicts.
* The UI is dynamic and supports a chat-like flow.
* The background is customizable using inline CSS.
