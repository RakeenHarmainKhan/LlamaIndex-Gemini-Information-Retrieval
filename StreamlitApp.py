import streamlit as st
import os

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model

def main():
    st.set_page_config("QA with Documents")
    
    st.header("QA with Documents (Information Retrieval)")
    
    # Upload document
    uploaded_file = st.file_uploader("Upload your PDF document", type=["pdf"])
    user_question = st.text_input("Ask your question")
    
    if st.button("Submit & Process"):
        if uploaded_file is not None:
            with st.spinner("Processing..."):
                
                # Save uploaded file to 'Data/' directory
                if not os.path.exists("Data"):
                    os.makedirs("Data")
                
                # Clear old files (optional, to avoid mixed data)
                for file in os.listdir("Data"):
                    os.remove(os.path.join("Data", file))
                
                # Save new file
                with open(os.path.join("Data", uploaded_file.name), "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # Now load and process
                document = load_data("Data")
                model = load_model()
                query_engine = download_gemini_embedding(model, document)
                response = query_engine.query(user_question)

                st.write(response.response)
        else:
            st.warning("Please upload a PDF before submitting.")

if __name__ == "__main__":
    main()
