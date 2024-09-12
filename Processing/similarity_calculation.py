from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(job_embedding, resume_embeddings, resumes):
    similarities = cosine_similarity([job_embedding], resume_embeddings)[0]
    sorted_resumes = sorted(zip(similarities, resumes), reverse=True, key=lambda x: x[0])
    return sorted_resumes