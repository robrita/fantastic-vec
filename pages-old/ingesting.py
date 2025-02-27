import streamlit as st
import requests
from unstructured.partition.auto import partition
import pandas as pd
from bs4 import BeautifulSoup
import tempfile
import os

# Home page
st.subheader("📥Ingest Data")

input_types = ["website", "google sheets", ".pdf", ".docx", ".pptx", ".csv", ".xlsx", ".md", ".json", ".html", ".txt", "sitemap", "enter manually"]
input_type = st.selectbox(":blue[**Select Data Type:**]", options=input_types, index=None)

def ingest_data(input_type, input_method=None, url=None, uploaded_file=None, text_input=None):
    st.write(input_type, input_method, url, uploaded_file, text_input)
    try:
        parsed_text = ""
        
        if input_type in ["website", "sitemap", ".html"]:
            if input_type in ["website", "sitemap"]:
                response = requests.get(url)
                content = response.text
            else:  # .html file
                content = uploaded_file.getvalue().decode('utf-8')
                
            soup = BeautifulSoup(content, 'html.parser')
            parsed_text = ' '.join([p.get_text() for p in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])])
        
        elif input_type == "google sheets":
            sheet_id = url.split('/')[5]  # Extract sheet ID from URL
            parsed_text = f"Google Sheets content from: {sheet_id}"  # Implement actual Google Sheets API integration
        
        elif input_type == ".pdf":
            if input_method == "Enter URL":
                # Download PDF from URL
                response = requests.get(url)
                if response.status_code == 200:
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                        tmp_file.write(response.content)
                        tmp_file_path = tmp_file.name
                    
                    elements = partition(filename=tmp_file_path)
                    parsed_text = '\n'.join([str(element) for element in elements])
                    os.unlink(tmp_file_path)  # Clean up temp file
                else:
                    st.error(f"Failed to download PDF. Status code: {response.status_code}")
            else:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_file_path = tmp_file.name
                
                elements = partition(filename=tmp_file_path)
                parsed_text = '\n'.join([str(element) for element in elements])
                os.unlink(tmp_file_path)  # Clean up temp file
        
        elif input_type in [".docx", ".pptx"]:
            with tempfile.NamedTemporaryFile(delete=False, suffix=input_type) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_file_path = tmp_file.name
            
            elements = partition(filename=tmp_file_path)
            parsed_text = '\n'.join([str(element) for element in elements])
            os.unlink(tmp_file_path)  # Clean up temp file
        
        elif input_type in [".csv", ".xlsx"]:
            if input_type == ".csv":
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            parsed_text = df.to_string()
        
        elif input_type in [".json", ".txt", ".md"]:
            parsed_text = uploaded_file.getvalue().decode('utf-8')
        
        elif input_type == "enter manually":
            parsed_text = text_input
        
        # Display parsed content
        if parsed_text:
            st.success("Content parsed successfully!")
            st.text_area("Parsed Content:", parsed_text, height=300)
        else:
            st.error("No content was parsed. Please check your input.")
            
    except Exception as e:
        st.error(f"Error processing the input: {str(e)}")

if input_type:
    # Initialize variables
    url = None
    uploaded_file = None
    text_input = None
    input_method = None

    # Text input for URL-based sources or file upload based on type
    if input_type == ".pdf":
        input_method = st.radio("Select input method:", ["Upload File", "Enter URL"])
        if input_method == "Enter URL":
            url = st.text_input("Enter PDF URL:")
        else:
            uploaded_file = st.file_uploader("Upload your PDF file", type="pdf", accept_multiple_files=True)
    elif input_type in ["website", "google sheets", "sitemap"]:
        url = st.text_input("Enter URL:")
    elif input_type in [".docx", ".pptx", ".csv", ".xlsx", ".md", ".json", ".html", ".txt"]:
        uploaded_file = st.file_uploader(f"Upload your {input_type} file", type=input_type.replace(".", ""), accept_multiple_files=True)
    elif input_type == "enter manually":
        text_input = st.text_area("Enter your text:")

    # Add ingest button
    if st.button("Ingest"):
        with st.spinner("Processing..."):
            ingest_data(input_type, input_method, url, uploaded_file, text_input)
