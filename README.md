# AI-chatbot

This repository contains a Streamlit-based web application that allows users to upload documents (Excel `.xlsx`, PDF `.pdf`, or Word `.docx`) and ask questions about their content using an AI-powered question-answering system. It leverages semantic search (ChromaDB + sentence transformers) and Azure OpenAI's GPT-4 for generating contextual answers.

## Instructions to Run the Application

### 1. Clone the Repository

Open your terminal or command prompt and run the following commands:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install Required Packages

Make sure Python 3.9 or above is installed. Then install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a file named `config.env` in the root folder of the project. Add the following content:

```env
azure_openai_key_gpt4=your_azure_openai_key
azure_openai_endpoint_gpt4=https://your-resource-name.openai.azure.com/
azure_openai_deployment_name_gpt4=your-deployment-name
```

Replace the values with your actual Azure OpenAI credentials.

### 4. Run the Streamlit App

In the same project directory, start the application:

```bash
streamlit run app.py
```

### 5. Access the App in Your Browser

After running the above command, Streamlit will launch a local server. Open the link it shows in your browser, usually:

```
http://localhost:8501
```

## Supported File Types

- Excel (`.xlsx`)
- PDF (`.pdf`)
- Word Document (`.docx`)
