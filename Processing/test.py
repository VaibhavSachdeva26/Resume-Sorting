from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq



api_key = "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"

llm = ChatGroq(groq_api_key = api_key, model_name = 'llama-3.1-70b-versatile', temperature = 0.2, top_p = 0.2)



prompt = "what is your name"

response = llm.chat.completions.create(message = prompt)

print(response.content)