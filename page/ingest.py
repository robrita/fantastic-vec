import streamlit as st

# Constants
MAX_FILES = 5
# Define all possible input types for use in the dashboard
ALL_INPUT_TYPES = ["website", "sitemap", "google sheets", "youtube", "pdf", "docx", "pptx", "csv", "xlsx", "md", "json", "html", "txt"]

# Home page
st.subheader("📥Ingest Data")

with st.container(border=True):
    # First select input method
    input_method = st.radio(
        ":blue[**Select Input Method:**]",
        ["Enter URL", "Upload File", "Enter KB"],
        index=None,
        horizontal=True
    )

    # Initialize variables
    url = None
    uploaded_file = None
    text_input = None
    
    # Show appropriate data types based on input method
    if input_method == "Enter URL":
        input_types = ["website", "sitemap", "google sheets", "youtube", "pdf"]
        input_type = st.radio(
            ":blue[**Select Data Type:**]",
            input_types,
            index=None,
            horizontal=True
        )
        if input_type:
            url = st.text_input(":blue[**Enter URL:**]")

    elif input_method == "Upload File":
        input_types = ["pdf", "docx", "pptx", "csv", "xlsx", "md", "json", "html", "txt"]
        input_type = st.radio(
            ":blue[**Select Data Type:**]",
            input_types,
            index=None,
            horizontal=True
        )
        if input_type:
            st.info(f"Maximum {MAX_FILES} files can be uploaded at once", icon="ℹ️")
            uploaded_file = st.file_uploader(f":blue[**Upload Your {input_type} File:**]", type=input_type, accept_multiple_files=True)
            if uploaded_file and len(uploaded_file) > MAX_FILES:
                st.error(f"Please upload a maximum of {MAX_FILES} files at a time")
                st.stop()
                
    elif input_method == "Enter KB":
        text_input = st.text_area(":blue[**Enter Your KB:**]")

    # Ingest button
    if input_method and st.button(":green[**Ingest**]"):
        with st.spinner("Processing..."):
            st.toast("running ingestion pipeline...", icon="✨")
            st.info(f"Check the status in the dashboard below.", icon="ℹ️")

# Dashboard
st.subheader("📊Dashboard")

with st.container(border=True):
    col1, col2 = st.columns(2)

    with col1:
        data_type = st.multiselect(
            ":blue[**Select Data Type:**]",
            ALL_INPUT_TYPES,
        )

    with col2:
        page_number = st.selectbox(
            ":blue[**Select Page Number:**]",
            (1, 2, 3),
        )

    # Refresh data
    if st.button(":green[**Refresh data**]"):
        with st.spinner("Processing..."):
            st.toast("pulling new data...", icon="✨")
