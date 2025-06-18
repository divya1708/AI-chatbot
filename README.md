# AI-chatbot
This repository contains a Streamlit-based web application that allows users to upload documents (Excel .xlsx, PDF .pdf, or Word .docx) and ask questions about their content using an AI-powered question-answering system. It leverages semantic search (ChromaDB + sentence transformers) and Azure OpenAI's GPT-4 for generating contextual answers.



🛠️ Instructions to Run the Application
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Install Required Packages
Make sure you have Python 3.9+ installed.

bash
Copy
Edit
pip install -r requirements.txt
3. Set Up Environment Variables
Create a file named config.env in the root folder with the following contents:

env
Copy
Edit
azure_openai_key_gpt4=your_azure_openai_key
azure_openai_endpoint_gpt4=https://your-resource-name.openai.azure.com/
azure_openai_deployment_name_gpt4=your-deployment-name
⚠️ Replace all the placeholders with your actual Azure OpenAI credentials.

4. Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
5. Open in Browser
After running, Streamlit will show a local URL like:

arduino
Copy
Edit
http://localhost:8501
Open it in your browser.

🧪 Supported File Types
Excel .xlsx

PDF .pdf

Word .docx
