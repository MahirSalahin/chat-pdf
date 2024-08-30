import streamlit as st
from core.pdf_processing import get_pdf_text, get_text_chunks
from core.vector_store import get_vector_store
from core.conversational_chain import response_from_user_input

def main():
    st.set_page_config("Chat PDF")
    st.title("Chat PDF")

    if 'message' not in st.session_state:
        st.session_state.message = []
    
    for message in st.session_state.message:
        st.chat_message(message['role']).markdown(message['content'])

    user_question = st.chat_input("Ask a Question from the PDF File(s)")

    if user_question:
        st.chat_message('user').markdown(user_question)
        st.session_state.message.append({'role':'user', 'content': user_question})
        response = response_from_user_input(user_question)
        st.chat_message('assistant').markdown(response)
        st.session_state.message.append({'role':'assistant', 'content': response})

    with st.sidebar:
        st.title("Sidebar:")
        pdf_docs = st.file_uploader("Upload your PDF File(s) and Click on the Submit Button", accept_multiple_files=True)
        if st.button("Submit"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                if raw_text is None:
                    st.error("Error extracting text from PDF")
                    return
                text_chunks = get_text_chunks(raw_text)
                if text_chunks is None:
                    st.error("Error splitting text into chunks")
                    return
                get_vector_store(text_chunks)
                st.success("Done")

if __name__ == "__main__":
    main()