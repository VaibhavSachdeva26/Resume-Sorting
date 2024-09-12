import streamlit as st
from Preprocessing.resume_processing import extract_text
from Processing.embedding_generation import generate_embeddings
from Processing.similarity_calculation import calculate_similarity

st.title("Resume Sorting Based on Job Description")
job_desc = st.text_area("Enter Job Description")
uploaded_files = st.file_uploader("Upload Resumes", accept_multiple_files=True, type=['pdf', 'doc', 'docx'])

if st.button("Process Resumes"):
    resume_texts = [extract_text(file) for file in uploaded_files]
    #job_desc_embedding = ''
    job_desc_embedding = generate_embeddings(job_desc)
    resume_embeddings = [generate_embeddings(text) for text in resume_texts]
    sorted_resumes = calculate_similarity(job_desc_embedding, resume_embeddings, resume_texts)
    for score, resume in sorted_resumes:
        st.write(f"Score: {score}, Resume: {resume}")


