from dotenv import load_dotenv
from models import gpt_model
from langchain_core.prompts import ChatPromptTemplate,  SystemMessagePromptTemplate, HumanMessagePromptTemplate

load_dotenv()

base_template = ChatPromptTemplate([
    SystemMessagePromptTemplate.from_template("Твой стиль общения дружелюбный"),
    HumanMessagePromptTemplate.from_template("Отвечай на вопрос : {text}")
])

template = base_template.partial()

text = input("Введите текст: ")
prompt = template.format_messages(text=text)

response = gpt_model.invoke(prompt)

print(response.content)