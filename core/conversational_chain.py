import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

def get_conversational_chain():
    try:
        prompt_template = """
        You are an AI assistant, Zorlan developed for PDF analysis, trained by Salahin.
        You are given a context and a question, you need to answer the question.\n
        context:\n {context}?\n
        question: \n{question}\n
        Answer:
        """

        model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.9)

        prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
        chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

        return chain
    except Exception as e:
        st.error(f"Error creating conversational chain: {e}")
        return None

def response_from_user_input(user_question):
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        new_db = FAISS.load_local("data/faiss_index", embeddings, allow_dangerous_deserialization=True)
        docs = new_db.similarity_search(user_question)

        chain = get_conversational_chain()
        if chain is None:
            st.error("Error creating conversational chain")
            return

        response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
        return response['output_text']
    except Exception as e:
        st.error(f"Error processing user input: {e}")
