import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


load_dotenv()

model = ChatOpenAI(
    #model="openai/gpt-4.1-mini",
    model="openai/gpt-5.4-pro",
    temperature=1,
    timeout=(10,120),
    max_retries=0,
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

response = model.invoke([
    SystemMessage(content="Ты специалист по славянским языкам"  ),
    HumanMessage(content="Скажи 'Привет' на трех языках"),
])
print(type(response))
print(response.response_metadata)
print(type(response.content))
print(response.content)