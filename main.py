import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from schemas.translates import TranslatedText

load_dotenv()

default_tone = "дружелюбный"

# values = {
#    "lang" : "романским",
#    "text" : input("Введите текст: "),
#    "tone" : input(f"Введите тон ({default_tone}): ").strip() or default_tone
# }

base_template = ChatPromptTemplate([
    SystemMessagePromptTemplate.from_template_file("prompts/system.txt", input_variables=["lang"]),
    SystemMessagePromptTemplate.from_template("Твой стиль общения: {tone}"),
    HumanMessagePromptTemplate.from_template("Скажи '{text}' на трех языках")
])

template = base_template.partial(lang="романским", tone=default_tone)

text = input("Введите текст: ")

prompt = template.format_messages(text=text)

# print(template.format(text=text))

model = ChatGoogleGenerativeAI(
   #model="openai/gpt-4.1-mini",
    model="gemini-3.5-flash-lite",
   #model="openai/gpt-5.4",
    #temperature=1,
    timeout=120,
    max_retries=0
    #,
    #base_url=os.getenv("GOOGLE_GEMINI_BASE_URL"),
    #api_key=os.getenv("GEMINI_API_KEY")
)

structured_model = model.with_structured_output(TranslatedText, strict=True)

response = structured_model.invoke(prompt)

# print(type(response))
# print(response.response_metadata)
# print(type(response.content))

# # Pydantic модель
# print(response.translates)
#
# # Словарь
# print(response.model_dump())

for translate in response.translates:
    print(f"{translate.language: >12}: {translate.text}")
