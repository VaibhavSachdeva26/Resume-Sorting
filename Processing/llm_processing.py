from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq


def get_resume_score(job_description: str, resume_texts: str):
    api_key = "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"

    llm = ChatGroq(groq_api_key=api_key, model_name='llama-3.1-8b-instant', temperature=0, top_p=0.2)

    prompt_template = PromptTemplate(
        input_variables=["job_description", "resume_texts"],
        template="Job Description:\n{job_description}\n\nI just want the name of the candidate, his skills matching with resume, certifications and rating of his/her resume in number without any explaination. all the skills should come in a string and not array and all the certifications should come in a string.  The output should be in JSON Format with just jey value pairn and keyword json should not be there. Rate the following resumes from 1 to 10 based on its relevance to the job:\n\nThe headers should be:'Name', Rating:'Skills','Certification'.'Ratings'\n\nResume:\n{resume_texts}"
    )

    chain = prompt_template | llm
    print(prompt_template)
    scores = []

    response = chain.invoke({"job_description":job_description, "resume_texts":resume_texts})

    try:
        score = response.content
        return score
    except ValueError:
        score = 0  # Handle parsing errors and default to 0 score

