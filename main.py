import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
#from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
load_dotenv()

default_tone = "дружелюбный"

#values = {
#    "lang" : "романским",
#    "text" : input("Введите текст: "),
#    "tone" : input(f"Введите тон ({default_tone}): ").strip() or default_tone
#}

base_template = ChatPromptTemplate([
    SystemMessagePromptTemplate.from_template_file("prompts/system.txt", input_variables=["lang"] ),
    SystemMessagePromptTemplate.from_template("Твой стиль общения: {tone}"),
    HumanMessagePromptTemplate.from_template("Скажи '{text}' на трех языках")
])

template =  base_template.partial(lang = "романским", tone = default_tone)

text = input("Введите текст: ")
prompt = template.format_messages(text = text)

print(template.format(text = text))

#model = ChatOpenAI(
#    model="openai/gpt-4.1-mini",
#    #model="openai/gpt-5.4",
#    temperature=1,
#   timeout=(10,120),
#    max_retries=0,
#    base_url=os.getenv("OPENAI_BASE_URL"),
#    api_key=os.getenv("OPENAI_API_KEY"),
#)

#response = model.invoke(prompt)

#print(type(response))
#print(response.response_metadata)
#print(type(response.content))
#print(response.content)