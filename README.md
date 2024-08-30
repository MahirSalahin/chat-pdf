---
title: Chat PDF
emoji: 📋
colorFrom: purple
colorTo: green
sdk: streamlit
sdk_version: 1.35.0
app_file: app.py
pinned: false
---

# **Chat PDF**
This is a RAG(Retrieval Augmented Generation) project that allows users to upload PDF files, extract text from them, and then ask questions about the content of the PDFs. The application uses the Gemini model from Google Generative AI to generate responses to user questions.
Check this out here: https://salahin-chat-pdf.hf.space/


## **Features**
*  **Upload multiple PDF files**
* **Extract text from PDF files**
* **Split text into chunks for efficient processing**
* **Create a vector store from text chunks using FAISS**
* **Use a conversational chain to generate responses to user questions**
* **Display conversation history**

## **How to Use**
1. Upload one or more PDF files using the file uploader in the sidebar.
2. Click the "Submit" button to process the PDF files.
3. Ask a question about the content of the PDF files using the chat input box.
4. The application will generate a response to your question and display it in the chat window.


## **Technical Details**
The application uses the following libraries:
* `streamlit` for the web interface
* `PyPDF2` for extracting text from PDF files
* `Langchain` for creating a conversational chain
* `Google Generative AI` for generating responses to user questions
* `FAISS` for creating a vector store from text chunks

The application uses a recursive character text splitter to split text into chunks of 10,000 characters with an overlap of 1,000 characters.
The conversational chain uses a prompt template to generate responses to user questions.


## **Local Run**
To run the application locally, follow these steps:

1. Clone the repository using git clone.
```
git clone https://huggingface.co/spaces/Salahin/Pdf_Analysis
```
2. Install the required libraries using 
```
pip install -r requirements.txt.
```
3. Set your GOOGLE_API_KEY in the `.env` file.  
4. Run the application using 
```
streamlit run app.py
```

## License
This project is licensed under the MIT License.