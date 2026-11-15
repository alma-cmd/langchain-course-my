import urllib.request
import urllib.error
import json
import os

API_KEY = os.getenv("OPENAI_API_KEY", "sk-YCB6MQms1VFnkc4S8cJqdf66hRU3rMwP")
BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.proxyapi.ru/v1").rstrip('/')

url = f"{BASE_URL}/models"
req = urllib.request.Request(url, headers={"Authorization": f"Bearer {API_KEY}"})

try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        all_models = [m.get("id") for m in data.get("data", []) if m.get("id")]

        # Фильтруем ТОЛЬКО модели с префиксом openai/
        openai_models = sorted([m for m in all_models if m.startswith("openai/")])

        print(f"\n✅ Найдено {len(openai_models)} моделей OpenAI:")
        for m in openai_models:
            print(f"   • {m}")

        # Ищем конкретно gpt-5
        gpt5_models = [m for m in openai_models if "gpt-5" in m.lower()]
        if gpt5_models:
            print(f"\n🔍 Модели GPT-5:")
            for m in gpt5_models:
                print(f"   ⭐ {m}")
        else:
            print("\n⚠️ Моделей с 'gpt-5' в названии не найдено!")

except urllib.error.HTTPError as e:
    print(f"\n❌ Ошибка HTTP {e.code}:")
    print(e.read().decode())
except Exception as e:
    print(f"\n❌ Произошла ошибка: {e}")