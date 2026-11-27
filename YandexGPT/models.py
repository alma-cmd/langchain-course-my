from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

gpt_model = ChatOpenAI(model="gpt://b1giaff96gld1lcrpavf/yandexgpt-5-pro/latest", temperature=0, timeout=120, max_retries=0)
# deepseek_model = ChatDeepSeek(model="gpt://b1giaff96gld1lcrpavf/deepseek-v4.1-flash/latest", temperature=0, timeout=120, max_retries=0)