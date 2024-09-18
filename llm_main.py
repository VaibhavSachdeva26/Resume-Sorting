import streamlit as st
import pandas as pd
import json
from Preprocessing.resume_processing import extract_text
from Processing.llm_processing import get_resume_score

st.title("LLM-based Resume Sorting")

job_desc = st.text_area("Enter Job Description")
uploaded_files = st.file_uploader("Upload Resumes", accept_multiple_files=True, type=['pdf', 'doc', 'docx','pptx'])

if st.button("Process Resumes"):
    resume_texts = [extract_text(file) for file in uploaded_files]
    table = []
    for resume in resume_texts:
        scores = get_resume_score(job_desc, resume)
        table.append(str(scores))

    data = [json.loads(item) for item in table]
    df = pd.DataFrame(data)
    sorted_df = df.sort_values(by='Rating', ascending=False)
    st.dataframe(sorted_df[['Name', 'Skills', 'Certification','Relevant Experience','Overall Experience', 'Rating']])



