from openai import OpenAI

client = OpenAI(
    api_key="sk-ws-H.YHXYDDI.XP2Y.MEQCIFWTMraXMWLo8W1H0B-3U6HsPKIQ9exkPNS2Y1cY12YcAiBfcd3S9T4wm3HuJKCH71ObuvfI1kJ_4E27rmVIi0SUjg",
    base_url="https://ws-ji0i895p4rymg7s3.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)


# 发起流式请求​
# 这里调用了create方法，但和之前不同的是多了stream=True。这一行的作用是：
# model="doubao-pro"：指定用豆包Pro这个模型。
# messages=[...]：对话内容，这里只有一条用户消息："讲一下强化学习RL"。
# stream=True：开启流式模式。意思是“不要等全部写完再给我，写一点就发一点过来”。
stream = client.chat.completions.create(
    model="qwen3.8-max",
    messages=[{"role": "user", "content": "200字简单介绍自己"}],
    stream=True,
)


for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
