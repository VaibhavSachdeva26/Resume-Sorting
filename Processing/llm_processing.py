from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq


def get_resume_score(job_description: str, resume_texts: str):
    api_key = "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"

    llm = ChatGroq(groq_api_key=api_key, model_name='llama-3.1-8b-instant', temperature=0, top_p=0.2)

    prompt_template = PromptTemplate(
        input_variables=["job_description", "resume_texts"],
        template="Job Description:\n{job_description}\n\n I just want the name of the candidate, his skills matching with resume, relevant certifications mentioned, Relevant years of experience in the required skills mentioned in JD just in numbers and the name fo the tool/tech without any explanation, Overall years of experience just in number without any explanation and rating out of 10 basis the percentage of resume matches the job description. all the skills should come in a string and not array and all the certifications should come in a string.  The output should be in JSON Format with just key value pair. Keyword json should not be there in the response. \n\nThe headers should be:'Name', 'Skills','Certification','Relevant Experience','Overall Experience','Rating'\n\nResume:\n{resume_texts}"
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
