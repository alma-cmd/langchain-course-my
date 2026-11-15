import urllib.request
import urllib.error
import json
import os

API_KEY = os.getenv("OPENAI_API_KEY", "sk-YCB6MQms1VFnkc4S8cJqdf66hRU3rMwP")
BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.proxyapi.ru/v1").rstrip('/')

url = f"{BASE_URL}/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}
data = {
    "model": "openai/gpt-5.4-pro",
    "messages": [{"role": "user", "content": "Привет! Это тест."}]
}

req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')

try:
    with urllib.request.urlopen(req) as response:
        print("✅ УСПЕХ! Модель работает через chat/completions:")
        result = json.loads(response.read().decode())
        print(result['choices'][0]['message']['content'])
except urllib.error.HTTPError as e:
    print(f"❌ Ошибка {e.code} напрямую от сервера ProxyAPI:")
    print(e.read().decode())