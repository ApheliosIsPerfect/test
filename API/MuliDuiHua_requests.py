import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL") + "/chat/completions"
model = os.getenv("MODEL_NAME")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

messages = [{"role": "system", "content": "你是助手"}]

def chat_request():
    while True:
        user_text = input("\n你：")
        if user_text == "exit":
            break
        messages.append({"role": "user", "content": user_text})
        payload = {
            "model": model,
            "messages": messages,
            "temperature": 0.7
        }
        r = requests.post(base_url, headers=headers, json=payload)
        res_json = r.json()
        ans = res_json["choices"][0]["message"]["content"]
        print("AI：", ans)
        messages.append({"role": "assistant", "content": ans})

if __name__ == "__main__":
    chat_request()
