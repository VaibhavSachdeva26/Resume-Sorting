import streamlit as st
from Preprocessing.resume_processing import extract_text
from Processing.llm_processing import get_resume_score

st.title("LLM-based Resume Sorting")

job_desc = st.text_area("Enter Job Description")
uploaded_files = st.file_uploader("Upload Resumes", accept_multiple_files=True, type=['pdf', 'doc', 'docx'])


if st.button("Process Resumes"):
    resume_texts = [extract_text(file) for file in uploaded_files]

    scores = [get_resume_score(job_desc, resume) for resume in resume_texts]
    #sorted_resumes = sorted(zip(scores, resume_texts), reverse=True, key=lambda x: x[0])

    st.write(scores)  # Display the first 500 characters
