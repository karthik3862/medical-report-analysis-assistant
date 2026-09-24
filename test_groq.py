import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
api_key=os.getenv("XAI_API_KEY")

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=api_key
)

response = llm.invoke("Say hello in one sentence.")

print(response.content)