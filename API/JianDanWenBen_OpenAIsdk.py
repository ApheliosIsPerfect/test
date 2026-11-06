# 导入 OpenAI 客户端类
from openai import OpenAI

# 创建客户端实例 并传了两个参数
# client 是 OpenAI 类的实例
client = OpenAI(
    api_key="sk-ws-H.YHXYDDI.XP2Y.MEQCIFWTMraXMWLo8W1H0B-3U6HsPKIQ9exkPNS2Y1cY12YcAiBfcd3S9T4wm3HuJKCH71ObuvfI1kJ_4E27rmVIi0SUjg",
    base_url="https://ws-ji0i895p4rymg7s3.cn-beijing.maas.aliyuncs.com/compatible-mode/v1" 
)


# 发起对话请求
# 调用了客户端的 chat.completions.create 方法，参数含义如下：
# model：指定要用的模型名
# messages：对话历史，是一个列表，包含两条消息：
# 第一条 role: "system" 是系统指令，告诉模型扮演什么角色。
# 第二条 role: "user" 是用户真正想问的问题。
# temperature：控制回答的随机性，0.7 表示中等创造力
# 模型生成回答，然后把结果存入 response 变量
# response 是 ChatCompletion 类的实例
response = client.chat.completions.create(
    model="qwen3.8-max",
    messages=[
        {"role": "system", "content": "你是代码助手"},
        {"role": "user", "content": "解释一下RAG的原理"}
    ],
    temperature=0.7
)


# 打印模型回答​
# 从返回的结果中提取回答文本：
# response.choices 是一个列表，存放所有候选回复（通常只有一个）。
# [0] 取第一个回复。
# .message.content 取这条消息的文本内容
print(response.choices[0].message.content)
print(type(response))
