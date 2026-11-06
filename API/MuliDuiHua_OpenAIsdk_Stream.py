from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

# 消息列表，存放对话历史
messages = [
    {"role": "system", "content": "你是一个专业助手，回答简洁清晰。"}
]

def chat_stream(): #相较于非流式 只替换了这个函数
    print("===== 流式多轮对话，输入 exit 退出 =====")
    while True:
        user_input = input("\n你：")
        if user_input.strip().lower() == "exit":
            print("对话结束")
            break
        messages.append({"role": "user", "content": user_input})

        stream = client.chat.completions.create(
            model=os.getenv("MODEL_NAME"),
            messages=messages,
            temperature=0.7,
            stream=True
        )
        print("AI：", end="", flush=True)
        full_reply = ""
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                text = chunk.choices[0].delta.content
                full_reply += text
                print(text, end="", flush=True)
        # 存入历史
        messages.append({"role": "assistant", "content": full_reply})


if __name__ == "__main__":
    chat_stream()
