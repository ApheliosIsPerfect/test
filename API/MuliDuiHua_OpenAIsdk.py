from openai import OpenAI #导入OpenAI客户端类
from dotenv import load_dotenv #导入环境变量加载工具
import os #导入操作系统模块

load_dotenv() #加载.env文件

# 创建客户端对象​
# 换服务商只需要改.env文件，不需要改代码。
client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

# 消息列表，存放对话历史
messages = [
    {"role": "system", "content": "你是一个专业助手，回答简洁清晰。"}
]

def chat():
    print("===== 多轮对话，输入 exit 退出 =====")
    while True:
        user_input = input("\n你：")
        if user_input.strip().lower() == "exit":
            print("对话结束")
            break

        # 添加用户消息到上下文
        messages.append({"role": "user", "content": user_input})

        # 向模型发送请求，调用模型，参数包括：
        # model：从环境变量读取模型名
        # messages：完整的对话历史（包含系统指令+之前所有对话）
        # temperature：控制回答的创造性
        # stream=False：非流式，等全部生成完再返回
        resp = client.chat.completions.create(
            model=os.getenv("MODEL_NAME"),
            messages=messages,
            temperature=0.7,
            stream=False  # True 开启流式输出
        )

        ai_reply = resp.choices[0].message.content
        print(f"AI：{ai_reply}")

        # 把AI回复加入历史，实现多轮记忆
        messages.append({"role": "assistant", "content": ai_reply})


if __name__ == "__main__":
    chat()
